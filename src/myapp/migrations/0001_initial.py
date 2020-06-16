# Generated by Django 3.0.6 on 2020-05-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masv', models.CharField(max_length=200, unique=True)),
                ('ho_ten', models.CharField(default='', max_length=200)),
                ('gioi_tinh', models.BooleanField(default=False)),
                ('ngay_sinh', models.DateField(auto_now_add=True)),
            ],
        ),
    ]