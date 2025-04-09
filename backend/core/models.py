from django.db import models
from django.conf import settings

class Retreat(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField()  # to define sequence of retreats
    unlocked_by_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Mission(models.Model):
    title = models.CharField(max_length=100)
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE, related_name='missions')
    description = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.retreat.title} - {self.title}"


class Meditation(models.Model):
    title = models.CharField(max_length=100)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='meditations')
    audio_url = models.URLField()
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.mission.title} - {self.title}"


class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    meditation = models.ForeignKey(Meditation, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'meditation')

    def __str__(self):
        return f"{self.user.username} - {self.meditation.title}"
