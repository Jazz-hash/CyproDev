# Generated by Django 3.0.7 on 2020-09-19 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_portfolio_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='filter',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]