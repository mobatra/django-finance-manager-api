from transactions.models import Transaction
from django.contrib.auth import get_user_model
import random

User = get_user_model()
user = User.objects.first()

CATEGORY_CHOICES = ["food", "transport", "rent", "shopping", "utilities", "entertainment", "others"]

for i in range(15):
    Transaction.objects.create(
        user=user,
        amount=random.randint(10, 500),
        category=random.choice(CATEGORY_CHOICES),
        description=f"Test transaction {i+1}"
    )

print("✅ Successfully created 15 test transactions!")