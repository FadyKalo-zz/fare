# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Diet'
        db.create_table(u'dietapp_diet', (
            ('diet_name', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('diet_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('diet_parameters', self.gf('django.db.models.fields.TextField')(null=True)),
            ('diet_description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dietapp', ['Diet'])

        # Adding model 'UserProfile'
        db.create_table(u'dietapp_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('weight', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('avg_cooking_time', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('current_diet', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dietapp.Diet'], unique=True, null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'dietapp', ['UserProfile'])

        # Adding model 'RecipeActivity'
        db.create_table(u'dietapp_recipeactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('recipe_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_liked', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('is_consumed', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dietapp', ['RecipeActivity'])

        # Adding unique constraint on 'RecipeActivity', fields ['user_id', 'recipe_id']
        db.create_unique(u'dietapp_recipeactivity', ['user_id_id', 'recipe_id'])

        # Adding model 'ActivityType'
        db.create_table(u'dietapp_activitytype', (
            ('activity_type_id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('activity_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'dietapp', ['ActivityType'])

        # Adding model 'ActivityEvent'
        db.create_table(u'dietapp_activityevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('recipe_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dietapp.ActivityType'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'dietapp', ['ActivityEvent'])

        # Adding model 'DietUser'
        db.create_table(u'dietapp_dietuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('diet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dietapp.Diet'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'dietapp', ['DietUser'])

        # Adding model 'UserDailyMeals'
        db.create_table(u'dietapp_userdailymeals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('meals', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dietapp', ['UserDailyMeals'])

        # Adding model 'Test_Model'
        db.create_table(u'dietapp_test_model', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'dietapp', ['Test_Model'])


    def backwards(self, orm):
        # Removing unique constraint on 'RecipeActivity', fields ['user_id', 'recipe_id']
        db.delete_unique(u'dietapp_recipeactivity', ['user_id_id', 'recipe_id'])

        # Deleting model 'Diet'
        db.delete_table(u'dietapp_diet')

        # Deleting model 'UserProfile'
        db.delete_table(u'dietapp_userprofile')

        # Deleting model 'RecipeActivity'
        db.delete_table(u'dietapp_recipeactivity')

        # Deleting model 'ActivityType'
        db.delete_table(u'dietapp_activitytype')

        # Deleting model 'ActivityEvent'
        db.delete_table(u'dietapp_activityevent')

        # Deleting model 'DietUser'
        db.delete_table(u'dietapp_dietuser')

        # Deleting model 'UserDailyMeals'
        db.delete_table(u'dietapp_userdailymeals')

        # Deleting model 'Test_Model'
        db.delete_table(u'dietapp_test_model')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dietapp.activityevent': {
            'Meta': {'object_name': 'ActivityEvent'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dietapp.ActivityType']"}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'dietapp.activitytype': {
            'Meta': {'object_name': 'ActivityType'},
            'activity_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'activity_type_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'})
        },
        u'dietapp.diet': {
            'Meta': {'object_name': 'Diet'},
            'diet_description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'diet_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'diet_parameters': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'diet_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'dietapp.dietuser': {
            'Meta': {'object_name': 'DietUser'},
            'diet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dietapp.Diet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'dietapp.recipeactivity': {
            'Meta': {'unique_together': "(('user_id', 'recipe_id'),)", 'object_name': 'RecipeActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_consumed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_liked': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'recipe_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'dietapp.test_model': {
            'Meta': {'object_name': 'Test_Model'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'test': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dietapp.userdailymeals': {
            'Meta': {'object_name': 'UserDailyMeals'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meals': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'dietapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'avg_cooking_time': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'current_diet': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['dietapp.Diet']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['dietapp']