# signal to save and update review rating whenever a review is added or deleted
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Review

@receiver([post_save, post_delete], sender=Review)
def update_university_rating(sender, instance, **kwargs):
    instance.university.update_rating()