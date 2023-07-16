# Generated by Django 4.2.3 on 2023-07-16 19:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("challenge", "0012_answer_confirmation"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="image"
            ),
        ),
    ]