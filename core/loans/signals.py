from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.dispatch import receiver
from .sendMail import request_treasurer_approval_email

from .models import Loan, LoanApprovalQueue,Comment


@receiver(pre_save, sender=Loan)
def update_is_declined(sender, instance, **kwargs):
    # Check if the loan is being declined
    try:
        if (
   
        instance.is_president_declined
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
    
    except:
        pass

@receiver(pre_save, sender=Loan)
def update_is_approved(sender, instance, **kwargs):

    try:
        if (instance.is_president_approved):
            instance.is_approved = True
            instance.is_active =True
            instance.date_approved = timezone.now()
            loan_approval_queue = LoanApprovalQueue.objects.get(loan=instance.id)
            loan_approval_queue.delete()

        else:
            instance.is_approved = False
    
    except:
        pass
      

@receiver(post_save, sender=Loan)
def add_loan_to_approval_queue(sender, instance, created, **kwargs):
    if created:
        try:
            loan_approval_queue = LoanApprovalQueue.objects.create()
            loan_approval_queue.loan.add(instance)
            request_treasurer_approval_email(instance=instance)
        except:
            raise ValueError('loan does not exist as it has already been declined')
   

@receiver(post_save, sender=Comment)
def add_comment_to_loan(sender, instance, created, **kwargs):
    if created:
        try:
           
            loan= Loan.objects.get(id=instance.loan.id)
            loan.comments.add(instance)

        except Exception as e:
            raise Exception(e)