# Generated by Django 2.1.5 on 2019-01-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20190119_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='todo_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]