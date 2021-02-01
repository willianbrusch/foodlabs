from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe, Ingredient, Tag
from .serializers import RecipeSerializer, IngredientSerializer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist,  MultipleObjectsReturned


class RecipeView(APIView):
    def get(self, request, recipe_id=''):
        if recipe_id:
            try:
                recipe = Recipe.objects.get(id=recipe_id)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = RecipeSerializer(recipe)
            return Response(serializer.data)

        queryset = Recipe.objects.all()
        serializer = RecipeSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        recipe, created = Recipe.objects.get_or_create(
            name=request.data['name'],
            description=request.data['description'],
            instructions=request.data['instructions']
        )

        if not created:
            return Response({'message': f'{recipe.name} already exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        for tag in request.data['tags']:
            try:
                tag = Tag.objects.get_or_create(**tag)[0]
                recipe.tags.add(tag)
            except MultipleObjectsReturned:
                Tag.objects.filter().first()
                recipe.tags.add(tag)

        for ingredient in request.data['ingredient_set']:
            Ingredient.objects.create(**ingredient, recipe=recipe)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, recipe_id):
        try:
            recipe = Recipe.objects.get(id=recipe_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        recipe.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
