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
class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"
    success_url = "/ingredients"


class IngredientCreateView(CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    success_url = "/ingredients"


class IngredientUpdateView(UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    success_url = "/ingredients"


class IngredientsListView(TemplateView):
    model = Ingredient
    template_name = "inventory/ingredients_view.html"
