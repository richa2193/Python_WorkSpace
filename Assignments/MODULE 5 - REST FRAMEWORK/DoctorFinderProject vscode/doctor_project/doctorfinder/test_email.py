from django.core.mail import send_mail

send_mail(
    'Test Email',
    'SMTP Working Successfully',
    'parmarricha2319@gmail.com',
    ['parmarricha2319@gmail.com'],
    fail_silently=False,
)