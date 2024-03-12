from django.urls import path
from .views import *

urlpatterns = [
    path("ingredients/", IngredientsListView.as_view(), name="ingredients"),
]
