# Generated by Django 4.1 on 2022-10-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0011_rawstock_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '待支付'), (2, '已支付')], default=1, verbose_name='状态'),
        ),
    ]
