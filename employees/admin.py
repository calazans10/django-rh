from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from employees.models import Employee, Department, JobPosition


class DepartmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Department, DepartmentAdmin)


class JobPositionAdmin(admin.ModelAdmin):
    pass

admin.site.register(JobPosition, JobPositionAdmin)


class EmployeeAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Employee, {'user': 'user'})

admin.site.register(Employee, EmployeeAdmin)
