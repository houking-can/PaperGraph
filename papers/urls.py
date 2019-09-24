from django.urls import path
from . import views
from .views import (
    UploadPDFView,
    UserUploadHistoryView,
    AdminUploadHistoryView,
    UserSpecifiedHistoryView,
    PDFOperationView,
    DeletePDFView,
    DeletePDFsView,
    DeleteOptView,
    # PDFPreviewView,

)


urlpatterns = [
    path("", views.index, name="papers_index"),
    path("upload/", UploadPDFView.as_view(), name="upload_pdf"),
    path(
        "process/history/user/<username>/",
        UserUploadHistoryView.as_view(),
        name="upload_history_user",
    ),
    path(
        "process/history/admin/<adminname>/",
        AdminUploadHistoryView.as_view(),
        name="upload_history_admin",
    ),
    path(
        "process/history/admin/<adminname>/specified/",
        UserSpecifiedHistoryView.as_view(),
        name="upload_history_specified",
    ),
    path("process/detail/<pk>/", PDFOperationView.as_view(), name="detail"),
    path("process/delete/PDF/<pk>/", DeletePDFView.as_view(), name="delete_pdf"),
    path("process/delete/PDF/", DeletePDFsView.as_view(), name="delete_pdfs"),
    path(
        "process/delete/operation/<pk>", DeleteOptView.as_view(), name="delete_opt"
    ),
    # path('process/preview/', PDFPreviewView.as_view(), name="preview_pdf")
]
