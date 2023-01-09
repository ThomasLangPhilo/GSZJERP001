# Generated by Django 4.1 on 2022-10-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0023_alter_product_industry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stockbase',
            field=models.ManyToManyField(related_query_name='stbas', to='app001.stockbase'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stocks',
            field=models.ManyToManyField(related_query_name='sto', to='app001.rawstock'),
        ),
    ]