# Generated by Django 4.2.2 on 2024-03-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_parking_app', '0005_alter_bikerackdata_date_inst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikerackdata',
            name='Date_Inst',
            field=models.DateField(),
        ),
    ]
