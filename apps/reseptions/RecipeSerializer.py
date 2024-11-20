from rest_framework import serializers
from.models import Recipe

class ReseptiEdi(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'