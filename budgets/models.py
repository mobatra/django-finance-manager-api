from django.db import models
from django.contrib.auth import get_user_model
from transactions.choices import CATEGORY_CHOICES

User = get_user_model()

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount_limit = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount_limit}"