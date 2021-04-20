from django.shortcuts import render
from django.views import View
from routes import services
from accounts.services import get_drivers


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


class ReportView(View):

    def get(self, request):
        context = {
            'drivers': get_drivers()
        }
        return render(self.request, 'routes/reports.html', context=context)

    def post(self, request):
        context = {
            'drivers': get_drivers()
        }
        return render(self.request, 'routes/reports.html', context=context)
