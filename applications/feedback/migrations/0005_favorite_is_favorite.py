# Generated by Django 4.1.6 on 2023-02-16 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_remove_favorite_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]