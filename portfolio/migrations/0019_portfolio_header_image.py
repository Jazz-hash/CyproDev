# Generated by Django 3.0.7 on 2020-09-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20200217_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='portfolio-images'),
        ),
    ]