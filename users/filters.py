from django.contrib.auth import get_user_model
from django.db import models
from django_filters import CharFilter, NumberFilter
from django_filters.rest_framework import FilterSet

User = get_user_model()


SEARCH_FIELDS = [
    "name",
    "email",
    "gender",
    "phone_number",
    "address",
    "city",
    "nationality",
    "social_category",
    "designation",
]


class AbstractFilter(FilterSet):
    class Meta:
        filter_overrides = {
            models.CharField: {
                "filter_class": CharFilter,
                "extra": lambda f: {"lookup_expr": "icontains"},
            },
            models.TextField: {
                "filter_class": CharFilter,
                "extra": lambda f: {"lookup_expr": "icontains"},
            },
            models.EmailField: {
                "filter_class": CharFilter,
                "extra": lambda f: {"lookup_expr": "icontains"},
            },
            models.PositiveIntegerField: {
                "filter_class": NumberFilter,
                "extra": lambda f: {"lookup_expr": "gte"},
            },
        }


class PersonFilter(AbstractFilter):
    class Meta(AbstractFilter.Meta):
        fields = [
            "name",
            "email",
            "gender",
            "phone_number",
            "address",
            "city",
            "nationality",
            "social_category",
            "designation",
            "annual_income",
        ]


class UserFilter(PersonFilter):
    class Meta(PersonFilter.Meta):
        model = User
        PersonFilter.Meta.fields.extend(["is_admin", "is_teacher", "is_accountant"])
