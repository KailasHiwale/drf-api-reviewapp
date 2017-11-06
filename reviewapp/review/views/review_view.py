from django.utils.six import BytesIO
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from review.models.review_model import Review
from review.serializers.review_serializer import ReviewSerializer


class ReviewViewset(generics.ListAPIView):
    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        json = JSONRenderer().render(request.data)
        stream = BytesIO(json)
        data = JSONParser().parse(stream)
        serializer = ReviewSerializer(data=data)

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
        serializer = ReviewSerializer(data=[data], many=True)

        try:
            review = Review.objects.get(id=pk)
            serializer = ReviewSerializer(review, data=data)

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
            review = Review.objects.get(id=pk)
            serializer = ReviewSerializer(review)
            serializer.delete(review)
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception:
            return Response("ID not found", status=status.HTTP_404_NOT_FOUND)
