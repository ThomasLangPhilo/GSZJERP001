# Generated by Django 4.1 on 2022-11-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0025_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='adress',
            field=models.CharField(default=1, max_length=128, verbose_name='地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockbase',
            name='adress',
            field=models.CharField(default=1, max_length=128, verbose_name='仓库名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='industry',
            name='industryname',
            field=models.CharField(max_length=64, verbose_name='工厂名称'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(2, '已支付'), (1, '待支付')], default=1, verbose_name='状态'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stockbase',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stocks',
        ),
        migrations.AlterField(
            model_name='rawstock',
            name='name',
            field=models.CharField(default=None, max_length=32, verbose_name='原料'),
        ),
        migrations.AlterField(
            model_name='stockbase',
            name='stockbasename',
            field=models.CharField(max_length=64, verbose_name='仓库名称'),
        ),
        migrations.AddField(
            model_name='product',
            name='industry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app001.industry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stockbase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app001.stockbase'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stocks',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app001.rawstock'),
            preserve_default=False,
        ),
    ]