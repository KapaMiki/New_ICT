# Generated by Django 2.2.10 on 2020-05-02 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_remove_group_student'),
        ('Users', '0003_profile_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='education.Group', verbose_name='Группа'),
        ),
    ]
