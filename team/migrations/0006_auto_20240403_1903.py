# Generated by Django 3.2.4 on 2024-04-03 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20240403_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default=0, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='intro',
            field=models.TextField(max_length=200, verbose_name='Introduction'),
        ),
    ]