# Generated by Django 4.1.4 on 2023-01-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0032_rename_note_lykjsys_note_l'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lykjsys',
            name='note_L',
            field=models.CharField(max_length=64, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='lykjsys',
            name='number_L',
            field=models.CharField(max_length=64, null=True, verbose_name='编号'),
        ),
    ]
