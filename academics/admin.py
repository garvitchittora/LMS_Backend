from django.contrib import admin

from academics.models import AcademicSession, Class, Examination, Score, Subject

admin.site.register(Subject)
admin.site.register(Class)


@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    """
    Encapsulate all admin options and functionality for AcademicSession model.
    """

    model = AcademicSession
    list_display = ("start", "end")


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    """
    Encapsulate all admin options and functionality for Examination model.
    """

    model = Examination
    list_display = ("title", "term", "session", "max_score")


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    """
    Encapsulate all admin options and functionality for Score model.
    """

    model = Score
    list_display = ("student", "subject", "examination", "score")
