from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=30)
    isbn = serializers.CharField(required=True, max_length=30)
    author = serializers.CharField(required=True, max_length=20)
    publish = serializers.CharField(required=True, max_length=30)
    rate = serializers.FloatField(default=0)


class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
