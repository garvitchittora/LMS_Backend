from django.contrib.auth import get_user_model
from django_filters import FilterSet

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


class CommonFilter(FilterSet):
    class Meta:
        abstract = True
        fields = {
            "name": ["iexact", "icontains"],
            "email": ["iexact", "icontains"],
            "gender": ["exact", "iexact"],
            "phone_number": ["exact", "contains"],
            "address": ["iexact", "icontains"],
            "city": ["iexact", "icontains"],
            "nationality": ["iexact", "icontains"],
            "social_category": ["iexact"],
            "designation": ["iexact", "icontains"],
            "annual_income": ["exact", "gt", "gte", "lt", "lte"]
        }


class UserFilter(CommonFilter):
    class Meta(CommonFilter.Meta):
        model = User
        CommonFilter.Meta.fields.update(
            {
                "is_admin": ["exact"],
                "is_teacher": ["exact"],
                "is_accountant": ["exact"]
            }
        )
