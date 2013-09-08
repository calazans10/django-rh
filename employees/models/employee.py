# -*- coding: utf-8 -*-
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


STATUS_CHOICES = (
    (10, 'inactive', 'Inativo'),
    (20, 'active', 'Ativo'),
)


class Employee(TimeStampedModel):
    STATUS = Choices(*STATUS_CHOICES)

    user = models.OneToOneField('auth.User', related_name='employee')
    photo = models.ImageField(upload_to='employee_photo')
    status = models.PositiveSmallIntegerField('Status', choices=STATUS)
    phone = models.CharField('Telefone', max_length=16)
    birthday_date = models.DateField('Data de Nascimento')
    department = models.ForeignKey('employees.Department')
    job_position = models.ForeignKey('employees.JobPosition')

    def __unicode__(self):
        return self.get_full_name()

    class Meta:
        app_label = 'employees'
        verbose_name = u'Funcionário'
        verbose_name_plural = u'Funcionários'
