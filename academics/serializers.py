from rest_framework import serializers

from academics.models import AcademicSession, Class, Examination, Score, Subject


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

    def get_unique_together_validators(self):
        validators = super().get_unique_together_validators()
        validators.append(
            serializers.UniqueTogetherValidator(
                queryset=self.Meta.model.objects.all(),
                fields=["classname", "section"],
                message="Class already exists",
            )
        )
        return validators


class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = "__all__"


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = "__all__"

    def get_unique_together_validators(self):
        validators = super().get_unique_together_validators()
        validators.append(
            serializers.UniqueTogetherValidator(
                queryset=self.Meta.model.objects.all(),
                fields=["term", "title", "session"],
                message="Exam already exists",
            )
        )
        return validators


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"

    def get_unique_together_validators(self):
        validators = super().get_unique_together_validators()
        validators.append(
            serializers.UniqueTogetherValidator(
                queryset=self.Meta.model.objects.all(),
                fields=["examination", "student", "subject"],
                message="Score already exists",
            )
        )
        return validators


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
