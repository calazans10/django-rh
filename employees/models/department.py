# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class Department(TimeStampedModel):
    name = models.CharField(u'Nome', max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'employees'
        verbose_name = u'Departamento'
        verbose_name_plural = u'Departamentos'
