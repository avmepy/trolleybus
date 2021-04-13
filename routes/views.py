from django.shortcuts import render
from django.views import View
from routes import services


class HomeView(View):

    def get(self, request):
        return render(self.request, 'routes/home.html')


class ScheduleView(View):

    def get(self, request):
        schedules = services.get_user_schedules(self.request.user)
        context = {
            'schedules': schedules
        }
        return render(self.request, 'routes/schedules.html', context=context)
