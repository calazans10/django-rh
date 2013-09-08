# -*- coding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


class JobPosition(TimeStampedModel):
    name = models.CharField('Nome', max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'employees'
        verbose_name = u'Cargo'
        verbose_name_plural = u'Cargos'
