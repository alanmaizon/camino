from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Extend this later with XR/game-specific fields
    is_pilgrim = models.BooleanField(default=True)

    def __str__(self):
        return self.username
