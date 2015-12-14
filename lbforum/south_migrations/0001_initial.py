# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Config'
        db.create_table(u'lbforum_config', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'lbforum', ['Config'])

        # Adding model 'Category'
        db.create_table(u'lbforum_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'lbforum', ['Category'])

        # Adding model 'Forum'
        db.create_table(u'lbforum_forum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=110)),
            ('description', self.gf('django.db.models.fields.TextField')(default='')),
            ('ordering', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lbforum.Category'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('num_topics', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num_posts', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('last_post', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'lbforum', ['Forum'])

        # Adding model 'TopicType'
        db.create_table(u'lbforum_topictype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lbforum.Forum'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'lbforum', ['TopicType'])

        # Adding model 'Topic'
        db.create_table(u'lbforum_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lbforum.Forum'])),
            ('topic_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lbforum.TopicType'], null=True, blank=True)),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='topics_', null=True, to=orm['lbforum.Post'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=999)),
            ('num_views', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num_replies', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_reply_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_post', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('has_imgs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_attachments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_replay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('need_reply_attachments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sticky', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('level', self.gf('django.db.models.fields.SmallIntegerField')(default=30)),
        ))
        db.send_create_signal(u'lbforum', ['Topic'])

        # Adding model 'Post'
        db.create_table(u'lbforum_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='posts', to=orm['lbforum.Topic'])),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
            ('poster_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('topic_post', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('format', self.gf('django.db.models.fields.CharField')(default='bbcode', max_length=20)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('has_imgs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_attachments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('edited_by', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'lbforum', ['Post'])

        # Adding M2M table for field attachments on 'Post'
        m2m_table_name = db.shorten_name(u'lbforum_post_attachments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'lbforum.post'], null=False)),
            ('attachment', models.ForeignKey(orm[u'attachments.attachment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'attachment_id'])

        # Adding model 'LBForumUserProfile'
        db.create_table(u'lbforum_lbforumuserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='lbforum_profile', unique=True, to=orm['core.User'])),
            ('last_activity', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('userrank', self.gf('django.db.models.fields.CharField')(default='Junior Member', max_length=30)),
            ('last_posttime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
        ))
        db.send_create_signal(u'lbforum', ['LBForumUserProfile'])


    def backwards(self, orm):
        # Deleting model 'Config'
        db.delete_table(u'lbforum_config')

        # Deleting model 'Category'
        db.delete_table(u'lbforum_category')

        # Deleting model 'Forum'
        db.delete_table(u'lbforum_forum')

        # Deleting model 'TopicType'
        db.delete_table(u'lbforum_topictype')

        # Deleting model 'Topic'
        db.delete_table(u'lbforum_topic')

        # Deleting model 'Post'
        db.delete_table(u'lbforum_post')

        # Removing M2M table for field attachments on 'Post'
        db.delete_table(db.shorten_name(u'lbforum_post_attachments'))

        # Deleting model 'LBForumUserProfile'
        db.delete_table(u'lbforum_lbforumuserprofile')


    models = {
        u'attachments.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_img': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'num_downloads': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'org_filename': ('django.db.models.fields.TextField', [], {}),
            'suffix': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']"})
        },
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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.user': {
            'Meta': {'object_name': 'User'},
            'course_provider_state': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'department_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_course_contact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_course_provider': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_course_seeker': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'profile_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skip_profile_completed_hint': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'suggested_provider': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'lbforum.category': {
            'Meta': {'ordering': "('-ordering', 'created_on')", 'object_name': 'Category'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'lbforum.config': {
            'Meta': {'object_name': 'Config'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'lbforum.forum': {
            'Meta': {'ordering': "('ordering', '-created_on')", 'object_name': 'Forum'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lbforum.Category']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_post': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num_posts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_topics': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ordering': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '110'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'lbforum.lbforumuserprofile': {
            'Meta': {'object_name': 'LBForumUserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_activity': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'last_posttime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'lbforum_profile'", 'unique': 'True', 'to': u"orm['core.User']"}),
            'userrank': ('django.db.models.fields.CharField', [], {'default': "'Junior Member'", 'max_length': '30'})
        },
        u'lbforum.post': {
            'Meta': {'ordering': "('-created_on',)", 'object_name': 'Post'},
            'attachments': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['attachments.Attachment']", 'symmetrical': 'False', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edited_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'bbcode'", 'max_length': '20'}),
            'has_attachments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_imgs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']"}),
            'poster_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['lbforum.Topic']"}),
            'topic_post': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'lbforum.topic': {
            'Meta': {'ordering': "('-last_reply_on',)", 'object_name': 'Topic'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lbforum.Forum']"}),
            'has_attachments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_imgs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_post': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_reply_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.SmallIntegerField', [], {'default': '30'}),
            'need_replay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'need_reply_attachments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'num_replies': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'num_views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'topics_'", 'null': 'True', 'to': u"orm['lbforum.Post']"}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']"}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'topic_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lbforum.TopicType']", 'null': 'True', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'lbforum.topictype': {
            'Meta': {'object_name': 'TopicType'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lbforum.Forum']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['lbforum']