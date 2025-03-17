from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from .models import Transaction
from .serializers import TransactionSerializer
from utils.s3_utils import generate_presigned_url


class TransactionListCreateView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["category"]
    ordering_fields = ["amount"]

    def get_queryset(self):
        cache_key = f"user_transactions_{self.request.user.id}"
        transactions = cache.get(cache_key)
        if not transactions:
            transactions = list(Transaction.objects.filter(user=self.request.user))
            cache.set(cache_key, transactions, timeout=600)
        return transactions    

    def perform_create(self, serializer):
        transaction = serializer.save(user=self.request.user)
        cache_key = f"user_transactions_{self.request.user.id}"
        cache.delete(cache_key)
        return transaction
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {
                "message": "Transaction created successfully",
                "data": response.data,
            },
            status=status.HTTP_201_CREATED,
        )


class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cache_key = f"transaction_{self.kwargs['pk']}"
        transaction = cache.get(cache_key)
        if not transaction:
            transaction = Transaction.objects.filter(id=self.kwargs["pk"], user=self.request.user).first()
            if transaction:
                cache.set(cache_key, transaction, timeout=600)
        return [transaction] if transaction else []
    def perform_update(self, serializer):
        transaction = serializer.save()
        cache.delete(f"transaction_{transaction.id}")
        cache.delete(f"user_transactions_{self.request.user.id}")
        return transaction

    def perform_destroy(self, instance):
        cache.delete(f"transaction_{instance.id}")
        cache.delete(f"user_transactions_{self.request.user.id}")
        instance.delete()


class GenerateUploadURL(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        filename = request.data.get("filename")
        if not filename:
            return Response({"error": "Filename is required"}, status=400)

        presigned_url = generate_presigned_url(f"receipts/{filename}", "put_object")
        return Response({"upload_url": presigned_url})


class GenerateDownloadURL(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, filename):
        presigned_url = generate_presigned_url(f"receipts/{filename}", "get_object")
        return Response({"download_url": presigned_url})