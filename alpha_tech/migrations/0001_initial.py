# Generated by Django 3.0 on 2019-12-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('quotes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('year_exp', models.IntegerField(default=0)),
                ('quotes', models.CharField(max_length=200)),
            ],
        ),
    ]
