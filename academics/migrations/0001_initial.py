# Generated by Django 4.1.1 on 2022-09-29 11:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
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
                    "classname",
                    models.CharField(max_length=10, verbose_name="class name"),
                ),
                ("section", models.CharField(max_length=10, verbose_name="section")),
            ],
            options={
                "verbose_name_plural": "classes",
            },
        ),
        migrations.CreateModel(
            name="Subject",
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
                    "title",
                    models.CharField(max_length=100, unique=True, verbose_name="title"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "students",
                    models.ManyToManyField(
                        related_name="subjects", to="students.student"
                    ),
                ),
                (
                    "teachers",
                    models.ManyToManyField(
                        related_name="subjects", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="class",
            constraint=models.UniqueConstraint(
                fields=("classname", "section"), name="class_unique_constraint"
            ),
        ),
    ]
