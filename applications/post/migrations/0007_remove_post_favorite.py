# Generated by Django 4.1.6 on 2023-02-16 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorite',
        ),
    ]
