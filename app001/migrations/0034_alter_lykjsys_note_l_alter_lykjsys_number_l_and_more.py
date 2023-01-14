# Generated by Django 4.1.4 on 2023-01-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0033_alter_lykjsys_note_l_alter_lykjsys_number_l'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lykjsys',
            name='note_L',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='lykjsys',
            name='number_L',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(2, '已支付'), (1, '待支付')], default=1, verbose_name='状态'),
        ),
    ]