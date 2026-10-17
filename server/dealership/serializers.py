from rest_framework import serializers
from .models import CarMake, CarModel, Dealer, Review
from django.contrib.auth.models import User

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
