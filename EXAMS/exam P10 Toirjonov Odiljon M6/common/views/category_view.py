from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.category_models import Category
from common.serializers.category_serializers import CategorySerializers


class CategoryListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.order_by("position")
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        serializer = CategorySerializers(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        serializer = CategorySerializers(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        category = self.get_object(pk)
        category.delete()
        return Response("Deleted.", status=status.HTTP_204_NO_CONTENT)
