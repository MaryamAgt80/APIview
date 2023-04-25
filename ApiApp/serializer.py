from rest_framework import serializers
from .models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# class serializerBook(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(max_length=100)
#     store_name = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=100)
#     fav = serializers.BooleanField(default=False)
#     image = serializers.ImageField(use_url=True, default='')
