from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout, password_validation

# Create your views here.

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['username'] and request.POST['password']:
                try:
                    u = User.objects.get(username=request.POST['username'])
                    user = authenticate(username = request.POST['username'], password=request.POST['password'])

                    if user is not None:
                        auth.login(request, user)
                        if request.POST["next"] != '':
                            return redirect(request.POST['next'])
                        else:
                            return redirect('/')
                    else:
                        return render(request, 'login.html', {'error':"Invalid credentials"})
                except User.DoesNotExist:
                    return render(request, 'login.html', {'error':"User Doesn't Exist"})
            else:
                return render(request, 'login.html', {'error':'Empty Fields'})
        else:
            return render(request, 'login.html')
    else:
        return redirect('/')

def signup(request):
    if request.method == "POST":
        #handle sign in
        if request.POST['password'] == request.POST['password2']:
            if request.POST['username'] and request.POST['email'] and request.POST['password']:
                try:
                    user = User.objects.get(email = request.POST['email'])
                    return render(request, 'signup.html', {'error': "User already exists"})
                except User.DoesNotExist:
                    User.objects.create_user(
                        username = request.POST['username'],
                        email = request.POST['email'],
                        password = request.POST['password']
                    )
                    
                    messages.success(request, "Signup Successful <br> Login Here")
                    return redirect(login)
            else:
                return render(request, 'signup.html', {'error': "Empty Fields"})
        else:
            return render(request, 'signup.html', {'error': "Password don't Match"})
    else: 
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/login')