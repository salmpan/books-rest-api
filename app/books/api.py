from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from books import models, serializers


class BooksListAPI(generics.ListAPIView):
    serializer_class = serializers.BooksListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = models.Book.objects.filter(visibility=True)\
            .exclude(publisher__isnull=True).order_by("-id").order_by("author__last_name")
        return queryset


class BookDetailAPI(generics.RetrieveAPIView):
    serializer_class = serializers.BookDetailSerializer

    def get(self, *args, **kwargs):
        book = get_object_or_404(models.Book, id=self.kwargs["id"])
        return Response(self.get_serializer(book).data)


class AddAuthorAPI(generics.RetrieveAPIView):
    serializer_class = serializers.AuthorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class AddPublisherAPI(generics.RetrieveAPIView):
    serializer_class = serializers.PublisherSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class AddBookAPI(generics.RetrieveAPIView):
    serializer_class = serializers.BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdBookAPI(generics.RetrieveAPIView):
    serializer_class = serializers.BookSerializer

    def patch(self, request, *args, **kwargs):
        book = get_object_or_404(models.Book, id=self.kwargs["id"])
        serializer = self.get_serializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DelBookAPI(generics.RetrieveAPIView):
    def delete(self, request, *args, **kwargs):
        book = get_object_or_404(models.Book, id=self.kwargs["id"])
        book.delete()

        return Response({"detail": "Deleted"}, status=status.HTTP_200_OK)
