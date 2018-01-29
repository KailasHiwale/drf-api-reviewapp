from django.utils.six import BytesIO
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from review.models.institute_course import InstituteCourse
from review.serializers.institute_course import InstituteCourseSerializer


class InstituteCourseViewset(generics.ListAPIView):
    def get(self, request):
        institute_course = InstituteCourse.objects.all()
        serializer = InstituteCourseSerializer(institute_course, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        json = JSONRenderer().render(request.data)
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        serializer = InstituteCourseSerializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        json = JSONRenderer().render(request.data)
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        serializer = InstituteCourseSerializer(data=[data], many=True)

        try:
            review = Review.objects.get(id=pk)
            serializer = InstituteCourseSerializer(review, data=data)

            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_202_ACCEPTED)

            except Exception:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response("ID not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            institute_course = InstituteCourse.objects.get(id=pk)
            serializer = InstituteCourseSerializer(institute_course)
            serializer.delete(institute_course)
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception:
            return Response("ID not found", status=status.HTTP_404_NOT_FOUND)
