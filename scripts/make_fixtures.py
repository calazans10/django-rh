# -*- coding: utf-8 -*-
from datetime import date
from django.db.models.loading import get_model
from django.template.defaultfilters import slugify
from emailusernames.utils import create_user
from employees.models import Employee, Department, JobPosition


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
    employee = Employee(user=user, status=20, phone=phone,
                        birthday_date=birthday_date, department=department,
                        job_position=job_position)
    employee.save()
    return employee


def make_data():
    comercial = make_department('Comercial')
    financeiro = make_department('Financeiro')
    rh = make_department('Recursos Humanos')
    juridico = make_department('Jurídico')
    ti = make_department('TI')

    ceo = make_job_position('CEO')
    cto = make_job_position('CTO')
    gerente = make_job_position('Gerente')
    dev = make_job_position('Desenvolvedor')
    designer = make_job_position('Designer')
    operacional = make_job_position('Operacional')

    birthday_date = date(1985, 10, 20)
    paula = make_employee('Paula', 'Rangel', '2185943327', birthday_date, rh,
                          gerente)
    paula.user.is_staff = True
    paula.user.is_superuser = True
    paula.user.save()

    birthday_date = date(1986, 06, 14)
    roberto = make_employee('Manuel', 'Conceição', '2187353320', birthday_date,
                            juridico, operacional)

    birthday_date = date(1987, 05, 27)
    roberto = make_employee('Rosana', 'Bastos', '2192353327', birthday_date,
                            juridico, gerente)

    birthday_date = date(1988, 06, 07)
    roberto = make_employee('Camila', 'Costa', '2182353329', birthday_date,
                            financeiro, operacional)

    birthday_date = date(1984, 01, 10)
    roberto = make_employee('Adélia', 'da Guia', '2194663327', birthday_date,
                            financeiro, gerente)

    birthday_date = date(1987, 05, 15)
    roberto = make_employee('Roberto', 'Silva', '2185943317', birthday_date,
                            rh, operacional)
    roberto.user.is_staff = True
    roberto.user.is_superuser = True
    roberto.user.save()

    birthday_date = date(1990, 02, 25)
    make_employee('Felipe', 'Magalhães', '218594397', birthday_date,
                  comercial, ceo)

    birthday_date = date(1988, 05, 15)
    make_employee('Mauro', 'Lima', '218894397', birthday_date,
                  ti, cto)

    birthday_date = date(1990, 07, 25)
    make_employee('Lilian', 'Ramos', '218694397', birthday_date,
                  ti, designer)

    birthday_date = date(1986, 01, 01)
    make_employee('Alberto', 'Brandão', '218694396', birthday_date,
                  ti, dev)


def run():
    clear_data()
    make_data()
