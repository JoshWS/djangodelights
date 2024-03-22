from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

# from .forms import *


# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete_form.html"
    success_url = "/ingredient"


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create_form.html"
    success_url = "/ingredient"
    fields = "__all__"


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update_form.html"
    success_url = "/ingredient"
    fields = "__all__"


class IngredientsListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_view.html"


class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "inventory/purchase_delete_form.html"
    success_url = "/purchase"


class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/purchase_create_form.html"
    success_url = "/purchase"
    fields = "__all__"

    def post(self, request):
        menu_item_id = request.POST["menu_item"]
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            required_ingredient = requirement.ingredient
            required_ingredient.quantity -= requirement.quantity
            dictionary = {"form": self.get_form()}
            if required_ingredient.quantity < 0:
                dictionary["failed"] = True
                return render(
                    request, "inventory/purchase_create_form.html", dictionary
                )
            required_ingredient.save()

        purchase.save()
        dictionary["failed"] = False
        return redirect("/purchase")


class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update_form.html"
    success_url = "/purchase"
    fields = "__all__"


class PurchasesListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_view.html"


class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "inventory/menuitem_delete_form.html"
    success_url = "/menuitem"


class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create_form.html"
    success_url = "/menuitem"
    fields = "__all__"


class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update_form.html"
    success_url = "/menuitem"
    fields = "__all__"


class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitem_view.html"


class RecipeRequirementDeleteView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_delete_form.html"
    success_url = "/reciperequirement"


class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create_form.html"
    success_url = "/reciperequirement"
    fields = "__all__"


class RecipeRequirementUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_update_form.html"
    success_url = "/reciperequirement"
    fields = "__all__"


class RecipeRequirementListView(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_view.html"


class FinancesView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/finances.html"

    def get_context_data(self, **kwargs):
        context = {
            "total_cost": round(sum([p.get_cost() for p in Purchase.objects.all()]), 2),
            "total_revenue": round(
                sum([p.get_revenue() for p in Purchase.objects.all()]), 2
            ),
            "total_profit": round(
                sum([p.get_profit() for p in Purchase.objects.all()]), 2
            ),
        }
        return context


def log_out(request):
    logout(request)
    return redirect("/")
