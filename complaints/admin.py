from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'student', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'student__username')
    ordering = ('-created_at',)
    list_editable = ('status',)
    readonly_fields = ('student', 'title', 'description', 'created_at')


admin.site.site_header = "CampusResolve Admin Panel"
admin.site.site_title = "CampusResolve Admin"
admin.site.index_title = "Grievance Management Dashboard"
