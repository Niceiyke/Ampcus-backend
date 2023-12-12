from django.core.mail import send_mail


def request_treasurer_approval_email(instance):
    subject = "Loan Approval Notification"
    message = f"Loan for member {instance.member}, ia awaiting for approval, click this link to view it."
    from_email = "your_email@example.com"  # Replace with your email
    recipient_list = ["treasurer@ampcus.com"]  # Replace with the actual member email
    send_mail(subject, message, from_email, recipient_list)
