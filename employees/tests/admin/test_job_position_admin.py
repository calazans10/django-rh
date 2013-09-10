# -*- coding: utf-8 -*-
from datetime import date
from django.contrib import admin
from model_mommy import mommy
from emailusernames.utils import create_user
from django.test import TestCase
from employees.admin import JobPositionAdmin
from employees.models import JobPosition


class JobPositionAdminTest(TestCase):
    def test_get_employees(self):
        job_position = JobPositionAdmin(JobPosition, admin.ModelAdmin)

        self.assertEqual(1, job_position.get_employees(self.job_position))

    def setUp(self):
        department = mommy.make('employees.Department',
                                     name='Recursos Humanos')
        self.job_position = mommy.make('employees.JobPosition', name='Gerente')

        user = create_user('pedro@xpto.com.br', '1234')
        user.first_name = 'Pedro'
        user.last_name = 'Bandeira'
        user.save()

        mommy.make('employees.Employee', user=user, department=department,
                   status=20, birthday_date=date(1980, 10, 25),
                   job_position=self.job_position)
