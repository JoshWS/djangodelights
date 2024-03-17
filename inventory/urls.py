from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("ingredients/", IngredientsListView.as_view(), name="ingredients"),
    path(
        "ingredients/create/", IngredientCreateView.as_view(), name="ingredient_create"
    ),
    path(
        "ingredients/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient_update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient_delete",
    ),
    path("purchases/", PurchasesListView.as_view(), name="purchases"),
    path("purchases/create/", PurchaseCreateView.as_view(), name="purchase_create"),
    path(
        "purchases/<int:pk>/update/",
        PurchaseUpdateView.as_view(),
        name="purchase_update",
    ),
    path(
        "purchases/<int:pk>/delete/",
        PurchaseDeleteView.as_view(),
        name="purchase_delete",
    ),
]
