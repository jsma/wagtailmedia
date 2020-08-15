# Generated by Django 2.2.8 on 2020-08-14 16:52

from django.core.validators import MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0004_auto_20200814_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='duration',
            field=models.FloatField(default=0, help_text='Duration in seconds', validators=[MinValueValidator(0)], verbose_name='duration'),
        ),
    ]
