# Generated by Django 4.2.7 on 2023-12-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-03-13'),
            preserve_default=False,
        ),
    ]