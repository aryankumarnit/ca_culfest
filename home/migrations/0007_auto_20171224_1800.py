# Generated by Django 2.0 on 2017-12-24 18:00

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=home.models.user_directory_path),
        ),
    ]
