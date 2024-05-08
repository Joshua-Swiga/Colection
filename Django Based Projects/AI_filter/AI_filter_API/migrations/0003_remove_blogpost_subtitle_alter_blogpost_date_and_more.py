# Generated by Django 5.0.3 on 2024-04-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI_filter_API', '0002_aboutpagecontent_blogpost_contactpagecontent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='subtitle',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='posted_by',
            field=models.CharField(default='Well Edited!', max_length=100),
        ),
    ]