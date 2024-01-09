# backend/serializers.py
from rest_framework import serializers
from .models import User, ClothingItem, TryOnResult

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClothingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingItem
        fields = '__all__'

class TryOnResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryOnResult
        fields = '__all__'
