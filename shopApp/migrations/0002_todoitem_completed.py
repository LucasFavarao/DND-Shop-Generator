# Generated by Django 4.2.13 on 2024-07-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
