# -*- coding: utf-8 -*-
from datetime import date
from django.contrib import admin
from model_mommy import mommy
from emailusernames.utils import create_user
from django.test import TestCase
from employees.admin import DepartmentAdmin
from employees.models import Department


class DepartmentAdminTest(TestCase):
    def test_get_employees(self):
        department = DepartmentAdmin(Department, admin.ModelAdmin)

        self.assertEqual(1, department.get_employees(self.department))

    def setUp(self):
        self.department = mommy.make('employees.Department',
                                     name='Recursos Humanos')
        job_position = mommy.make('employees.JobPosition', name='Gerente')

        user = create_user('pedro@xpto.com.br', '1234')
        user.first_name = 'Pedro'
        user.last_name = 'Bandeira'
        user.save()

        mommy.make('employees.Employee', user=user, department=self.department,
                   status=20, birthday_date=date(1980, 10, 25),
                   job_position=job_position)
