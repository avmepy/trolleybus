#!/usr/bin/env python3
# -*-encoding: utf-8-*-

from routes.models import Shift, Schedule
from openpyxl import Workbook


def report_worked_hours(driver, date_from, date_to):
    shifts = Shift.objects.filter(driver=driver, date__range=[date_from, date_to])
    schedules = []
    res = []
    hours = 6 * len(shifts)
    for shift in shifts:
        schedules += [Schedule.objects.filter(shift=shift)]
        res.append(f'{shift.date}, {shift}')

    wb = Workbook()
    ws = wb.active
    ws['A1'] = f'Report "worked hours"'
    ws['B1'] = f'from {date_from} to {date_to}'
    ws['C1'] = f'{driver.first_name} {driver.last_name}'
    ws['D1'] = f'total hours: {6 * len(res)}'
    for i in range(len(res)):
        ws[f'A{i+2}'] = res[i]

    # wb.save(f'{driver}_{date_from}_{date_to}.xlsx')
    return wb
