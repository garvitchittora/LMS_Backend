from rest_framework import serializers

from academics.models import AcademicSession, Class, Examination, Score


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"
