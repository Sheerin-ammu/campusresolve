from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Solved', 'Solved'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudentProfile(models.Model):
    student = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student_profile')
    parent = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='parent_profile')

    def __str__(self):
        return f"{self.student.username} - Parent"
