# Generated by Django 3.0.5 on 2021-02-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0005_auto_20210224_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Moderator'), ('3', 'User')], default='1', max_length=50),
        ),
    ]
