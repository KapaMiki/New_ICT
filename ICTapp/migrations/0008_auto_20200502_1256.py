# Generated by Django 2.2.10 on 2020-05-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ICTapp', '0007_auto_20190409_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='description',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='perspectives',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='price',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='purpose',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='tasks',
        ),
        migrations.AddField(
            model_name='specialty',
            name='data',
            field=models.FileField(default=1, upload_to='lectures/'),
            preserve_default=False,
        ),
    ]
