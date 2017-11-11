from django.utils.six import BytesIO
from rest_framework.                                                                                                                                                                                                                                            
from rest_framework import generics
from rest_framework.response import Response
# from django.http import HttpResponse

from review.models.course import Course
from review.serializers.course import CourseSerializer


class CourseViewset(generics.ListAPIView):

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        json

    def put(self, request, pk, *args, **kwargs):
        pass

    def delete(self, request, pk):
        pass
