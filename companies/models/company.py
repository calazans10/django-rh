# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Company(TimeStampedModel):
    name = models.CharField(u'Nome', max_length=128)
    corporate_name = models.CharField(u'Razão Social', max_length=255,
                                      blank=True)

    class Meta:
        app_label = 'companies'
        verbose_name = u'Empresa'
        verbose_name_plural = u'Empresas'
