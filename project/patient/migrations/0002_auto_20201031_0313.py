# Generated by Django 3.1 on 2020-10-31 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
