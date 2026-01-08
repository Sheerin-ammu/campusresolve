from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint


@login_required
def dashboard(request):
    complaints = Complaint.objects.filter(student=request.user)
    return render(request, 'dashboard.html', {'complaints': complaints})


@login_required
def submit_complaint(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        Complaint.objects.create(
            student=request.user,
            title=title,
            description=description
        )
        return redirect('dashboard')

    return render(request, 'submit.html')
