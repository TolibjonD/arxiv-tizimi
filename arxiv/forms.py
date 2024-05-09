from .models import Folders, Files
from django import forms

class FolderForm(forms.ModelForm):
    folder_name = forms.CharField(max_length=120, help_text="Papka nomini kiriting")
    class Meta:
        model = Folders
        fields = ['folder_name']

class FilesForm(forms.ModelForm):
    file_name = forms.CharField(max_length=120, help_text="Fayl nomini kiriting")
    class Meta:
        model = Files
        fields = ['file_status', 'file_name', 'about_file', 'file']