from django.contrib import admin

from app_api.models.event import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(Event, EventAdmin, )
