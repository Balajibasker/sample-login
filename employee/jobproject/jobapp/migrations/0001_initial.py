# Generated by Django 4.1.4 on 2022-12-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="login_data",
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
                ("username", models.CharField(default="", max_length=20)),
                ("password", models.CharField(default="", max_length=20)),
                ("email", models.CharField(default="", max_length=20)),
            ],
        ),
    ]
