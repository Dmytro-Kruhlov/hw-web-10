# Generated by Django 4.2.6 on 2023-10-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0002_alter_author_born_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
