# Generated by Django 4.1.1 on 2022-09-27 18:41

from django.db import migrations, models
import students.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Guardian",
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
                    "name",
                    models.CharField(blank=True, max_length=300, verbose_name="name"),
                ),
                (
                    "relation",
                    models.CharField(
                        choices=[
                            ("FATHER", "Father"),
                            ("MOTHER", "Mother"),
                            ("RELATIVE", "Relative"),
                            ("NON RELATED", "Non Related"),
                        ],
                        default="RELATIVE",
                        max_length=20,
                        verbose_name="relation",
                    ),
                ),
                (
                    "age",
                    models.PositiveSmallIntegerField(default=0, verbose_name="age"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHER", "Other"),
                        ],
                        default="MALE",
                        max_length=15,
                        verbose_name="gender",
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="occupation"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="email"),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=16, verbose_name="phone number"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="address"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=100, verbose_name="city"),
                ),
                (
                    "nationality",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="nationality"
                    ),
                ),
                (
                    "annual_income",
                    models.PositiveIntegerField(
                        default=0, verbose_name="annual income"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default.png",
                        upload_to=students.utils.guardian_image_path,
                        verbose_name="image",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                    "enrollment_id",
                    models.PositiveBigIntegerField(
                        unique=True, verbose_name="enrollment number"
                    ),
                ),
                (
                    "class_roll_id",
                    models.PositiveIntegerField(verbose_name="class roll number"),
                ),
                ("name", models.CharField(max_length=300, verbose_name="name")),
                (
                    "age",
                    models.PositiveSmallIntegerField(default=0, verbose_name="age"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("MALE", "Male"),
                            ("FEMALE", "Female"),
                            ("OTHER", "Other"),
                        ],
                        default="MALE",
                        max_length=15,
                        verbose_name="gender",
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="email"),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=16, verbose_name="phone number"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="address"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=100, verbose_name="city"),
                ),
                (
                    "nationality",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="nationality"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="default.png",
                        upload_to=students.utils.student_image_path,
                        verbose_name="image",
                    ),
                ),
                (
                    "guardians",
                    models.ManyToManyField(
                        related_name="wards", to="students.guardian"
                    ),
                ),
            ],
        ),
    ]
