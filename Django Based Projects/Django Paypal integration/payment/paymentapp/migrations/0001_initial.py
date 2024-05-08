# Generated by Django 5.0.4 on 2024-04-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.URLField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('product_description', models.TextField()),
            ],
        ),
    ]
