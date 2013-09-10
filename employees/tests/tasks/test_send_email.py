# -*- coding: utf-8 -*-
from datetime import date
from model_mommy import mommy
from emailusernames.utils import create_user
from django.test import TestCase
from employees.tasks import send_email
from employees.models import Employee


class SendEmailTest(TestCase):
    def test_successful(self):
        # TODO: refatorar
        # employees = Employee.objects.all()
        # result = send_email.delay(employees, 'oi')

        # self.assertTrue(result.successful())
        pass

    def setUp(self):
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
