# Generated by Django 2.1.2 on 2019-04-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_auto_20190408_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_1',
            field=models.ImageField(blank=True, upload_to='posts_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_2',
            field=models.ImageField(blank=True, upload_to='posts_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_3',
            field=models.ImageField(blank=True, upload_to='posts_images'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_4',
            field=models.ImageField(blank=True, upload_to='posts_images'),
        ),
    ]
