from rest_framework import serializers
from review.models.review_model import Review
from review.models.institute import Institute
from reviewer.models import Reviewer


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    institute = serializers.PrimaryKeyRelatedField(
        queryset=Institute.objects.all())
    reviewer = serializers.PrimaryKeyRelatedField(
        queryset=Reviewer.objects.all())
    overall_rating = serializers.IntegerField(required=False)
    review_title = serializers.CharField(required=False)
    merits = serializers.CharField(required=False)
    demerits = serializers.CharField(required=False)
    advice = serializers.CharField(required=False)

    class Meta:
        model = Review
        fields = (
            'id',
            'institute',
            'reviewer',
            'overall_rating',
            'review_title',
            'merits',
            'demerits',
            'advice')

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.institute = validated_data.get(
            'institute', instance.institute)
        instance.reviewer = validated_data.get(
            'reviewer', instance.reviewer)
        instance.overall_rating = validated_data.get(
            'overall_rating', instance.overall_rating)
        instance.review_title = validated_data.get(
            'review_title', instance.review_title)
        instance.merits = validated_data.get('merits', instance.merits)
        instance.demerits = validated_data.get('demerits', instance.demerits)
        instance.advice = validated_data.get('advice', instance.advice)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return True
