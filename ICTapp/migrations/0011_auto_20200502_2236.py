# Generated by Django 2.2.10 on 2020-05-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ICTapp', '0010_information_img_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': 'Практическое задание', 'verbose_name_plural': 'Практические задания'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name': 'Лекция', 'verbose_name_plural': 'Лекции'},
        ),
        migrations.AlterField(
            model_name='information',
            name='data',
            field=models.FileField(upload_to='practices/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='information',
            name='img_main',
            field=models.ImageField(upload_to='practice_images', verbose_name='Главная фотография'),
        ),
        migrations.AlterField(
            model_name='information',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='data',
            field=models.FileField(upload_to='lectures/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='img',
            field=models.ImageField(upload_to='Specialty_images', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
