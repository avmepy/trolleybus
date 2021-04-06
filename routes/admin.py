from django.contrib import admin
from routes.models import Stop, Schedule, Route, ScheduledStop

admin.site.register(Stop)
admin.site.register(Schedule)
admin.site.register(Route)
admin.site.register(ScheduledStop)
