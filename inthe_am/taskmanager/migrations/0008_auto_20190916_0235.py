# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0007_auto_20181216_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='category',
            field=models.CharField(max_length=10, choices=[('error', 'Error'), ('notice', 'Info'), ('warning', 'Warning')]),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='duration',
            field=models.PositiveIntegerField(default=300, help_text='In seconds'),
        ),
        migrations.AlterField(
            model_name='taskstore',
            name='sms_replies',
            field=models.PositiveIntegerField(default=9, choices=[(9, 'Reply to all messages'), (5, 'Reply only to error messages'), (0, 'Do not reply to any incoming text messages')]),
        ),
        migrations.AlterField(
            model_name='taskstoreactivity',
            name='metadata_version',
            field=models.CharField(max_length=10, default='v5'),
        ),
        migrations.AlterField(
            model_name='taskstorestatistic',
            name='measure',
            field=models.CharField(max_length=50, choices=[('size', 'Repository Size')]),
        ),
        migrations.AlterField(
            model_name='taskstorestatistic',
            name='run_id',
            field=models.CharField(max_length=255, help_text='If generated by an automated process, indicates the job name used for generating this value.'),
        ),
        migrations.AlterField(
            model_name='trelloobject',
            name='type',
            field=models.CharField(max_length=10, choices=[('card', 'Card'), ('board', 'Board'), ('list', 'List')]),
        ),
        migrations.AlterField(
            model_name='usermetadata',
            name='colorscheme',
            field=models.CharField(max_length=255, default='dark-yellow-green.theme'),
        ),
    ]
