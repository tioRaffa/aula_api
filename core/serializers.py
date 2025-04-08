from rest_framework import serializers
from .models import Course, Evaluation

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = [
            'id',
            'name',
            'course',
            'email',
            'comment',
            'evaluation',
            'created_at',
            'active',
        ]
        
        extra_kwargs = {
            'email': {'write_only': True}
        }
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'url',
            'created_at',
            'active',
        ]