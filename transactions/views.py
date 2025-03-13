from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListCreateView(ListCreateAPIView):
  serializer_class = TransactionSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, OrderingFilter]
  filterset_fields = ['category']
  ordering_fields = ['amount']
  def get_queryset(self):
    return Transaction.objects.filter(user=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
    
  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    return Response(
        {
          "message": "Transaction created successfully",
          "data": response.data
        },
        status=status.HTTP_201_CREATED
        )
  
class TransactionDetailView(RetrieveUpdateDestroyAPIView):
  serializer_class = TransactionSerializer
  permission_classes = [permissions.IsAuthenticated]
  def get_queryset(self):
    return Transaction.objects.filter(user=self.request.user)
