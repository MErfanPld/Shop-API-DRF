# Generated by Django 4.1.2 on 2022-10-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
    ]
