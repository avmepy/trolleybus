import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from routes import services
from accounts.services import get_drivers
from routes import reports
from openpyxl.writer.excel import save_virtual_workbook

from routes.models import Shift, Schedule
from trolleybus2.settings import LOGIN_URL


class HomeView(View):

    def get(self, request):
        return render(self.request, 'routes/home.html')


class ScheduleView(LoginRequiredMixin, View):
    login_url = LOGIN_URL

    def get(self, request):

        shifts = services.get_user_shifts(self.request.user)

        context = {
            'shifts': shifts
        }
        return render(self.request, 'routes/schedules.html', context=context)


class ReportView(LoginRequiredMixin, View):
    login_url = LOGIN_URL

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
            if self.request.user.groups.filter(name='Водій').exists():
                wb = reports.report_worked_hours(self.request.user, date_from, date_to)
            else:
                driver = self.request.POST.get('driver')
                if driver == 'all_drivers':
                    wb = reports.report_worked_hours_all_drivers(date_from, date_to)
                else:
                    wb = reports.report_worked_hours(User.objects.get(id=int(driver)), date_from, date_to)
            return HttpResponse(save_virtual_workbook(wb), content_type='application/vnd.ms-excel')

        return render(self.request, 'routes/reports.html', context=context)


class GenerateShiftView(LoginRequiredMixin, View):
    login_url = LOGIN_URL

    def get(self, request):
        today = datetime.date.today()
        this_week_monday = today - datetime.timedelta(days=today.weekday())
        next_week_monday = today + datetime.timedelta(days=7-today.weekday())
        timedelda_days_7 = datetime.timedelta(days=7)

        Shift.objects.filter(date__gte=next_week_monday).delete()

        old_shifts = Shift.objects.filter(date__gte=this_week_monday)

        new_shifts = []
        for old_shift in old_shifts:
            new_shift = Shift.objects.create(driver=old_shift.driver,
                                             shift_kind=old_shift.shift_kind,
                                             date=old_shift.date + timedelda_days_7)
            for schedule in old_shift.schedules.all():
                new_shift.schedules.add(schedule)
            new_shifts.append(new_shift)
        messages.success(request, 'Успішно згенеровано!')

        return redirect('reports')
