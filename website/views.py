from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

def home(request):
    # Check to see if loggin in
    records = Record.objects.all().order_by("-created_at").values()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in ...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})




def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out ...")
    return redirect('home')
