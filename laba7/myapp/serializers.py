# myapp/serializers.py
from rest_framework import serializers
from .models import Token, Good


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['value']


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'name', 'amount', 'price']
