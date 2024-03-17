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
    success_url = "/ingredients"


class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    success_url = "/ingredients"
    fields = "__all__"


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    success_url = "/ingredients"
    fields = "__all__"


class IngredientsListView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients_view.html"


class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    success_url = "/purchases"


class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    success_url = "/purchases"
    fields = "__all__"


class PurchaseUpdateView(UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    success_url = "/purchases"
    fields = "__all__"


class PurchasesListView(ListView):
    model = Purchase
    template_name = "inventory/purchase_view.html"
