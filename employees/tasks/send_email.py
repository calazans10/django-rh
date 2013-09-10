# -*- coding: utf-8 -*-
from celery import task
from employees.notification import EmployeeNotification


@task()
def send_email(employees, message):
    for employee in employees:
        notification = EmployeeNotification(employee, message)
        notification.send()
    return 'Ok'
