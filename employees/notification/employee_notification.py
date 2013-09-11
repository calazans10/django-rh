# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context


class EmployeeNotification(object):
    template_email = 'notification/email.html'

    def __init__(self, employee, subject, message):
        self.employee = employee
        self.message = message
        self.subject = subject
        self.from_email = 'contato@xpto.com.br'
        self.to_email = self.employee.user.email

    def get_context(self):
        cxt = {}
        cxt['employee'] = self.employee
        cxt['message'] = self.message

        return cxt

    def _send(self, cxt):
        html_content = loader.render_to_string(self.template_email,
                                               Context(cxt))
        message = EmailMultiAlternatives(self.subject, html_content,
                                         self.from_email, [self.to_email])
        message.attach_alternative(html_content, "text/html")
        message.send()
        return 'Ok'

    def send(self):
        cxt = self.get_context()

        return self._send(cxt)
