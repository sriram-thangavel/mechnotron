# Generated by Django 4.1.6 on 2023-02-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_event_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='banner'),
        ),
    ]