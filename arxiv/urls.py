from django.urls import path
from .views import (
    Categories,
    FilesView,
    MainPageView
)

app_name = "arxiv"
urlpatterns = [
    path("arxiv__folders/", Categories.as_view(), name="folders"),
    path("arxiv_folders/<int:id>/files_list/", FilesView.as_view(), name="files_list"),
    path("arxiv_folders/public/files/", MainPageView.as_view(), name="public_files")
]
