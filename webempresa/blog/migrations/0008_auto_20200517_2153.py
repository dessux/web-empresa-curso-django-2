# Generated by Django 3.0.6 on 2020-05-17 21:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200517_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
        ),
    ]
