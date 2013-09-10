# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from employees.models import Employee
from employees.forms import EmailForm


def send_email_action(self, request, queryset):
    template_name = "admin/send_email.html"
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    form = EmailForm(initial={'_selected_action': selected})

    context = {'form': form}

    if 'send' in request.POST:
        form = EmailForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            self.message_user(request, 'Email enviado com sucesso.')
            return HttpResponseRedirect(request.get_full_path())
        else:
            return render_to_response(template_name, context,
                                      context_instance=RequestContext(request))
    elif 'cancel' in request.POST:
        self.message_user(request, 'Envio de email cancelado.')
        return HttpResponseRedirect(request.get_full_path())

    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))
description = 'Enviar email para os Funcionários selecionados'
send_email_action.short_description = description


def change_status_action(self, request, queryset):
    for obj in queryset:
        if obj.status is 20:
            obj.status = 10
        else:
            obj.status = 20
        obj.save()
description = 'Alterar status dos Funcionários selecionados'
change_status_action.short_description = description


def admin_permission_action(self, request, queryset):
    for obj in queryset:
        obj.user.is_staff = True
        obj.user.is_superuser = True
        obj.user.save()
description = 'Permitir acesso ao admin para os Funcionários selecionados'
admin_permission_action.short_description = description


class EmployeeAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Employee, {'user': 'user'})

    def get_name(self, obj):
        return obj.user.get_full_name()
    get_name.short_description = 'Nome'
    get_name.admin_order_field = 'user__name'

    def get_department(self, obj):
        return obj.department.name
    get_department.short_description = 'Departamento'
    get_department.admin_order_field = 'department__name'

    def get_job_position(self, obj):
        return obj.job_position.name
    get_job_position.short_description = 'Cargo'
    get_job_position.admin_order_field = 'job_position__name'

    list_display = ('get_name', 'birthday_date', 'get_department',
                    'get_job_position', 'status',)
    list_filter = ('status', 'department__name', 'job_position__name')
    ordering = ['-created']
    actions = [send_email_action, change_status_action,
               admin_permission_action]

admin.site.register(Employee, EmployeeAdmin)
