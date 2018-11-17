# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='商品唯一货号')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('sold_nums', models.IntegerField(default=0, verbose_name='销售量')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('goods_nums', models.IntegerField(default=0, verbose_name='商品库存')),
                ('market_price', models.FloatField(default=0, verbose_name='市场价格')),
                ('shop_price', models.FloatField(default=0, verbose_name='本店价格')),
                ('goods_brief', models.CharField(max_length=500, verbose_name='商品简短描述')),
                ('goods_desc', models.TextField(null=True)),
                ('ship_free', models.BooleanField(default=True, verbose_name='是否承担运费')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图')),
                ('is_new', models.BooleanField(default=False, verbose_name='是否新品')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热销')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
            ],
            options={
                'db_table': 'f_goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.IntegerField(choices=[(1, '新鲜水果'), (2, '海鲜水产'), (3, '猪牛羊肉'), (4, '禽类蛋品'), (5, '新鲜蔬菜'), (6, '速冻食品')], verbose_name='类目级别')),
                ('category_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图')),
            ],
            options={
                'db_table': 'f_goods_category',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]
