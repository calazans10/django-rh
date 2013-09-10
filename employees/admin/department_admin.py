# -*- coding: utf-8 -*-
from django.contrib import admin
from employees.models import Department


class DepartmentAdmin(admin.ModelAdmin):
    def get_employees(self, obj):
        return obj.employee_set.all().count()
    get_employees.short_description = 'Funcionários'

    list_display = ('name', 'get_employees',)
    ordering = ['name']

admin.site.register(Department, DepartmentAdmin)
