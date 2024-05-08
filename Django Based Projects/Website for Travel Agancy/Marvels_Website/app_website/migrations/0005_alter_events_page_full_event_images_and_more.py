# Generated by Django 5.0.1 on 2024-03-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0004_alter_events_page_event_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events_page',
            name='full_event_images',
            field=models.ImageField(default=False, upload_to='media/images/event_images'),
        ),
        migrations.AlterField(
            model_name='events_page',
            name='thumbnail_image',
            field=models.ImageField(default=False, upload_to='media/images/event_thumbnails'),
        ),
    ]
