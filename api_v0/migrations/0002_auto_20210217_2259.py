# Generated by Django 3.0.5 on 2021-02-17 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_admin',
        ),
    ]