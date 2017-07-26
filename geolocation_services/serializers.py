'''
Created on 21-06-2017

@author: atong
'''
from rest_framework import serializers
from geolocation_services.models import Location

class LocationSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    address = serializers.CharField(required=True, max_length=100)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    elevation = serializers.FloatField()
    

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.address = validated_data.get('address', instance.address)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.elevation = validated_data.get('elevation', instance.elevation)
        instance.save()
        return instance