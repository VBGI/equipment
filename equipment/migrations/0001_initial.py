# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Equipment'
        db.create_table(u'equipment_equipment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=255)),
        ))
        db.send_create_signal(u'equipment', ['Equipment'])

        # Adding model 'Application'
        db.create_table(u'equipment_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=300)),
            ('organization', self.gf('django.db.models.fields.CharField')(default='', max_length=300, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='0', max_length=1, blank=True)),
            ('equipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipment.Equipment'], null=True)),
            ('starttime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 10, 12, 0, 0), blank=True)),
            ('endtime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 10, 12, 0, 0), blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('unum', self.gf('django.db.models.fields.CharField')(default='b6785dcc1658449fadddd6be1203383b', max_length=32)),
        ))
        db.send_create_signal(u'equipment', ['Application'])


    def backwards(self, orm):
        # Deleting model 'Equipment'
        db.delete_table(u'equipment_equipment')

        # Deleting model 'Application'
        db.delete_table(u'equipment_application')


    models = {
        u'equipment.application': {
            'Meta': {'ordering': "('equipment', 'status', 'organization', 'created', 'starttime')", 'object_name': 'Application'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 10, 12, 0, 0)', 'blank': 'True'}),
            'equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equipment.Equipment']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300'}),
            'organization': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 10, 12, 0, 0)', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'blank': 'True'}),
            'unum': ('django.db.models.fields.CharField', [], {'default': "'b6785dcc1658449fadddd6be1203383b'", 'max_length': '32'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'equipment.equipment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Equipment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['equipment']