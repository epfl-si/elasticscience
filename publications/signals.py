from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Publication


@receiver(post_save, sender=Publication)
def index_publication(sender, instance, **kwargs):
    instance.indexing()
