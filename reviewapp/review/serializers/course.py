from rest_framework import serializers
from review.models.course import Course


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    course_name = serializers.CharField()
    course_detail = serializers.CharField(required=False)

    class Meta:
        model = Course
        fields = ('id', 'course_name', 'course_detail')

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.course_name = validated_data.get(
            'course_name', instance.course_name)
        instance.course_detail = validated_data.get(
            'course_detail', instance.course_detail)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return True
