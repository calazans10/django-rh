# -*- coding: utf-8 -*-
import re
from django import forms
from employees.models import Employee
from employees.tasks import send_email


class EmailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    message = forms.CharField(widget=forms.Textarea, label='Mensagem:')

    def _normalize(self, _selected_action):
        return map(int, re.sub("[\[\]u' ',]", '', _selected_action))

    def save(self):
        data = self.cleaned_data
        message = data['message']
        _selected_action = data['_selected_action']
        _selected_action = self._normalize(_selected_action)
        employees = Employee.objects.filter(id__in=_selected_action)

        send_email.delay(employees, message)
