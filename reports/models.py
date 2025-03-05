from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    generated_at = models.DateTimeField(auto_now_add=True)
    file_url = models.URLField()

    def __str__(self):
        return f"Report for {self.user.username} - {self.generated_at}"
  