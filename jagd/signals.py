from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from jagd.models import U18M, U18W, UE50M, UE50W, BJM, BJW, UserProfile


#@receiver(post_save, sender=User)
#def create_boulder_entry(sender, instance, created, **kwargs):
