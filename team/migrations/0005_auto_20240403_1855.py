# Generated by Django 3.2.4 on 2024-04-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20240403_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='interest1',
        ),
        migrations.RemoveField(
            model_name='member',
            name='interest2',
        ),
        migrations.RemoveField(
            model_name='member',
            name='interest3',
        ),
        migrations.AddField(
            model_name='member',
            name='interests',
            field=models.TextField(default=1, max_length=80, verbose_name='Interests'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(default=1, max_length=30, verbose_name='Position'),
            preserve_default=False,
        ),
    ]
