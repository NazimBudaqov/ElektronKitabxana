# Generated by Django 4.0.4 on 2022-04-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElektronKitabxana', '0009_remove_author_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
    ]
