# -*- coding: utf-8 -*-
from django.conf import settings
from datetime import date
from model_mommy import mommy
from emailusernames.utils import create_user
from django.test import TestCase
from employees.tasks import send_email
from employees.models import Employee


class SendEmailTest(TestCase):
    def test_successful(self):
        employees = Employee.objects.all()
        result = send_email.delay(employees, 'Bem-vindo', 'oi')

        self.assertTrue(result.successful())

    def setUp(self):
        settings.CELERY_ALWAYS_EAGER = True
        settings.CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

        department = mommy.make('employees.Department',
                                name='Recursos Humanos')
        job_position = mommy.make('employees.JobPosition', name='Gerente')

        user = create_user('pedro@xpto.com.br', '1234')
        user.first_name = 'Pedro'
        user.last_name = 'Bandeira'
        user.save()

        mommy.make('employees.Employee', user=user, department=department,
                   status=20, birthday_date=date(1980, 10, 25),
                   job_position=job_position)
