from rest_framework import mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission

from .serializers import BookSerializer, BookModelSerializer
from .models import UserProfile, Book


# Serializer
class BookAPIView1(APIView):

    def get(self, request, format=None):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            if developer.money > 0:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=isbn)
                book_serializer = BookSerializer(books, many=True)
                developer.money -= 1
                developer.save()
                return Response(book_serializer.data)
            else:
                return Response("兄弟，又到了充钱的时候！好开森！")
        else:
            return Response("查无此人")


# ModelSerializer
class BookAPIView2(APIView):

    def get(self, request, format=None):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            if developer.money:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=isbn)
                book_serializer = BookModelSerializer(books, many=True)
                developer.money -= 1
                developer.save()
                return Response(book_serializer.data)
            else:
                return Response("兄弟，又到了充钱的时候！好开森！")
        else:
            return Response("查无此人")


# mixins.ListModelMixin+GenericAPIView
class BookMixinView1(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            if developer.money:
                isbn = self.request.query_params.get('isbn', 0)
                self.queryset = Book.objects.filter(isbn=isbn)
                developer.money -= 1
                developer.save()
                return self.list(request, *args, **kwargs)
            else:
                return Response("兄弟，又到了充钱的时候！好开森！")
        else:
            return Response("查无此人")


# generics.ListAPIView
class BookMixinView2(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        APIKey = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            if developer.money:
                isbn = self.request.query_params.get('isbn', 0)
                self.queryset = Book.objects.filter(isbn=isbn)
                developer.money -= 1
                developer.save()
                return self.list(request, *args, **kwargs)
            else:
                return Response("兄弟，又到了充钱的时候！好开森！")
        else:
            return Response("查无此人")


# viewsets+Router
class IsDeveloper(BasePermission):
    message = '查无此人啊'

    def has_permission(self, request, view):
        APIKey = request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            return True
        else:
            return False


class EnoughMoney(BasePermission):
    message = '兄弟，又到了充钱的时候！好开森！'

    def has_permission(self, request, view):
        APIKey = request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer.money > 0:
            developer.money -= 1
            developer.save()
            return True
        else:
            return False


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    authentication_classes = []
    permission_classes = [IsDeveloper, EnoughMoney]

    def get_queryset(self):
        isbn = self.request.query_params.get('isbn', 0)
        query = self.queryset.filter(isbn=isbn)

        return query

