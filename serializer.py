from rest_framework import serializers
from .models import Book, Author


class BookNamesSerializer(serializers.Serializer):

    book_id = serializers.IntegerField()
    book_name = serializers.CharField(max_length=120)

    def to_representation(self, instance: Book):
        return {
            "book_id": instance.id,
            "book_name": instance.name,
        }

    def validate_book_name(self, value):
        if value == ' ':
            raise serializers.ValidationError('Invalid value')
        return value


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']

    def validate_first_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("First name size should be more than 3 characters")
        return value
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ["id", "name", "price", "available_amount", "author"]
