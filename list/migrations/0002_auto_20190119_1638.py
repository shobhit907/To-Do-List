# Generated by Django 2.1.5 on 2019-01-19 11:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='List',
        ),
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.ForeignKey(default=None, on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]