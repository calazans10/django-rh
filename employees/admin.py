# -*- coding: utf-8 -*-
import re
from django import forms
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.core.mail import EmailMultiAlternatives
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
    message = forms.CharField(widget=forms.Textarea, label='Mensagem:')

    def _normalize(self, _selected_action):
        return map(int, re.sub("[\[\]u' ',]", '', _selected_action))

    def _send(self, employee, message):
        template_email = 'notification/email.html'
        subject = 'Comunicado'
        from_email = 'contato@xpto.com.br'
        to_email = employee.user.email

        cxt = {'employee': employee, 'message': message}

        html_content = loader.render_to_string(template_email, Context(cxt))
        message = EmailMultiAlternatives(subject, html_content, from_email,
                                         [to_email])
        message.attach_alternative(html_content, "text/html")
        message.send()

    def save(self):
        data = self.cleaned_data
        message = data['message']
        _selected_action = data['_selected_action']
        _selected_action = self._normalize(_selected_action)
        employees = Employee.objects.filter(id__in=_selected_action)

        for employee in employees:
            self._send(employee, message)
        return 'Ok'


def send_email_action(self, request, queryset):
    template_name = "admin/send_email.html"
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
    form = SendEmailForm(initial={'_selected_action': selected})

    context = {'form': form}

    if 'send' in request.POST:
        form = SendEmailForm(request.POST)
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


class EmployeeAdmin(AjaxSelectAdmin):
    form = make_ajax_form(Employee, {'user': 'user'})

    def get_name(self, obj):
        return obj.user.get_full_name()
    get_name.short_description = 'Nome'
    get_name.admin_order_field = 'user__name'

    list_display = ('get_name', 'birthday_date', 'department', 'job_position',
                    'status',)
    actions = [send_email_action]

admin.site.register(Employee, EmployeeAdmin)
