from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from routes import services
from accounts.services import get_drivers
from routes import reports
from openpyxl.writer.excel import save_virtual_workbook


class HomeView(View):

    def get(self, request):
        return render(self.request, 'routes/home.html')


class ScheduleView(View):

    def get(self, request):

        shifts = services.get_user_shifts(self.request.user)

        context = {
            'shifts': shifts
        }
        return render(self.request, 'routes/schedules.html', context=context)


class ReportView(View):

    def get(self, request):
        context = {
            'drivers': get_drivers()
        }
        return render(self.request, 'routes/reports.html', context=context)

    def post(self, request):

        report = self.request.POST.get('report')
        date_from = self.request.POST.get('from')
        date_to = self.request.POST.get('to')
        context = {
            'drivers': get_drivers()
        }

        if report == 'hours':
            wb = reports.report_worked_hours(self.request.user, date_from, date_to)
            return HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')

        return render(self.request, 'routes/reports.html', context=context)

