# Generated by Django 4.1.1 on 2022-09-29 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("students", "0002_student_class_section_alter_student_guardians"),
        ("academics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AcademicSession",
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
                ("start", models.DateField(verbose_name="start date")),
                ("end", models.DateField(verbose_name="end date")),
            ],
        ),
        migrations.CreateModel(
            name="Examination",
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
                ("term", models.CharField(max_length=1, verbose_name="term")),
                ("title", models.CharField(max_length=10, verbose_name="title")),
                (
                    "max_score",
                    models.PositiveSmallIntegerField(verbose_name="maximum score"),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="academics.academicsession",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Score",
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
                    "score",
                    models.PositiveSmallIntegerField(default=0, verbose_name="score"),
                ),
                (
                    "examination",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="academics.examination",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="academics.subject",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="score",
            constraint=models.UniqueConstraint(
                fields=("examination", "student", "subject"), name="student_score"
            ),
        ),
        migrations.AddConstraint(
            model_name="examination",
            constraint=models.UniqueConstraint(
                fields=("term", "title", "session"), name="exam_unique"
            ),
        ),
    ]
