from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Executive
from members.models import Member


@receiver(post_save, sender=Executive)
def update_member_position(sender, instance, created, **kwargs):
    if created:
        print("created", instance.portfolio.id)
        member = Member.objects.filter(user=instance.name).first()

        if instance.portfolio.id == "135fac87-72b1-4526-81d2-2932fe3267b7":
            member.is_president = True
            member.save()
            print("president created created", member)

        elif instance.portfolio.id == "135fac87-72b1-4526-81d2-2932fe3267b7":
            member.is_treasurer = True
            member.save()
            print("trasurer created created", member)

        elif str(instance.portfolio.id) == "8813c009-ce5c-40cd-b70f-5326f9c56eb4":
            member.is_admin_officer = True
            member.save()
            print("addmin officer reated", instance.portfolio.id)
