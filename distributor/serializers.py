from rest_framework import serializers

from distributor.models import Tag, Category, Product


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'name'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'.split()


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title text is_active created updated category tags'.split()

    def get_category(self, obj):
        return obj.category.name
