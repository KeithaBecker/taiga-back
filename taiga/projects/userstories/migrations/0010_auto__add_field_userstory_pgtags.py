# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserStory.pgtags'
        db.add_column('userstories_userstory', 'pgtags',
                      self.gf('djorm_pgarray.fields.TextArrayField')(null=True, dbtype='text', blank=True, default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserStory.pgtags'
        db.delete_column('userstories_userstory', 'pgtags')


    models = {
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'issues.issue': {
            'Meta': {'ordering': "['project', 'created_date']", 'object_name': 'Issue'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True', 'default': 'None', 'related_name': "'issues_assigned_to_me'"}),
            'blocked_note': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'finished_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['milestones.Milestone']", 'null': 'True', 'blank': 'True', 'default': 'None', 'related_name': "'issues'"}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True', 'default': 'None', 'related_name': "'owned_issues'"}),
            'pgtags': ('djorm_pgarray.fields.TextArrayField', [], {'null': 'True', 'dbtype': "'text'", 'blank': 'True', 'default': 'None'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Priority']", 'related_name': "'issues'"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'issues'"}),
            'ref': ('django.db.models.fields.BigIntegerField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True', 'default': 'None'}),
            'severity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Severity']", 'related_name': "'issues'"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.IssueStatus']", 'related_name': "'issues'"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tags': ('picklefield.fields.PickledObjectField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.IssueType']", 'related_name': "'issues'"}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'watchers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['users.User']", 'null': 'True', 'related_name': "'issues_issue+'", 'blank': 'True', 'symmetrical': 'False'})
        },
        'milestones.milestone': {
            'Meta': {'ordering': "['project', 'created_date']", 'unique_together': "(('name', 'project'),)", 'object_name': 'Milestone'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'disponibility': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True', 'default': '0.0'}),
            'estimated_finish': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'estimated_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True', 'related_name': "'owned_milestones'"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'milestones'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'blank': 'True', 'max_length': '250'}),
            'watchers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['users.User']", 'null': 'True', 'related_name': "'milestones_milestone+'", 'blank': 'True', 'symmetrical': 'False'})
        },
        'projects.issuestatus': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'IssueStatus'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'#999999'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'issue_statuses'"})
        },
        'projects.issuetype': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'IssueType'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'#999999'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'issue_types'"})
        },
        'projects.membership': {
            'Meta': {'ordering': "['project', 'role']", 'unique_together': "(('user', 'project'),)", 'object_name': 'Membership'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True', 'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'null': 'True', 'max_length': '255', 'blank': 'True', 'default': 'None'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'memberships'"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Role']", 'related_name': "'memberships'"}),
            'token': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '60', 'blank': 'True', 'default': 'None'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True', 'default': 'None', 'related_name': "'memberships'"})
        },
        'projects.points': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'Points'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'points'"}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True', 'default': 'None'})
        },
        'projects.priority': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'Priority'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'#999999'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'priorities'"})
        },
        'projects.project': {
            'Meta': {'ordering': "['name']", 'object_name': 'Project'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'creation_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectTemplate']", 'null': 'True', 'blank': 'True', 'default': 'None', 'related_name': "'projects'"}),
            'default_issue_status': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.IssueStatus']", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'+'"}),
            'default_issue_type': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.IssueType']", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'+'"}),
            'default_points': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Points']", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'+'"}),
            'default_priority': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Priority']", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'+'"}),
            'default_severity': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.Severity']", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'+'"}),
            'default_task_status': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.TaskStatus']", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'+'"}),
            'default_us_status': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['projects.UserStoryStatus']", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'+'"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_backlog_activated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_issues_activated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_kanban_activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_wiki_activated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['users.User']", 'through': "orm['projects.Membership']", 'related_name': "'projects'", 'symmetrical': 'False'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'related_name': "'owned_projects'"}),
            'pgtags': ('djorm_pgarray.fields.TextArrayField', [], {'null': 'True', 'dbtype': "'text'", 'blank': 'True', 'default': 'None'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'blank': 'True', 'max_length': '250'}),
            'tags': ('picklefield.fields.PickledObjectField', [], {'blank': 'True'}),
            'total_milestones': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': '0'}),
            'total_story_points': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': 'None'}),
            'videoconferences': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '250', 'blank': 'True'}),
            'videoconferences_salt': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '250', 'blank': 'True'})
        },
        'projects.projecttemplate': {
            'Meta': {'ordering': "['name']", 'object_name': 'ProjectTemplate'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'default_options': ('django_pgjson.fields.JsonField', [], {}),
            'default_owner_role': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_backlog_activated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_issues_activated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_kanban_activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_wiki_activated': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'issue_statuses': ('django_pgjson.fields.JsonField', [], {}),
            'issue_types': ('django_pgjson.fields.JsonField', [], {}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'points': ('django_pgjson.fields.JsonField', [], {}),
            'priorities': ('django_pgjson.fields.JsonField', [], {}),
            'roles': ('django_pgjson.fields.JsonField', [], {}),
            'severities': ('django_pgjson.fields.JsonField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'blank': 'True', 'max_length': '250'}),
            'task_statuses': ('django_pgjson.fields.JsonField', [], {}),
            'us_statuses': ('django_pgjson.fields.JsonField', [], {}),
            'videoconferences': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '250', 'blank': 'True'}),
            'videoconferences_salt': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '250', 'blank': 'True'})
        },
        'projects.severity': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'Severity'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'#999999'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'severities'"})
        },
        'projects.taskstatus': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'TaskStatus'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'#999999'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'task_statuses'"})
        },
        'projects.userstorystatus': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'UserStoryStatus'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20', 'default': "'#999999'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'us_statuses'"}),
            'wip_limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True', 'default': 'None'})
        },
        'users.role': {
            'Meta': {'ordering': "['order', 'slug']", 'unique_together': "(('slug', 'project'),)", 'object_name': 'Role'},
            'computable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'related_name': "'roles'", 'symmetrical': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'roles'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'max_length': '250'})
        },
        'users.user': {
            'Meta': {'ordering': "['username']", 'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'color': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '9', 'default': "'#b2ae34'"}),
            'colorize_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'default_language': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'default': "''"}),
            'default_timezone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'default': "''"}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '256'}),
            'github_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'null': 'True', 'max_length': '500', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True', 'default': 'None'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'userstories.rolepoints': {
            'Meta': {'ordering': "['user_story', 'role']", 'unique_together': "(('user_story', 'role'),)", 'object_name': 'RolePoints'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Points']", 'related_name': "'role_points'"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.Role']", 'related_name': "'role_points'"}),
            'user_story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['userstories.UserStory']", 'related_name': "'role_points'"})
        },
        'userstories.userstory': {
            'Meta': {'ordering': "['project', 'order', 'ref']", 'object_name': 'UserStory'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'null': 'True', 'blank': 'True', 'default': 'None', 'related_name': "'userstories_assigned_to_me'"}),
            'blocked_note': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'client_requirement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'finish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'generated_from_issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issues.Issue']", 'null': 'True', 'blank': 'True', 'related_name': "'generated_user_stories'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['milestones.Milestone']", 'default': 'None', 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'user_stories'"}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['users.User']", 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'owned_user_stories'"}),
            'pgtags': ('djorm_pgarray.fields.TextArrayField', [], {'null': 'True', 'dbtype': "'text'", 'blank': 'True', 'default': 'None'}),
            'points': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['projects.Points']", 'through': "orm['userstories.RolePoints']", 'related_name': "'userstories'", 'symmetrical': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']", 'related_name': "'user_stories'"}),
            'ref': ('django.db.models.fields.BigIntegerField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True', 'default': 'None'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.UserStoryStatus']", 'on_delete': 'models.SET_NULL', 'null': 'True', 'blank': 'True', 'related_name': "'user_stories'"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tags': ('picklefield.fields.PickledObjectField', [], {'blank': 'True'}),
            'team_requirement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'watchers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['users.User']", 'null': 'True', 'related_name': "'userstories_userstory+'", 'blank': 'True', 'symmetrical': 'False'})
        }
    }

    complete_apps = ['userstories']