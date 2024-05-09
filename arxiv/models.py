from django.db import models
from users.models import CustomUser
import uuid

# Create your models here.
class Folders(models.Model):
    class Meta:
        verbose_name_plural = "Folders"
        verbose_name = "Folder"
    folder_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=120)
    folder_photo = models.ImageField(upload_to="arxiv/folders/", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return f"{self.folder_name}"


class Files(models.Model):
    class Meta:
        verbose_name_plural = "Files"
        verbose_name = "file"
    STATUS = (
        ('PRIVATE', "Shaxsiy"),
        ('PUBLIC', "Hamma uchun")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file_folder = models.ForeignKey(Folders, on_delete=models.CASCADE, related_name="files")
    file_status = models.CharField(max_length=20,choices=STATUS, default="PRIVATE")
    file_name = models.CharField(max_length=120)
    about_file = models.TextField(blank=True, null=True)
    file_type = models.CharField(max_length=30)
    file = models.FileField(upload_to="arxiv/files/")
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self)->str:
        return f"{self.file_name}"