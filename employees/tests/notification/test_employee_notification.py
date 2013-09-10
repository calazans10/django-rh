# -*- coding: utf-8 -*-
from datetime import date
from model_mommy import mommy
from emailusernames.utils import create_user
from django.test import TestCase
from employees.notification import EmployeeNotification


class EmployeeNotificationTest(TestCase):
    def test_get_context(self):
        notification = EmployeeNotification(self.employee, 'oi')
        context = notification.get_context()

        self.assertEqual(self.employee, context['employee'])
        self.assertEqual('oi', context['message'])

    def test_send(self):
        notification = EmployeeNotification(self.employee, 'oi')

        try:
            notification.send()
        except Exception:
            self.fail('Notificação não foi enviada.')

    def setUp(self):
        department = mommy.make('employees.Department',
                                name='Recursos Humanos')
        job_position = mommy.make('employees.JobPosition', name='Gerente')

        user = create_user('pedro@xpto.com.br', '1234')
        user.first_name = 'Pedro'
        user.last_name = 'Bandeira'
        user.save()

        self.employee = mommy.make('employees.Employee', user=user,
                                   department=department, status=20,
                                   birthday_date=date(1980, 10, 25),
                                   job_position=job_position)
