# Generated by Django 3.2.4 on 2024-04-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20240403_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='interest1',
            field=models.TextField(blank=True, max_length=24, verbose_name='Interest 1'),
        ),
        migrations.AlterField(
            model_name='member',
            name='interest2',
            field=models.TextField(blank=True, max_length=24, verbose_name='Interest 2'),
        ),
        migrations.AlterField(
            model_name='member',
            name='interest3',
            field=models.TextField(blank=True, max_length=24, verbose_name='Interest 3'),
        ),
        migrations.AlterField(
            model_name='member',
            name='intro',
            field=models.TextField(blank=True, max_length=50, verbose_name='Introduction'),
        ),
    ]
