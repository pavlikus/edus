from rest_framework import serializers

from .models import Course, CourseStream


class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
