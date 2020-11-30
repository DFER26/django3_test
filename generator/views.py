from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home (request):
    return render(request,'generator/home.html',{'password':'123456'})

def mysite (request):
    return HttpResponse ('This is my site..')

def numbers (request):

    characters = list('123')
    length = int(request.GET.get('length'))
    selectnumber = ''
    for x in range(length):
        selectnumber += random.choice(characters)

    return render(request,'generator/numbers.html',{'numbers':selectnumber})

def about (request):
    return render(request,'generator/about.html')
