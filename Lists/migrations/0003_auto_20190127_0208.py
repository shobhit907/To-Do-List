# Generated by Django 2.1.5 on 2019-01-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lists', '0002_lists_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lists',
            name='slug',
            field=models.SlugField(),
        ),
    ]
