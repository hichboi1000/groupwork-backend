from rest_framework import serializers
from .models import Unit, Assignment, GroupAssignment, Submission


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class GroupAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAssignment
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'