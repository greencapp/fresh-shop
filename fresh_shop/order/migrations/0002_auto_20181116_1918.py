# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('WAIT_BUYER_PAY', '交易创建'), ('paying', '待支付'), ('TRADE_CLOSE', '交易关闭'), ('TRADE_FINISHED', '交易结束'), ('TRADE_SUCCESS', '成功')], default='paying', max_length=20, verbose_name='交易状态'),
        ),
    ]
