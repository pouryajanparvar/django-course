# Generated by Django 3.2.7 on 2021-09-19 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('A', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
