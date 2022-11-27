from students.models import Guardian, Student
from users.filters import AbstractFilter


class StudentFilter(AbstractFilter):
    class Meta(AbstractFilter.Meta):
        model = Student
        fields = [
            "enrollment_id",
            "name",
            "email",
            "class_section",
            "class_section__classname",
            "class_section__section",
        ]


class GuardianFilter(AbstractFilter):
    class Meta(AbstractFilter.Meta):
        model = Guardian
        fields = ["name", "email", "wards__name", "wards__enrollment_id"]
