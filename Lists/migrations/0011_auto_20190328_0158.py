# Generated by Django 2.1.5 on 2019-03-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lists', '0010_auto_20190328_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='lists',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]