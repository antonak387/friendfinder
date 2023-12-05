# Generated by Django 4.2.4 on 2023-12-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_customuser_profile_picture_customuser_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likes',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фотография профиля'),
        ),
    ]
