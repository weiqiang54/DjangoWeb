from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView


class IndexView(APIView):

    def get(self, request):
        print(request)

        return HttpResponse('首页')

