from django.db import models
from django.contrib.auth import get_user_model
from .choices import CATEGORY_CHOICES

User = get_user_model()

class Transaction(models.Model):
      user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="transaction")
      amount = models.DecimalField(max_digits=10, decimal_places=2)
      category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
      description = models.TextField(blank=True, null=True)
      date = models.DateField(auto_now_add=True)
      receipt = models.URLField(blank=True, null=True)
      def __str__(self):
        return f"{self.user.username} | {self.category} | {self.amount}"