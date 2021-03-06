# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 09:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='邮箱')),
                ('code', models.CharField(max_length=4, verbose_name='验证码')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('codeType', models.CharField(choices=[('reg', '注册'), ('reset', '忘记密码')], default='reg', max_length=6, verbose_name='类型')),
            ],
        ),
    ]
