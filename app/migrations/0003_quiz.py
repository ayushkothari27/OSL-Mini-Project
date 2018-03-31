# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-31 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180331_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='q1', to='app.Game')),
                ('q2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='q2', to='app.Game')),
                ('q3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='q3', to='app.Game')),
                ('q4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='q4', to='app.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfile')),
            ],
        ),
    ]