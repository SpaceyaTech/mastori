# Generated by Django 4.1.3 on 2023-04-27 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_rename_user_comment_account_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="post",
            new_name="stori",
        ),
    ]
