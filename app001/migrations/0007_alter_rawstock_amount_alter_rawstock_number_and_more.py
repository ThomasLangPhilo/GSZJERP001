# Generated by Django 4.1 on 2022-10-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0006_alter_rawstock_name_alter_rawstock_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawstock',
            name='amount',
            field=models.SmallIntegerField(default=None, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='rawstock',
            name='number',
            field=models.SmallIntegerField(default=None, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='rawstock',
            name='price',
            field=models.SmallIntegerField(default=None, verbose_name='单价'),
        ),
    ]