from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .models import Feature
from .models import Animal_Shelters
from .models import Adoption
from .models import AppliedAdoption
from .models import Volunteering
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import AdoptionForm
from .forms00 import VolunteeringForm
from .forms01 import RegForm

# Create your views here.
def index(request):
    features=Feature.objects.all()
    return render(request, 'index.html',{'feature':features})

def animalshelters(request):
   animshel=Animal_Shelters.objects.all()
   context={"animshels":animshel,}
   return render(request,'animalshelterspage.html',context)

def adoption(request):
   adopt=Adoption.objects.all()
   form=AdoptionForm()
   if request.method=='POST':

    form=AdoptionForm(request.POST)
    if form.is_valid():
      form.save()
   context1={"adopts":adopt, 'form':form}
   return render(request,'adoption.html',context1)

def volunteering(request):
  volunteer=Volunteering.objects.all()
  form00=VolunteeringForm()
  if request.method=='POST':

    form00=VolunteeringForm(request.POST)
    if form00.is_valid():
      form00.save()
  context3={"volunteers":volunteer,'form00':form00}
  return render(request,'volunteering.html',context3)

 

def counter(request):
     text=request.GET["text"]
     wordcount=len(text.split())
     return render(request, "counter.html",{'amount':wordcount})
     
def register(request):
  formreg=RegForm(request.POST)
  if request.method == 'POST':
    if(formreg.is_valid()):

     
     username=request.POST.get('username')
     email=request.POST.get('email')
     password=request.POST.get('password')
     confirmpassword=request.POST.get('confirm_Password')
     if password==confirmpassword:
        if User.objects.filter(email=email).exists():
          messages.info(request, 'Email Already Exists')
          return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Registered')
            return redirect('register')
        else:
          user=User.objects.create_user(username=username,email=email,password=password)
          user.save();
          return redirect('login')
     else: 
      messages.info(request,'Password Mismatch')
      return redirect('register')
    else: 
      return render(request,'register.html')
  else: 
    context5={'formreg':formreg}
    return render(request, 'register.html',context5)

def login(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('/')
    else:
      messages.info(request,'Please Enter The Correct Username And Password')
      return redirect('login')
      


  else:
    return render(request,'login.html')
def logout(request):
  auth.logout(request)
  return redirect('/')

def about(request):
  return render(request,'about.html')

def services(request):
  if User.is_authenticated:
    return render(request,'services.html')
  else:
    return redirect('login')


  