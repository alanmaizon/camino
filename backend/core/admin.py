from django.contrib import admin
from .models import Retreat, Mission, Meditation, UserProgress

admin.site.register(Retreat)
admin.site.register(Mission)
admin.site.register(Meditation)
admin.site.register(UserProgress)
