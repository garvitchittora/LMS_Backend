from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "last_login", "is_superuser", "is_staff", "groups", "user_permissions"
        ]
        extra_kwargs = {"password": {"write_only": True}}
    
    def validate(self, attrs: dict):
        """ 
        Check the request data for invalid values and raise `ValidationError` if found.
        """
        # validate password
        validate_password(attrs["password"])

        # The user must be of atleast one type
        if not (
            attrs.get("is_admin") 
            or attrs.get("is_teacher") 
            or attrs.get("is_accountant")
        ):
            raise serializers.ValidationError(
                detail={
                    "msg": "is_admin, is_teacher and is_accountant cannot all be false"
                },
                code=400
            )
        
        return super().validate(attrs)
    
    def create(self, validated_data: dict):
        instance = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
