# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-31 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0019_sales_areano_sales_custno_sales_harborid_sales_noid_sales_orderno_sales_refid_sales_siteno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sr_rollno',
            name='testItem',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sr_samplingid',
            name='errMsg',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]