from tkinter import E
from django.shortcuts import render,HttpResponse,redirect
#loading StudentForm from form.py inside students app
#from app_name.form import ModelForm_name
from students.form import StudentForm
from students.models import Student
# Create your views here.
def index(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()#persist data in database, using queryset(Django ORM API) method ==> create
            return redirect('../show')
            #return render(request,'show.html',{'form':form})
        else:
            pass
    else:
        obj=StudentForm()
        return render(request,'index.html',{'stu':obj}) #HTTP GET Method for displaying an empty form
        
def show(request):  
        students = Student.objects.all()  #similar to select * from student
        return render(request,"show.html",{'stu_list':students})  


#just display a form with filled fields
def edit(request, id):  
        stu = Student.objects.get(id=id)  
        return render(request,'edit.html', {'stu':stu})

def update(request, id):  
        stu =Student.objects.get(id=id)  
        form=StudentForm(request.POST, instance = stu)  
        if form.is_valid():  
            form.save()  
            return redirect("../show")
            #return render(request,'show.html')
        return render(request, 'edit.html', {'stu': stu})  

def destroy(request, id):  
    stu=Student.objects.get(id=id)  
    stu.delete() 
    return redirect("../show") 
    #return render(request,'show.html')
   
   
    '''org_name='TTL'
    student_name='Yashraj'
    return render(request,'index.html',{'msg':org_name})'''

def new_func():
    return redirect('show')
    
    
def upload(request):
    obj=StudentForm()
    return render(request,'upload.html',{'stu':obj})

