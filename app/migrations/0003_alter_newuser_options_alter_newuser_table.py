# Generated by Django 5.0.3 on 2024-05-14 10:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_newuser_options_alter_newuser_managers_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newuser",
            options={},
        ),
        migrations.AlterModelTable(
            name="newuser",
            table="new_user",
        ),
    ]
