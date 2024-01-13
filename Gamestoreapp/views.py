from django.shortcuts import render, redirect, HttpResponse
from Gamestoreapp.models import Game
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def create(request):
    #  print(request.method)
    if request.method == 'GET':
        
      return render(request, 'create.html')
  
    else:
        name = request.POST['name']
        age = request.POST['age']
        number = request.POST['number']
        cat = request.POST['cat']
        
        
        
        M = Game.objects.create(name = name, age = age, number = number, cat = cat)
        
        M.save()
        return redirect('/dashboard')
def dashboard(request):
    
    m = Game.objects.all()
    # print(m)
    
    context = {}
    context ['data'] = m
    
    return render(request, 'dashboard.html',context)

def delete(request, rid):
    m = Game.objects.filter(id = rid)
    
    m.delete()
    
    return redirect('/dashboard')

def edit(request, rid):
    
    if request.method == 'GET':
        
        m = Game.objects.filter(id = rid)
        
        context = {}
        context ['data'] = m
        return render(request, 'edit.html', context)
    
    else:
        name = request.POST['name']
        age = request.POST['age']
        number = request.POST['number']
        cat = request.POST['cat']
        
        m = Game.objects.filter(id = rid)
        
        m.update(name = name, age = age, number = number, cat = cat)
        
        return redirect('/dashboard')
    
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'GET':
        
        return render(request, 'registration.html')
    else:
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        upass = request.POST['upass']
        cpass = request.POST['cpass']
        
        if uname == "" or upass == "" or cpass == "":
            
            context = {}
            
            context['msg']= 'Fields Can not be empty'
            
            return render(request, 'registration.html', context)
        
        elif upass != cpass:
            context = {}
            context['msg']= 'Password and Confirm password should Be Same'
            return render(request, 'registration.html', context)
        
        else:
            u= User.objects.create(username=uname, email= uemail)
            u.set_password(upass)
        
            u.save()
            
            context = {}
            context['msg'] = "User Registered Successfully"
            return redirect('/login')
            
        
        
        
        
    
def user_login(request):
    
    if request.method == 'GET':
        
        return render(request, 'login.html')
    else:
        uname = request.POST['uname']
        upass = request.POST['upass']
        
        u = authenticate(username = uname, password = upass)
        
        
        if u is not None:
                login(request, u)
                return redirect('/')
            
        else:
            
            return HttpResponse ("User not found")
        
def user_logout(request):
    logout(request)
    
    return redirect("/")