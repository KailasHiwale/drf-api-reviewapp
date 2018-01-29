"""
Use unicode_literals when back-porting new or existing Python 3 code
to Python 2/3 than when porting existing Python 2 code to 2/3
"""
from __future__ import unicode_literals

from review.models.institute import Institute


class InstituteSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    institute_name = serializers.CharField()
    address = serializers.CharField()
    pin_code = serializers.IntegerField(required=False)
    office_mail = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)
    website = serializers.URLField(required=False)
    institute_type = serializers.CharField(required=False)
    founded_in = serializers.IntegerField(required=False)
    affiliated_to = serializers.CharField(required=False)
    approved_by = serializers.CharField(required=False)

    class Meta:
        model = Institute
        fields = (
            'id',
            'institute_name',
            'address',
            'pin_code',
            'office_mail',
            'phone_number',
            'website',
            'institute_type',
            'founded_in',
            'affiliated_to',
            'approved_by')

    def create(self, validated_data):
        return Institute.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.institute_name = validated_data.get(
            'institute_name', instance.institute_name)
        instance.address = validated_data.get(
            'address', instance.address)
        instance.pin_code = validated_data.get(
            'pin_code', instance.pin_code)
        instance.office_mail = validated_data.get(
            'office_mail', instance.office_mail)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.website = validated_data.get('website', instance.website)
        instance.institute_type = validated_data.get(
            'institute_type', instance.institute_type)
        instance.founded_in = validated_data.get(
            'founded_in', instance.founded_in)
        instance.affiliated_to = validated_data.get(
            'affiliated_to', instance.affiliated_to)
        instance.approved_by = validated_data.get(
            'approved_by', instance.approved_by)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return True

