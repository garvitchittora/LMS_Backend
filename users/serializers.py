from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "last_login",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs: dict):
        """
        Check the request data for invalid values and raise `ValidationError` if found.
        """
        # validate password
        if "password" in attrs:
            validate_password(attrs["password"])

        # all user types must not be false
        if (
            not attrs.get(
                "is_admin", self.instance.is_admin if self.instance else False
            )
            and not attrs.get(
                "is_teacher", self.instance.is_teacher if self.instance else False
            )
            and not attrs.get(
                "is_accountant", self.instance.is_accountant if self.instance else False
            )
        ):
            raise serializers.ValidationError(
                detail={"msg": "At least one user type must be true"}, code=400
            )

        return super().validate(attrs)

    def create(self, validated_data: dict):
        instance = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
