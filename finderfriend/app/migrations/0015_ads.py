# Generated by Django 4.2.4 on 2024-01-07 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_message_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=255)),
            ],
        ),
    ]
