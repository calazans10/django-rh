# -*- coding: utf-8 -*-
from datetime import date
from model_mommy import mommy
from django.test import TestCase
from emailusernames.utils import create_user
from employees.models import Employee


class EmployeeTest(TestCase):
    def test_employee_creation(self):
        self.assertTrue(isinstance(self.employee, Employee))
        self.assertEqual(Employee.objects.all().count(), 1)
        self.assertEqual(self.employee.__unicode__(), 'Pedro Bandeira')

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
