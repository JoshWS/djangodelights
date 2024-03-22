from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("ingredient/", IngredientsListView.as_view(), name="ingredient"),
    path(
        "ingredient/create/", IngredientCreateView.as_view(), name="ingredient_create"
    ),
    path(
        "ingredient/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient_update",
    ),
    path(
        "ingredient/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient_delete",
    ),
    path("purchase/", PurchasesListView.as_view(), name="purchase"),
    path("purchase/create/", PurchaseCreateView.as_view(), name="purchase_create"),
    path(
        "purchase/<int:pk>/update/",
        PurchaseUpdateView.as_view(),
        name="purchase_update",
    ),
    path(
        "purchase/<int:pk>/delete/",
        PurchaseDeleteView.as_view(),
        name="purchase_delete",
    ),
    path("menuitem/", MenuItemListView.as_view(), name="menuitem"),
    path("menuitem/create/", MenuItemCreateView.as_view(), name="menuitem_create"),
    path(
        "menuitem/<int:pk>/update/",
        MenuItemUpdateView.as_view(),
        name="menuitem_update",
    ),
    path(
        "menuitem/<int:pk>/delete/",
        MenuItemDeleteView.as_view(),
        name="menuitem_delete",
    ),
    path(
        "reciperequirement/",
        RecipeRequirementListView.as_view(),
        name="reciperequirement",
    ),
    path(
        "reciperequirement/create/",
        RecipeRequirementCreateView.as_view(),
        name="reciperequirement_create",
    ),
    path(
        "reciperequirement/<int:pk>/update/",
        RecipeRequirementUpdateView.as_view(),
        name="reciperequirement_update",
    ),
    path(
        "reciperequirement/<int:pk>/delete/",
        RecipeRequirementDeleteView.as_view(),
        name="reciperequirement_delete",
    ),
    path("finances/", FinancesView.as_view(), name="finances"),
    path("logout/", log_out, name="logout"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
]
