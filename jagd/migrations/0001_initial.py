# Generated by Django 4.2.6 on 2023-10-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("user_name", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("woman", "Woman"), ("man", "Man")],
                        default="man",
                        max_length=10,
                    ),
                ),
                ("professional", models.BooleanField(default=False)),
            ],
        ),
    ]
