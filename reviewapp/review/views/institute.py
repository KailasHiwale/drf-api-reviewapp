from django.utils.six import BytesIO
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from review.models.institute import Institute
from review.serializers.institute import InstituteSerializer


class InstituteViewset(generics.ListAPIView):
    def get(self, request):
        institute = Institute.objects.all()
        serializer = InstituteSerializer(institute, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        json = JSONRenderer().render(request.data)
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        serializer = InstituteSerializer(data=data)

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
        serializer = InstituteSerializer(data=[data], many=True)

        try:
            review = Review.objects.get(id=pk)
            serializer = InstituteSerializer(review, data=data)

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
            institute = Institute.objects.get(id=pk)
            serializer = InstituteSerializer(institute)
            serializer.delete(institute)
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception:
            return Response("ID not found", status=status.HTTP_404_NOT_FOUND)
