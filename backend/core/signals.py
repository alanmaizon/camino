# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProgress, Meditation

@receiver(post_save, sender=UserProgress)
def unlock_next_meditation(sender, instance, created, **kwargs):
    if instance.completed:
        retreat_meditations = Meditation.objects.filter(retreat=instance.retreat).order_by("order")
        current_index = list(retreat_meditations).index(instance.meditation)

        if current_index + 1 < retreat_meditations.count():
            next_meditation = retreat_meditations[current_index + 1]
            UserProgress.objects.get_or_create(
                user=instance.user,
                retreat=instance.retreat,
                meditation=next_meditation,
                defaults={'completed': False}
            )
