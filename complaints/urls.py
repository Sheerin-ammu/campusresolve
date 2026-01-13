from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),

    path("admin/complaint/<int:complaint_id>/", views.update_complaint, name="update_complaint"),
]
