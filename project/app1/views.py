from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Product,cart

# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        if User.objects.filter(username=username).exists():
            return render(request,"registration.html",{'message':"username already exists"})
        password=request.POST['password']
        data=User.objects.create(name=name,email=email,username=username,password=password)
        data.save()
        return render(request,"login.html")
    else:
        return render(request,"registration.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            data=User.objects.get(username=username)
            if data.password==password:
                request.session['id']=data.id
                return redirect(profile)
            else:
                return render(request,'login.html',{'message':"Password doesn't match"})
        except Exception:
            return render(request,'login.html',{'message':'Username doesnot exists'})
        
    else:
        return render(request,'login.html',)
    
def profile(request):
    if 'id' in request.session:
        id=request.session['id']
        data=User.objects.get(id=id)
        return render(request,'profile.html',{'data':data})
    else:
        return render(request,'login.html')
    

def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)
    else:
        return render(request,'login.html')

def addproduct(request):
     if 'id' in request.session:
        id=request.session['id']
        data=User.objects.get(id=id)
        if request.method =="POST":
            productname=request.POST==['productname']
            details=request.POST==['details']
            data=Product.objects.create(productname=productname,details=details)
            data.save()
            return redirect(viewproducts)
            # return render(request,'viewblog.html',{'data':blogg})
        else:
            return render(request,'addproduct.html')
    
def viewproducts(request):
    if 'id' in request.session:
        id=request.session['id']
        user = User.objects.get(id=id)
        product = Product.objects.filter(user=user)
        return render(request,'viewblog.html',{'data':product})
    else:
        return render(request,'profile.html')
    
def deleteproduct(request):
    if 'id' in request.session:
        id=request.session['id']
        data=Product.objects.get(id=id)
        data.delete()
    



    
