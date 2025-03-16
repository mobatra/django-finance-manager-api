from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "user", "amount", "category", "description", "date", "receipt"]
        read_only_fields = ["id", "user", "date"]

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value