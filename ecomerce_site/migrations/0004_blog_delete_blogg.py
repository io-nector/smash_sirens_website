# Generated by Django 5.0.2 on 2024-02-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce_site', '0003_blogg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image_2', models.ImageField(blank=True, upload_to='blog')),
            ],
        ),
        migrations.DeleteModel(
            name='Blogg',
        ),
    ]
