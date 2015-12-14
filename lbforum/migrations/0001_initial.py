# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'')),
                ('ordering', models.PositiveIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ('-ordering', 'created_on'),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=110)),
                ('description', models.TextField(default=b'')),
                ('ordering', models.PositiveIntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('num_topics', models.IntegerField(default=0)),
                ('num_posts', models.IntegerField(default=0)),
                ('last_post', models.CharField(max_length=255, blank=True)),
                ('category', models.ForeignKey(to='lbforum.Category')),
            ],
            options={
                'ordering': ('ordering', '-created_on'),
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Forums',
            },
        ),
        migrations.CreateModel(
            name='LBForumUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_activity', models.DateTimeField(auto_now_add=True)),
                ('userrank', models.CharField(default=b'Junior Member', max_length=30)),
                ('last_posttime', models.DateTimeField(auto_now_add=True)),
                ('signature', models.CharField(max_length=1000, blank=True)),
                ('user', models.OneToOneField(related_name='lbforum_profile', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poster_ip', models.GenericIPAddressField()),
                ('topic_post', models.BooleanField(default=False)),
                ('format', models.CharField(default=b'bbcode', max_length=20)),
                ('message', models.TextField()),
                ('has_imgs', models.BooleanField(default=False)),
                ('has_attachments', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('edited_by', models.CharField(max_length=255, blank=True)),
                ('attachments', models.ManyToManyField(to='attachments.Attachment', blank=True)),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
                'get_latest_by': ('created_on',),
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=999)),
                ('num_views', models.IntegerField(default=0)),
                ('num_replies', models.PositiveSmallIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(null=True, blank=True)),
                ('last_reply_on', models.DateTimeField(auto_now_add=True)),
                ('last_post', models.CharField(max_length=255, blank=True)),
                ('has_imgs', models.BooleanField(default=False)),
                ('has_attachments', models.BooleanField(default=False)),
                ('need_replay', models.BooleanField(default=False)),
                ('need_reply_attachments', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('sticky', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('level', models.SmallIntegerField(default=30, choices=[(30, 'Default'), (60, 'Distillate')])),
                ('forum', models.ForeignKey(verbose_name='Forum', to='lbforum.Forum')),
                ('post', models.ForeignKey(related_name='topics_', verbose_name='Post', blank=True, to='lbforum.Post', null=True)),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-last_reply_on',),
                'get_latest_by': 'created_on',
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
        migrations.CreateModel(
            name='TopicType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(default=b'', blank=True)),
                ('forum', models.ForeignKey(verbose_name='Forum', to='lbforum.Forum')),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_type',
            field=models.ForeignKey(verbose_name='Topic Type', blank=True, to='lbforum.TopicType', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(related_name='posts', verbose_name='Topic', to='lbforum.Topic'),
        ),
    ]
