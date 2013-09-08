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

    first_name = models.CharField('Nome', max_length=255)
    last_name = models.CharField('Sobrenome', max_length=255)
    photo = models.ImageField(upload_to='employee_photo')
    email = models.EmailField('E-mail')
    status = models.PositiveSmallIntegerField('Status', choices=STATUS)
    phone = models.CharField('Telefone', max_length=16)
    birthday_date = models.DateField('Data de Nascimento')

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def __str__(self):
        return self.get_full_name()

    class Meta:
        app_label = 'companies'
        verbose_name = u'Funcionário'
        verbose_name_plural = u'Funcionários'
