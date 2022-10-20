from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _
from students.models import Student

User = get_user_model()


class Subject(models.Model):
    """
    Contains information of a subject such as title, description, etc.
    """

    title = models.CharField(_("title"), max_length=100, unique=True)
    description = models.TextField(_("description"), blank=True)
    teachers = models.ManyToManyField(User, related_name="subjects")
    students = models.ManyToManyField(Student, related_name="subjects")

    def __str__(self) -> str:
        return self.title


class Class(models.Model):
    """
    Contains information of a class. A unique class is identified by a
    number from 1-12 (or LKG, UKG, Nursery, etc.) and a section (A, B, C, etc.)
    """

    classname = models.CharField(_("class name"), max_length=10)
    section = models.CharField(_("section"), max_length=10)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["classname", "section"], name="class_unique_constraint"
            )
        ]
        verbose_name_plural = "classes"

    def __str__(self) -> str:
        return f"{self.classname} {self.section}"


class AcademicSession(models.Model):
    """
    Contains start and end date of an academic session.
    """

    start = models.DateField(_("start date"))
    end = models.DateField(_("end date"))

    def __str__(self) -> str:
        return f"{self.start.year}-{self.end.year}"


class Examination(models.Model):
    """
    Contains session (eg: 2021-22), term (eg: 1, 2) and exam name (eg: PT-1, HY).
    """

    term = models.CharField(_("term"), max_length=1)
    title = models.CharField(_("title"), max_length=10)
    max_score = models.PositiveSmallIntegerField(_("maximum score"))
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["term", "title", "session"], name="exam_unique")
        ]

    def __str__(self) -> str:
        return f"{self.term} {self.title} {self.session}"


class Score(models.Model):
    """
    Contains the score of a student in an examination.
    """

    score = models.PositiveSmallIntegerField(_("score"), default=0)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["examination", "student", "subject"], name="student_score"
            )
        ]

    def __str__(self) -> str:
        return f"{self.student} {self.subject} {self.examination}"
