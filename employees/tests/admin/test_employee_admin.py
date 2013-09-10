# -*- coding: utf-8 -*-
from datetime import date
from django.contrib import admin
from model_mommy import mommy
from emailusernames.utils import create_user
from django.test import TestCase
from employees.admin import EmployeeAdmin
from employees.models import Employee


class DepartmentAdminTest(TestCase):
    def test_get_name(self):
        employee = EmployeeAdmin(Employee, admin.ModelAdmin)

        self.assertEqual('Pedro Bandeira', employee.get_name(self.employee))

    def test_get_department(self):
        employee = EmployeeAdmin(Employee, admin.ModelAdmin)

        self.assertEqual('Recursos Humanos',
                         employee.get_department(self.employee))

    def test_get_job_position(self):
        employee = EmployeeAdmin(Employee, admin.ModelAdmin)

        self.assertEqual('Gerente', employee.get_job_position(self.employee))

    def test_change_status_action(self):
        # TODO: criar
        pass

    def test_admin_permission_action(self):
        # TODO: criar
        pass

    def test_send_email_action(self):
        # TODO: criar
        pass

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
