# Generated by Django 2.1.5 on 2021-08-05 21:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddance', '0006_auto_20210805_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]