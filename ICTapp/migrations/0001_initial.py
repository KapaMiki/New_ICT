# Generated by Django 2.1.2 on 2019-04-03 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('img_main', models.ImageField(blank=True, upload_to='posts_images')),
                ('img_1', models.ImageField(blank=True, upload_to='event_images')),
                ('img_2', models.ImageField(blank=True, upload_to='event_images')),
                ('img_3', models.ImageField(blank=True, upload_to='event_images')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
