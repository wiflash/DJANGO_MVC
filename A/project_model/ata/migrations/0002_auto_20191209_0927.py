# Generated by Django 3.0 on 2019-12-09 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livecode',
            name='tanggal_pelaksanaan',
            field=models.DateField(verbose_name='Tanggal Pelaksanaan'),
        ),
    ]
