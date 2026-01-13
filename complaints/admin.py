from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'text')
    ordering = ('-created_at',)

    fields = ('user', 'text', 'status', 'admin_remark', 'created_at')
    readonly_fields = ('user', 'text', 'created_at')
