from django.shortcuts import render
import requests

def home(request):
    url="https://jsonplaceholder.typicode.com/posts"
    req = requests.get(url)
    data = req.json()

    context = {
        'data': data
    }

    return render (request, 'index.html', context)



# Create your views here.


# username = richa
# password = test@123
