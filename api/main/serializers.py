from rest_framework import serializers
from .models import People, Car

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'