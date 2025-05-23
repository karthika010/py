from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def homepage(request):
    return render(request,'index.html')
    





    
def student_form(request):
       if(request.method =='POST'):
           name=request.POST.get('name')
           rollnumber=request.POST.get('rollno')
           email=request.POST.get('email') 
           student.objects.create(name=name,rollno=rollno,email=email)    
           return redirect('student_form')      
 
       students=students.objects.all()
        
       return render(request,'index.html',{'students':students})
 
