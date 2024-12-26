from rest_framework import serializers
from .models import Card

class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'description', 'image', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'image': {'required': False}
        }