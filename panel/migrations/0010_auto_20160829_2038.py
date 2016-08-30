# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_auto_20160827_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='signal',
            name='trigger_value',
            field=models.DecimalField(decimal_places=3, max_digits=12, null=True, verbose_name='信号值'),
        ),
        migrations.AlterField(
            model_name='param',
            name='float_value',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='浮点值'),
        ),
        migrations.AlterField(
            model_name='param',
            name='int_value',
            field=models.IntegerField(blank=True, null=True, verbose_name='整数值'),
        ),
        migrations.AlterField(
            model_name='param',
            name='str_value',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='字符串值'),
        ),
        migrations.AlterField(
            model_name='param',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='priority',
            field=models.IntegerField(choices=[(0, '低'), (1, '普通'), (2, '高')], default=1, verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='type',
            field=models.CharField(choices=[('换月移仓', '换月移仓'), ('买开', '买开'), ('卖开', '卖开'), ('卖平', '卖平'), ('买平', '买平')], max_length=16, verbose_name='信号类型'),
        ),
    ]
