# Generated by Django 4.1 on 2022-10-24 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawstock',
            name='admin',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='app001.admin', verbose_name='管理员'),
            preserve_default=False,
        ),
    ]