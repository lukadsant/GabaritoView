# Generated by Django 4.0.8 on 2023-02-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultasql',
            name='curso',
            field=models.CharField(choices=[('24', 'Educação Física'), ('2', 'Enfermagem'), ('5', 'Farmácia'), ('6', 'Fisioterapia'), ('1', 'Medicina'), ('23', 'Nutrição'), ('13', 'Odontologia'), ('10', 'Psicologia')], max_length=45),
        ),
    ]
