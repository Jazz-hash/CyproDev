# Generated by Django 3.1.5 on 2021-01-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
