# -*- coding: utf-8 -*-
from model_mommy import mommy
from django.test import TestCase
from employees.models import Department


class DepartmentTest(TestCase):
    def test_creation_department(self):
        self.assertTrue(isinstance(self.department, Department))
        self.assertTrue(Department.objects.all().count(), 1)
        self.assertEqual(self.department.__unicode__(), 'Recursos Humanos')

    def setUp(self):
        self.department = mommy.make('employees.Department',
                                     name='Recursos Humanos')
