from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.dispatch import receiver
from .sendMail import request_tresurer_approval_email

from .models import Loan, LoanApprovalQueue


@receiver(pre_save, sender=Loan)
def update_is_declined(sender, instance, **kwargs):
    # Check if the loan is being declined
    if (
        instance.is_tresurer_declined
        or instance.is_president_declined
        or instance.is_user_declined
    ):
        # Set is_declined to True and update the date_declined field
        instance.is_declined = True
        instance.date_declined = timezone.now()
        loan_approval_queue = LoanApprovalQueue.objects.get(loan=instance.id)
        loan_approval_queue.delete()

    else:
        # Set is_declined to False if not declined
        instance.is_declined = False


@receiver(post_save, sender=Loan)
def add_loan_to_approval_queue(sender, instance, created, **kwargs):
    if created:
        loan_approval_queue = LoanApprovalQueue.objects.create()
        loan_approval_queue.loan.add(instance)
        request_tresurer_approval_email(instance=instance)
