from django.urls import path
from .views import TransactionListCreateView, TransactionDetailView, GenerateUploadURL,GenerateDownloadURL

urlpatterns = [
    path("", TransactionListCreateView.as_view(), name="transaction-list-create"),
    path("<int:pk>", TransactionDetailView.as_view(), name="transaction-detail"),
    path("s3/upload-url/", GenerateUploadURL.as_view(), name="generate-upload-url"),
    path("s3/download-url/<str:filename>/", GenerateDownloadURL.as_view(), name="generate-download-url"),
]