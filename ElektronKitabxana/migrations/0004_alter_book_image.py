# Generated by Django 4.0.4 on 2022-04-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElektronKitabxana', '0003_category_slug_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='books'),
        ),
    ]