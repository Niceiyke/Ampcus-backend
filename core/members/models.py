from django.db import models
from django.contrib.auth import get_user_model
import uuid


User=get_user_model()

# Create your models here.


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="member"
    )
    monthly_contribution = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=70, blank=True, null=True)
    bank_account = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=70, blank=True, null=True)
    total_contribution = models.PositiveIntegerField(default=0)
    total_loan = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
