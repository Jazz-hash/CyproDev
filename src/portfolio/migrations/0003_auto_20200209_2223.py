# Generated by Django 3.0.1 on 2020-02-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_hosted_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='hosted_link',
            field=models.URLField(blank=True),
        ),
    ]
