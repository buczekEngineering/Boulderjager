from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from jagd.models import U18M, U18W, UE50M, UE50W, BJM, BJW


@receiver(post_save, sender=User)
def create_boulder_entry(sender, instance, created, **kwargs):
    if created:
        U18M.objects.create(user=instance)
        U18W.objects.create(user=instance)
        UE50M.objects.create(user=instance)
        UE50W.objects.create(user=instance)
        BJM.objects.create(user=instance)
        BJW.objects.create(user=instance)
