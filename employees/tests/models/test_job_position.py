# -*- coding: utf-8 -*-
from model_mommy import mommy
from django.test import TestCase
from employees.models import JobPosition


class JobPositionTest(TestCase):
    def test_job_position_creation(self):
        self.assertTrue(isinstance(self.job_position, JobPosition))
        self.assertTrue(JobPosition.objects.all().count(), 1)
        self.assertEqual(self.job_position.__unicode__(), 'Gerente')

    def setUp(self):
        self.job_position = mommy.make('employees.JobPosition', name='Gerente')
