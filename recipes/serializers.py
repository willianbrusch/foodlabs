from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    name = serializers.CharField()


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField()
    unit = serializers.CharField()
    amount = serializers.IntegerField()


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    instructions = serializers.CharField()
    tags = TagSerializer(many=True)
    ingredient_set = IngredientSerializer(many=True)
