# Generated by Django 4.0.4 on 2022-04-27 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ElektronKitabxana', '0008_alter_author_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
    ]