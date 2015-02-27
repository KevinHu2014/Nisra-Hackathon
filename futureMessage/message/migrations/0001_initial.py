# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageID', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField(blank=True)),
                ('endTime', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.ForeignKey(to='message.Message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(serialize=False, primary_key=True)),
                ('userEmail', models.CharField(unique=True, max_length=30)),
                ('userPassword', models.CharField(max_length=30)),
                ('inVaild', models.BooleanField(default=False)),
                ('checkCode', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='send',
            name='uid',
            field=models.ForeignKey(to='message.User'),
            preserve_default=True,
        ),
    ]
