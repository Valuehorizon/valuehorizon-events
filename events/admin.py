from django.contrib import admin

from events.models import Event, EventType


admin.site.register(Event)
admin.site.register(EventType)


