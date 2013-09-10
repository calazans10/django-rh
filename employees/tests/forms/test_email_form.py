# -*- coding: utf-8 -*-
from datetime import date
from model_mommy import mommy
from django.test import TestCase
from emailusernames.utils import create_user
from employees.forms import EmailForm


class EmailFormTest(TestCase):
    def test_normalize(self):
        form = EmailForm()
        self.assertEqual([self.employee.id], form._normalize(self.selected))

    def test_valid_form(self):
        data = {'_selected_action': self.selected, 'message': 'oi'}
        form = EmailForm(data=data)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'_selected_action': self.selected}
        form = EmailForm(data=data)

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['message'][0],
                         u'Este campo é obrigatório.')

    def test_save(self):
        data = {'_selected_action': self.selected, 'message': 'oi'}
        form = EmailForm(data=data)
        form.is_valid()

        try:
            form.save()
        except Exception:
            self.fail('Não foi possível executar a ação salvar.')

    def setUp(self):
        department = mommy.make('employees.Department',
                                name='Recursos Humanos')
        job_position = mommy.make('employees.JobPosition', name='Gerente')

        user = create_user('pedro@xpto.com.br', '1234')
        user.first_name = 'Pedro'
        user.last_name = 'Bandeira'
        user.save()

        self.employee = mommy.make('employees.Employee', user=user,
                                   department=department, status=20,
                                   birthday_date=date(1980, 10, 25),
                                   job_position=job_position)

        self.selected = str([unicode(self.employee.id)])
