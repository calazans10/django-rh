# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Employee'
        db.create_table(u'employees_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('birthday_date', self.gf('django.db.models.fields.DateField')()),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employees.Department'])),
            ('job_position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employees.JobPosition'])),
        ))
        db.send_create_signal('employees', ['Employee'])

        # Adding model 'Department'
        db.create_table(u'employees_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('employees', ['Department'])

        # Adding model 'JobPosition'
        db.create_table(u'employees_jobposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('employees', ['JobPosition'])


    def backwards(self, orm):
        # Deleting model 'Employee'
        db.delete_table(u'employees_employee')

        # Deleting model 'Department'
        db.delete_table(u'employees_department')

        # Deleting model 'JobPosition'
        db.delete_table(u'employees_jobposition')


    models = {
        'employees.department': {
            'Meta': {'object_name': 'Department'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'employees.employee': {
            'Meta': {'object_name': 'Employee'},
            'birthday_date': ('django.db.models.fields.DateField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['employees.Department']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['employees.JobPosition']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'employees.jobposition': {
            'Meta': {'object_name': 'JobPosition'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['employees']