from django.shortcuts import render
from .models import Books
# Create your views here.

def borrow(request) :
    bsk = Books.objects.all()
    return render(request,'borrow.html',{ 'bsk' : bsk})

def profile(request) :
    return render(request,'Profile.html')
def lend(request) :
    return render(request,'lend.html')
def donate(request) :
    return render(request,'donate.html')
