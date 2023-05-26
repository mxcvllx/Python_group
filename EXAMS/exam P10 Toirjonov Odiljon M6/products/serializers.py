from rest_framework import serializers

from common.models.category_models import Category
from products.models import Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class ProductListSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ["id", "title", "slug", "price", "image", "category"]


class ProductCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)

    class Meta:
        model = Product
        fields = ["title", "slug", "price", "category"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = ProductCategorySerializer(instance.category).data
        return data
