# Generated by Django 2.1.2 on 2019-04-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='information',
            field=models.TextField(blank=True),
        ),
    ]
