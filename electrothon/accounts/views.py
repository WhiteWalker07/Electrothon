from django.contrib.auth import get_user_model,authenticate
from django.shortcuts import render,redirect
from django.contrib.auth import login as authlog
from django.contrib.auth import logout as authlogout
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
User = get_user_model()
def login(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None :
            print("loged in")
            authlog(request,user)
            return redirect("borrow")
            
        else :
            messages.info("invalid Username or Password")
            return redirect("login")
    else :
        return render(request,'Login.html')
    
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['date']
        email = request.POST['email']
        contact = int(request.POST['phone_no'])
        institute = request.POST['institute']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        agree =  request.POST['agree-term']
        if password1 == password2 :
            if User.objects.filter(username=username).exists() :
                messages.info(request,'username exists')
                return redirect("register")
            elif User.objects.filter(email=email).exists() :
                messages.info(request,'email alredy registered try with Another one')
                return redirect("register")
            else :
                user = User.objects.create_user( username = username , password = password1 , first_name = first_name , last_name = last_name , email = email, phone = contact , institute = institute , dob =dob)
                user.save()
                print("USER CREATED !!!!!")
                return redirect("/")   
        else :
            messages.info(request,'Password and Confirm Password are not matching')
            return redirect("register")
    else :
        return render(request,'Register.html')

def logout(request):
    authlogout(request,user)
    return redirect('/')