from rest_framework import serializers
from books import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ("first_name", "last_name", "email", "birthday",)


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ("name", "address", "phone_number",)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ("title", "description", "isbn", "pub_date", "visibility", "author", "publisher", )


class BooksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ("id", "title", "description", "isbn", "author_name",)


class BookDetailSerializer(serializers.ModelSerializer):
    author_email = serializers.EmailField(source="author.email")
    author_birthday = serializers.DateField(source="author.birthday")
    publisher_address = serializers.CharField(source="publisher.address")
    
    class Meta:
        model = models.Book
        fields = ("title", "isbn", "author_name", "author_email", "author_birthday",
                  "pub_date", "publisher_name", "publisher_address", )
