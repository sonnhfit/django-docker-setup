# Generated by Django 3.0.6 on 2020-05-26 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_monhoc'),
    ]

    operations = [
        migrations.AddField(
            model_name='monhoc',
            name='year',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sinhvien',
            name='ngay_sinh',
            field=models.DateField(blank=True, null=True),
        ),
    ]
