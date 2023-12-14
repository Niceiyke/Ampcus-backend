from django.db import models
from members.models import Member
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.


class LoanType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    interest = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan = models.ForeignKey("Loan", on_delete=models.CASCADE)
    description = models.CharField(max_length=240, blank=True)
    date_commented = models.DateTimeField(auto_now_add=True)
    attachments = models.FileField(upload_to='pdfs',blank=True, null=True)

    def __str__(self) -> str:
        super().__str__()
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ("date_commented",)


class LoanAwaitingDisbursmentQueue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    loan = models.ManyToManyField("Loan", blank=True)

    def __str__(self):
        self.loan.member


class LoanApprovalQueue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    loan = models.ManyToManyField("Loan", blank=True, related_name="approvalqueue")


class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member = models.ForeignKey(
        Member, on_delete=models.SET_NULL, null=True, related_name="loan"
    )
    loan_type = models.ForeignKey(LoanType, on_delete=models.SET_NULL, null=True)
    borrowed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    repaid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.ManyToManyField(Comment, blank=True, related_name="loanComment")
    is_active = models.BooleanField(default=False)
    is_treasurer_approved = models.BooleanField(default=False)
    is_president_approved = models.BooleanField(default=False)
    is_treasurer_declined = models.BooleanField(default=False)
    is_president_declined = models.BooleanField(default=False)
    is_user_declined = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_declined = models.BooleanField(default=False)
    date_initiated = models.DateTimeField(auto_now_add=True)
    date_declined = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_approved = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("-date_initiated",)

    def __str__(self):
        return f"{self.member.user.first_name} {self.member.user.last_name} - Loan: {self.borrowed_amount}"


class LoanRepayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="repayment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.loan.member.user.first_name} {self.loan.member.user.last_name} Repayment - {self.amount} on {self.payment_date}"


class VendorHomeAppliances(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class HomeAppliance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=240, null=True, blank=True)
    vendor = models.ForeignKey(VendorHomeAppliances, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    starting_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=240, null=True, blank=True)
    price = models.PositiveIntegerField()
    unit = models.CharField(max_length=50, blank=True, null=True)
    starting_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.name
