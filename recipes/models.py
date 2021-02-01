from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    instructions = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name='recipes')

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    amount = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
