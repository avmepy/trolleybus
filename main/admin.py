from django.contrib import admin
from .models import Route, Trolleybus, TrolleybusState, StopPoint, Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('route', 'stop_point', 'time')


admin.site.register(Trolleybus)
admin.site.register(Route)
admin.site.register(TrolleybusState)
admin.site.register(StopPoint)
admin.site.register(Schedule, ScheduleAdmin)
