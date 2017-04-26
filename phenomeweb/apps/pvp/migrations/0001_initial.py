# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 20:01
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(blank=True, max_length=127, null=True)),
                ('phenotypes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phenotypes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=15, null=True), blank=True, null=True, size=None)),
                ('inheritance_mode', models.CharField(choices=[(b'dominant', b'dominant'), (b'recessive', b'recessive'), (b'x-linked', b'x-linked'), (b'others', b'others'), (b'unknown', b'unknown')], max_length=31)),
                ('vcf_file', models.FileField(upload_to='pvp/%Y/%m/%d/')),
                ('status', models.CharField(default=b'Pending', max_length=31)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('disease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='queries', to='pvp.Disease')),
            ],
        ),
    ]
