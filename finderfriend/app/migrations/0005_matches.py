# Generated by Django 4.2.4 on 2023-12-05 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_likes_options_alter_customuser_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('json_dialog', models.JSONField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
