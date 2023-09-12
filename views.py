from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
from .models import Book
from rest_framework.decorators import api_view
from django.http import HttpRequest

class Books_api(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # def books_api(request):
    #     books = Book.objects.all()
    #     serializer = BookSerializer(books, many=True)
    #     return Response(serializer.data)
@api_view(['POST'])
def new_author(request: HttpRequest):
    author = AuthorSerializer(data=request.data)
    if author.is_valid():
        author.save()
        return HttpResponse("Success<br>Author id: " + str(author.instance.id))
    else:
        return Response(author.errors, status=400)
