from django.contrib import admin
from .models import Folders, Files

# Register your models here.
@admin.register(Folders)
class AdminFolders(admin.ModelAdmin):
    search_fields = ['folder_name']
    list_filter = ['created_at', 'folder_owner','is_deleted']
    list_display = ['folder_name', 'folder_owner']

@admin.register(Files)
class AdminFiles(admin.ModelAdmin):
    search_fields = ['file_name']
    list_filter = ['created_at', 'file_status', 'file_type', 'file_owner']
    list_display = ['file_name', 'file_owner', 'file_status']
