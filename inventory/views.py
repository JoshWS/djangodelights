from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# from .forms import *


# Create your views here.
class HomeView(TemplateView):
    template_name = "inventory/home.html"


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = "/ingredient"


class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    success_url = "/ingredient"
    fields = "__all__"


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    success_url = "/ingredient"
    fields = "__all__"


class IngredientsListView(ListView):
    model = Ingredient
    template_name = "inventory/ingredient_view.html"


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    success_url = "/purchase"


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    success_url = "/purchase"
    fields = "__all__"


class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    success_url = "/purchase"
    fields = "__all__"


class PurchasesListView(ListView):
    model = Purchase
    template_name = "inventory/purchase_view.html"


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = "/menuitem"


class MenuItemCreateView(CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    success_url = "/menuitem"
    fields = "__all__"


class MenuItemUpdateView(UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update_form.html"
    success_url = "/menuitem"
    fields = "__all__"


class MenuItemListView(ListView):
    model = MenuItem
    template_name = "inventory/menuitem_view.html"


class RecipeRequirementDeleteView(DeleteView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_delete_form.html"
    success_url = "/reciperequirement"


class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create_form.html"
    success_url = "/reciperequirement"
    fields = "__all__"


class RecipeRequirementUpdateView(UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_update_form.html"
    success_url = "/reciperequirement"
    fields = "__all__"


class RecipeRequirementListView(ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_view.html"
