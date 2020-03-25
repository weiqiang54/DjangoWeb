from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Types
from .serializers import TypeModelSerializer


class TypeView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        types = Types.objects.all()
        types_serializer = TypeModelSerializer(types, many=True)
        return Response(types_serializer.data)

    def post(self, request):
        name =request.data.get('name')
        category_type = request.data.get('lei')
        parent_category_id = request.data.get('parent')
        type = Types()
        type.name = name
        type.category_type = category_type
        if parent_category_id:
            parent_category = Types.objects.filter(id=parent_category_id).first()
            type.parent_category = parent_category
        type.save()
        type_serializer = TypeModelSerializer(type)
        return Response(type_serializer.data)


