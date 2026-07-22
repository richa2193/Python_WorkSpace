import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomUserCreationForm, OTPVerificationForm, ForgotPasswordForm, ResetPasswordForm, ProfileUpdateForm

User = get_user_model()

def generate_otp():
    return str(random.randint(100000, 999999))

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False # Will be active after OTP
            otp = generate_otp()
            user.otp = otp
            user.save()
            
            # Send Email
            send_mail(
                'Verify your Doctor Finder Account',
                f'Your OTP for registration is {otp}',
                settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'noreply@doctorfinder.com',
                [user.email],
                fail_silently=False,
            )
            
            request.session['verification_email'] = user.email
            messages.success(request, 'Registration successful. Please check your email for the OTP.')
            return redirect('verify_otp')
    else:
        form = CustomUserCreationForm()
    return render(request, 'userapp/register.html', {'form': form})

def verify_otp_view(request):
    email = request.session.get('verification_email')
    if not email:
        messages.error(request, 'Session expired or invalid access.')
        return redirect('register')
        
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data.get('otp')
            try:
                user = User.objects.get(email=email)
                if user.otp == otp_entered:
                    user.is_active = True
                    user.is_email_verified = True
                    user.otp = '' # Clear OTP
                    user.save()
                    del request.session['verification_email']
                    messages.success(request, 'Email verified successfully. You can now login.')
                    return redirect('login')
                else:
                    messages.error(request, 'Invalid OTP. Please try again.')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
    else:
        form = OTPVerificationForm()
        
    return render(request, 'userapp/verify_otp.html', {'form': form, 'email': email})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        email_or_username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Simple support for login with email or username
        user_obj = None
        if '@' in email_or_username:
            try:
                user_obj = User.objects.get(email=email_or_username)
            except User.DoesNotExist:
                pass
        
        username = user_obj.username if user_obj else email_or_username
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_email_verified:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Please verify your email first.')
                request.session['verification_email'] = user.email
                return redirect('verify_otp')
        else:
            messages.error(request, 'Invalid credentials.')
            
    return render(request, 'userapp/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                user = User.objects.get(email=email)
                otp = generate_otp()
                user.otp = otp
                user.save()
                
                # Send Email
                send_mail(
                    'Reset your Doctor Finder Password',
                    f'Your OTP to reset password is {otp}',
                    settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'noreply@doctorfinder.com',
                    [user.email],
                    fail_silently=False,
                )
                
                request.session['reset_email'] = user.email
                messages.success(request, 'OTP sent to your email to reset password.')
                return redirect('reset_password')
            except User.DoesNotExist:
                messages.error(request, 'No user found with this email address.')
    else:
        form = ForgotPasswordForm()
    return render(request, 'userapp/forgot_password.html', {'form': form})

def reset_password_view(request):
    email = request.session.get('reset_email')
    if not email:
        messages.error(request, 'Session expired or invalid access.')
        return redirect('forgot_password')
        
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data.get('otp')
            new_password = form.cleaned_data.get('new_password')
            try:
                user = User.objects.get(email=email)
                if user.otp == otp_entered:
                    user.set_password(new_password)
                    user.otp = ''
                    user.save()
                    del request.session['reset_email']
                    messages.success(request, 'Password reset successfully. You can now login.')
                    return redirect('login')
                else:
                    messages.error(request, 'Invalid OTP. Please try again.')
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
    else:
        form = ResetPasswordForm()
        
    return render(request, 'userapp/reset_password.html', {'form': form, 'email': email})

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'userapp/dashboard.html')

@login_required(login_url='login')
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'userapp/profile.html', {'form': form})
