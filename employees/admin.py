# -*- coding: utf-8 -*-
import re
from django import forms
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from employees.models import Employee, Department, JobPosition


class DepartmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Department, DepartmentAdmin)


class JobPositionAdmin(admin.ModelAdmin):
    pass

admin.site.register(JobPosition, JobPositionAdmin)


class SendEmailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    message = forms.CharField(widget=forms.Textarea)

    def normalize(self, _selected_action):
        return map(int, re.sub("[\[\]u' ',]", '', _selected_action))

    def save(self):
        data = self.cleaned_data
        message = data['message']
        _selected_action = data['_selected_action']
        _selected_action = self.normalize(_selected_action)

        employees = Employee.objects.filter(id__in=_selected_action)
        print employees, message


def send_employee_email(self, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    form = SendEmailForm(initial={'_selected_action': selected})

    context = {'form': form}

    if 'send' in request.POST:
        form = SendEmailForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
        else:
            return render_to_response("admin/send_email.html", context,
                                      context_instance=RequestContext(request))

    return render_to_response("admin/send_email.html", context,
                              context_instance=RequestContext(request))


description = 'Enviar email para os Funcionários selecionados'
send_employee_email.short_description = description


class EmployeeAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Employee, {'user': 'user'})

    def get_name(self, obj):
        return obj.user.get_full_name()
    get_name.short_description = 'Nome'
    get_name.admin_order_field = 'user__name'

    list_display = ('get_name', 'birthday_date', 'department', 'job_position',
                    'status',)
    actions = [send_employee_email]

admin.site.register(Employee, EmployeeAdmin)
