# Generated by Django 5.0.3 on 2024-03-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI_filter_API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('burner_image', models.ImageField(blank=True, null=True, upload_to='aboutpage/images')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('subtitle', models.CharField(max_length=300)),
                ('posted_by', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('burner_image', models.ImageField(blank=True, null=True, upload_to='contactpage/images')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('paragraph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HomePageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('burner_image', models.ImageField(blank=True, null=True, upload_to='homepage/images')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='User_Queries',
            new_name='UserQuery',
        ),
        migrations.DeleteModel(
            name='About_page_Content',
        ),
        migrations.DeleteModel(
            name='Blog_Posts',
        ),
        migrations.DeleteModel(
            name='Contact_Page_Content',
        ),
        migrations.DeleteModel(
            name='Home_page_Content',
        ),
    ]
