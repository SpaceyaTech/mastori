# Generated by Django 4.1.2 on 2022-11-01 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_unique_id_blogpost_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-date_published', '-date_updated']},
        ),
    ]