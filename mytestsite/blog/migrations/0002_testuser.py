# Generated by Django 4.2.14 on 2024-08-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField(max_length=50)),
                ("user_pw", models.CharField(max_length=50)),
                ("user_name", models.CharField(max_length=50)),
            ],
        ),
    ]
