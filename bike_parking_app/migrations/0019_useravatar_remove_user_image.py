# Generated by Django 4.2.2 on 2024-05-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike_parking_app', '0018_user_achievements_delete_userachievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAvatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.ImageField(upload_to='user_avatars/')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
