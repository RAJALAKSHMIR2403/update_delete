from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas       #datas is a class name



def home(request): # 127.0.0.1:8000/
    mydata=Datas.objects.all()
    if(mydata!=''):
       return render(request,'home.html',{'datas':mydata})
    else:
       return render(request, 'home.html')
 
   
    
def addData(request):
   if request.method=='POST':
      name=request.POST['name']      # this name, age, address is same as html./ name parameter
      age=request.POST['age']
      address=request.POST['address']
      contact=request.POST['contact']
      mail=request.POST['mail']

      obj=Datas()
      obj.Name=name              # Name,Age is same as a model .py
      obj.Age=age
      obj.Address=address
      obj.Contact=contact
      obj.Mail=mail
      obj.save()
      mydata=Datas.objects.all()   # Data is table name / class name set in model.py
      # return render(request, 'home.html',{'datas':mydata})
      return redirect('home')   # home refer to the url home page name=home 
   return render(request, 'home.html')

def updatedata(request,id):
   mydata=Datas.objects.get(id=id)
   if request.method=='POST':
      name=request.POST['name']      # this name, age, address is same as html./ name parameter
      age=request.POST['age']
      address=request.POST['address']
      contact=request.POST['contact']
      mail=request.POST['mail']

      mydata.Name=name
      mydata.Age=age
      mydata.Address=address
      mydata.Contact=contact
      mydata.Mail=mail
      mydata.save()
      return redirect("home")
   return render(request,"update.html",{'data':mydata})


       # Data is table name / class name set in model.py
      #return render(request, 'home.html',{'datas':mydata})
def deletedata(request,id):
   mydata=Datas.objects.get(id=id)
   mydata.delete()
   return redirect("home")