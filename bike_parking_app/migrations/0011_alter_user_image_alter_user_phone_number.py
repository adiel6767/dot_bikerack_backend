# Generated by Django 4.2.2 on 2024-03-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_parking_app', '0010_bikerackdata_notes_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
