# Generated by Django 4.1.3 on 2023-02-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="verification_code",
            field=models.CharField(default="550965", max_length=6, unique=True),
        ),
    ]
