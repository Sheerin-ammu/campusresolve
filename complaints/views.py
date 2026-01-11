from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Complaint

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


@login_required
def dashboard(request):
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'complaints/dashboard.html', {'complaints': complaints})



@login_required(login_url="login")
def submit_complaint(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Complaint.objects.create(user=request.user, text=text)
            return redirect("dashboard")

    return redirect("dashboard")


def logout_view(request):
    logout(request)
    return redirect("login")
