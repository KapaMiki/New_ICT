# Generated by Django 2.2.10 on 2020-05-02 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20190510_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img_1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img_3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img_4',
        ),
    ]
