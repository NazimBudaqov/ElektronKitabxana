# Generated by Django 4.0.4 on 2022-04-26 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ElektronKitabxana', '0004_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ElektronKitabxana.category'),
        ),
    ]