# Generated by Django 2.1.5 on 2019-03-27 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lists', '0009_auto_20190328_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lists',
            name='slug',
            field=models.SlugField(default='a'),
        ),
    ]