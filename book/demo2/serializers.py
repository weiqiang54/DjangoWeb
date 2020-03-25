from rest_framework import serializers

from .models import Types


class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = '__all__'

