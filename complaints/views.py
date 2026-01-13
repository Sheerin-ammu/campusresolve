from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Complaint


# ---------------- HOME ----------------
def home(request):
    return render(request, 'complaints/home.html')


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )

        if user:
            login(request, user)
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Student').exists():
                return redirect('student_dashboard')
            else:
                return HttpResponseForbidden("No role assigned")

        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------- REPORT ENTRY ----------------
@login_required
def report_entry(request):
    if not request.user.groups.filter(name='Student').exists():
        return HttpResponseForbidden("Admins cannot submit complaints")

    if request.method == "POST":
        Complaint.objects.create(
            user=request.user,
            text=request.POST.get("text")
        )
        return redirect('student_dashboard')

    return HttpResponseForbidden("Invalid request")


# ---------------- STUDENT DASHBOARD ----------------


@login_required
def student_dashboard(request):
    if request.user.groups.filter(name='Admin').exists():
        return HttpResponseForbidden("Admins cannot access student dashboard")

    if request.method == "POST":
        Complaint.objects.create(
            user=request.user,
            text=request.POST.get("text")
        )

    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')

    context = {
        "user": request.user,
        "complaints": complaints,
    }

    return render(request, "complaints/student_dashboard.html", context)





# ---------------- ADMIN DASHBOARD ----------------
@login_required
def admin_dashboard(request):
    if not request.user.groups.filter(name="Admin").exists():
        return HttpResponseForbidden("Access denied")

    complaints = Complaint.objects.all().order_by("-created_at")
    return render(request, "complaints/admin_dashboard.html", {
        "complaints": complaints
    })
    
@login_required
def update_complaint(request, complaint_id):
    if not request.user.groups.filter(name="Admin").exists():
        return HttpResponseForbidden()

    complaint = Complaint.objects.get(id=complaint_id)

    if request.method == "POST":
        complaint.status = request.POST.get("status")
        complaint.admin_remark = request.POST.get("admin_remark")
        complaint.save()
        return redirect("admin_dashboard")

    return render(request, "complaints/update_complaint.html", {
        "complaint": complaint
    })
