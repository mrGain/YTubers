from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators  import login_required
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are Loggedin successfully !..")
            return redirect('dashboard')
        else:
            messages.warning(request,"Invalid Credintial")
            return redirect('login')
    return render(request, 'myusers/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username alresdy exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email is already registered')
                    return render('register')    
                else:
                    user = User.objects.create_user(
                        first_name=firstname,
                        last_name=lastname,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.success(request,"Acount created successfully")
                    return redirect('login')

        else:
            messages.warning(request,"Password does not mached.")
            return redirect('register')
        

    return render(request, 'myusers/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')
     
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'myusers/dashboard.html')