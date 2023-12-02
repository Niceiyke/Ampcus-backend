from django.db.models.signals import post_save
from django.dispatch import receiver
from members.models import Member
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
import pyshorteners


@receiver(post_save, sender=CustomUser)
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        member = Member.objects.create(user=instance)
        member.save()


@receiver(post_save, sender=CustomUser)
def save_member_profile(sender, instance, **kwargs):
    instance.member.save()


@receiver(post_save, sender=CustomUser)
def send_successefull_signup(sender, instance, created, **kwargs):
    url = f"http://127.0.0.1:8000/api/member-update/{instance.member.id} "
    s = pyshorteners.Shortener()

    short_url = s.tinyurl.short(url)
    print("Shortened URL:", short_url)
    print("email", settings.EMAIL_HOST_USER)

    subject = "Successfull Registration "
    message = f"Thank you for registering with Ama Cooperative Society.\nuse this link {short_url} to update your profile "
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [instance.email]

    if created:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
