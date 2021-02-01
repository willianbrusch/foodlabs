from .views import RecipeView
from django.urls import path

urlpatterns = [
    path('recipes/', RecipeView.as_view()),
    path('recipes/<int:recipe_id>/', RecipeView.as_view())
]
