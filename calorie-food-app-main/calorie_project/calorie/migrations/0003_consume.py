# Generated by Django 4.2 on 2023-04-16 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("calorie", "0002_rename_carbohydrates_food_fats"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consume",
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
                (
                    "food_consumed",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="calorie.food"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
