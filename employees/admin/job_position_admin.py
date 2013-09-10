# -*- coding: utf-8 -*-
from django.contrib import admin
from employees.models import JobPosition


class JobPositionAdmin(admin.ModelAdmin):
    pass

admin.site.register(JobPosition, JobPositionAdmin)
