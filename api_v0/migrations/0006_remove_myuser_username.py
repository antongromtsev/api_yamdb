# Generated by Django 3.0.5 on 2021-02-20 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0005_auto_20210219_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
    ]
