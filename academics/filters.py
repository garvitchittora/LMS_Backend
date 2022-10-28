from users.filters import AbstractFilter

from academics.models import Examination, Score, Subject


class SubjectFilter(AbstractFilter):
    class Meta(AbstractFilter.Meta):
        model = Subject
        fields = ["title", "description", "students__name", "teachers__name"]


class ExamFilter(AbstractFilter):
    class Meta(AbstractFilter.Meta):
        model = Examination
        fields = ["term", "title", "max_score", "session"]


class ScoreFilter(AbstractFilter):
    class Meta(AbstractFilter.Meta):
        model = Score
        fields = [
            "score",
            "examination",
            "student",
            "student__name",
            "teacher",
            "teacher__name",
            "subject",
            "subject__title",
        ]
