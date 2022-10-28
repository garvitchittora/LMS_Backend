from users.filters import AbstractFilter

from academics.models import Subject


class SubjectFilter(AbstractFilter):
    class Meta(AbstractFilter.Meta):
        model = Subject
        fields = ["title", "description", "students__name", "teachers__name"]
