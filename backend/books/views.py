from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, BookListSerializer
from rest_framework import status
from rest_framework.response import Response
from books.utils.constans import FAKE_AUTHOR


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET'] and 'pk' not in self.kwargs:
            return BookListSerializer
        return BookSerializer

    def perform_create(self, serializer):
        author = Author.objects.get(id=self.request.data['author'])

        if not self.request.user.id == author.user_id:
            serializer.save()
        else:
            return Response(FAKE_AUTHOR, status=status.HTTP_406_NOT_ACCEPTABLE)
