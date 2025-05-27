from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')
    





    
def student_form(request):
       if(request.method =='POST'):
           name=request.POST.get('name')
           rollno=request.POST.get('rollno')
           email=request.POST.get('email') 
           Student.objects.create(name=name,rollno=rollno,email=email)   
           print('fghjkl') 
           return redirect('student_form')      
 
       students=Student.objects.all()
       print('fghjkl') 
       return render(request,'index.html',{'students':students})
 


from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully.")
        return redirect('login')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_form')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def student_biodata(request):
    if request.method == 'POST':
        studentname = request.POST.get('studentname')
        rollno = request.POST.get('rollno')
        age = request.POST.get('age')
        gender = request.POST.get('gender') 
        
        address = request.POST.get('address')
        phoneno =request.POST.get('phoneno')
        department =request.POST.get('department')
        stream =request.POST.get('stream')
        Biodata.objects.create(studentname=studentname,rollno=rollno,age=age,gender=gender,address=address,phoneno=phoneno,department=department,stream=stream)   
            
        return redirect('student_biodata')      
 
    biodata=Biodata.objects.all()
        
    return render(request,'biodata.html',{'biodata':biodata})






def edit_biodata(request, pk):
    biodata = get_object_or_404(Biodata, pk=pk)

    if request.method == "POST":
        biodata.studentname = request.POST.get("studentname")
        biodata.rollno = request.POST.get("rollno")
        biodata.age = request.POST.get("age")
        biodata.gender = request.POST.get("gender") 
        
        biodata.address = request.POST.get("address")
        biodata.phoneno =request.POST.get("phoneno")
        biodata.department =request.POST.get("department")
        biodata.stream =request.POST.get("stream")
        biodata.save() 
        return redirect("edit_biodata", pk=biodata.pk)
        


    return render(request, "edit.html", {
        "edit_biodata": biodata,
        "biodata": Biodata.objects.all()
    })






def delete_biodata(request, pk):
    biodata = get_object_or_404(Biodata, pk=pk)
    biodata.delete()
    return redirect("edit_biodata")
