# Generated by Django 5.0.1 on 2024-06-02 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
