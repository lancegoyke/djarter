# Generated by Django 4.2.6 on 2023-11-01 12:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_customuser_username_alter_customuser_email"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[],
        ),
    ]
