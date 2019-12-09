# Generated by Django 3.0 on 2019-12-09 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='obat',
            old_name='nama',
            new_name='nama_obat',
        ),
        migrations.AlterField(
            model_name='resep',
            name='kumpulan_obat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Obat'),
        ),
        migrations.AlterField(
            model_name='resep',
            name='nama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Pasien'),
        ),
    ]
