from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FolderForm, FilesForm
from .models import Folders, Files
from django.contrib import messages
from django.db.models import Q

from django.core.files.storage import default_storage


def change_filename(file, newFileName):
    ext = file.name.split('.')[-1]
    filename = "%s.%s" % (newFileName, ext)
    return filename

# Create your views here.
class Categories(LoginRequiredMixin, View):
    def get(self, request):
        folder_form = FolderForm()
        folders = Folders.objects.filter(Q(is_deleted=False) & Q(folder_owner=request.user)).order_by('-created_at')
        delete_id = request.GET.get('delete_id')
        if delete_id:
            folder = Folders.objects.get(id=delete_id)
            folder.is_deleted = True
            folder.save()
            messages.success(request, "Siz papkani o'chirib yubordingiz 😮")
        if request.GET.get('edit_folder_name_id'):
            folder_id = request.GET.get('edit_folder_name_id')
            folder = Folders.objects.get(id=folder_id)
            folder.folder_name = request.GET.get('edit_folder_name')
            folder.save()
            messages.success(request, "Siz papka nomini o'zgartirdingiz 🤥")
            return redirect("arxiv:folders")
        context = {
            "folders": folders,
            "folder_form": folder_form
        }
        return render(request, "arxiv/folders.html", context)
    
    def post(self, request):
        folder_form = FolderForm(data=request.POST, files=request.FILES)
        if folder_form.is_valid():
            folder = Folders(
                folder_owner = request.user,
                folder_name = folder_form.cleaned_data['folder_name']
            )
            folder.save()
            messages.success(request, "Siz yangi papka yaratdingiz 😜")
            return redirect("arxiv:folders")
        context = {
            "folder_form": folder_form
        }
        messages.success(request, "Afsuski, nimadur xato ketti 😔")
        return render(request, "arxiv/folders.html", context)
    
class FilesView(LoginRequiredMixin, View):
    def get(self, request, id):
        folder = Folders.objects.get(id=int(id))
        file_form = FilesForm()
        files = Files.objects.filter(Q(file_folder=folder) & Q(file_folder=folder) & Q(file_owner=request.user)).order_by("-created_at")
        change_file_status_to_public_id = request.GET.get("change_file_status_to_public_id")
        if change_file_status_to_public_id:
            file = Files.objects.get(id=change_file_status_to_public_id)
            file.file_status = 'PUBLIC'
            file.save()
            messages.success(request, "Siz faylni hammaga ko'rinadigan qilib o'zgartirdingiz 😜")
            return redirect(reverse("arxiv:files_list", kwargs={"id":folder.id}))
        change_file_status_to_private_id = request.GET.get("change_file_status_to_private_id")
        if change_file_status_to_private_id:
            file = Files.objects.get(id=change_file_status_to_private_id)
            file.file_status = 'PRIVATE'
            file.save()
            messages.success(request, "Bu fay endi faqat siz uchun ko'rinadi 😜")
            return redirect(reverse("arxiv:files_list", kwargs={"id":folder.id}))
        delete_file_id = request.GET.get("delete_file_id")
        if delete_file_id:
            file = Files.objects.get(id=delete_file_id)
            file.is_deleted = True
            file.save()
            messages.success(request, "Siz faylni o'chirib yubordingiz 😮")
            return redirect(reverse("arxiv:files_list", kwargs={"id":folder.id}))
        for file in files:
            file.file_type = str(file.file_type).split('/')[-1]
        context = {
            "folder": folder,
            "file_form": file_form,
            "files": files
        }
        return render(request, "arxiv/files.html", context)
    
    def post(self, request,id):
        folder = Folders.objects.get(id=int(id))
        file_form = FilesForm(data=request.POST, files=request.FILES)
        files = Files.objects.filter(Q(file_folder=folder) & Q(file_folder=folder) & Q(file_owner=request.user))
        context = {
            "folder": folder,
            "file_form": file_form,
            "files": files
        }
        if file_form.is_valid():
            file = file_form.cleaned_data['file']
            filename = change_filename(file, file_form.cleaned_data['file_name'])
            filename = default_storage.save(filename, file)
            file = Files(
                file_owner = request.user,
                file_folder = folder,
                file_status = file_form.cleaned_data['file_status'],
                file_name = file_form.cleaned_data['file_name'],
                about_file = file_form.cleaned_data['about_file'],
                file_type = str(request.FILES['file'].content_type).split('/')[-1],
                file = filename,
            )
            file.save()
            messages.success(request, "Siz yangi fayl joyladingiz 😜")
            return redirect(reverse("arxiv:files_list", kwargs={"id":folder.id}))
        return render(request, "arxiv/files.html", context)
    

class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        files = Files.objects.filter(Q(is_deleted=False) & Q(file_status="PUBLIC"))
        for file in files:
            file.file_type = str(file.file_type).split('/')[-1]
        context = {
            "files": files
        }

        return render(request, "arxiv/main_page.html", context)