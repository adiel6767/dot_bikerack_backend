# Generated by Django 5.0.6 on 2024-12-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_parking_app', '0005_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]