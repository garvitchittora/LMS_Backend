# Generated by Django 4.1.1 on 2022-11-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0003_remove_student_class_roll_id_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="age",
        ),
        migrations.AddField(
            model_name="student",
            name="dob",
            field=models.DateField(blank=True, null=True, verbose_name="date of birth"),
        ),
    ]
