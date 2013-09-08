# -*- coding: utf-8 -*-
from datetime import date
from django.db.models.loading import get_model
from django.template.defaultfilters import slugify
from emailusernames.utils import create_user
from employees.models import Employee, Department, JobPosition
from rh_system.urls import urlpatterns


def clear_model(app, model_cls):
    for obj in get_model(app, model_cls).objects.all():
        obj.delete()


def clear_data():
    clear_model('auth', 'User')
    clear_model('employees', 'Employee')
    clear_model('employees', 'Department')
    clear_model('employees', 'JobPosition')


def make_department(name):
    department = Department(name=name)
    department.save()
    return department


def make_job_position(name):
    job_position = JobPosition(name=name)
    job_position.save()
    return job_position


def make_user(first_name, last_name):
    email = "%s@xpto.com.br" % slugify(first_name)
    user = create_user(email, '1234')
    user.first_name = first_name
    user.last_name = last_name
    user.is_staff = True
    user.is_superuser = True
    user.save()
    return user


def make_employee(first_name, last_name, phone, birthday_date, department,
                  job_position):
    user = make_user(first_name, last_name)
    employee = Employee(user=user, status=10, phone=phone,
                        birthday_date=birthday_date, department=department,
                        job_position=job_position)
    employee.save()
    return employee


def run():
    clear_data()

    comercial = make_department('Comercial')
    # make_department('Financeiro')
    # make_department('Recursos Humanos')
    # make_department('Jurídico')
    # make_department('TI')

    ceo = make_job_position('CEO')
    # make_job_position('CTO')
    # make_job_position('Gerente')
    # make_job_position('Operacional')

    make_employee('Jeferson', 'Farias Calazans', '21-95184567',
                  date(1989, 10, 10), comercial, ceo)
