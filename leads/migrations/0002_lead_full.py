# Generated by Django 3.2.8 on 2021-11-07 03:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='full',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
