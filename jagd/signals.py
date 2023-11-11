from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Boulder
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from jagd.models import Boulder

@receiver(post_save, sender=User)
def create_boulder_entry(sender, instance, created, **kwargs):
    if created:
        Boulder.objects.create(user=instance)
