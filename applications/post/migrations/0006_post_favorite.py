# Generated by Django 4.1.6 on 2023-02-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
