# Generated by Django 4.1.6 on 2023-02-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200),
        ),
    ]
