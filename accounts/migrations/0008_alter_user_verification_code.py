# Generated by Django 4.1.3 on 2023-03-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_alter_user_verification_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="verification_code",
            field=models.CharField(default="638847", max_length=6, unique=True),
        ),
    ]
