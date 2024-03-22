from django.db import models


# Create your models here.
class Ingredient(models.Model):
    """
    An iIngredient of different Ingredients, their available quantity, and their prices per unit.

    Fields:
        name (CharField): The name of the Ingredient.
        quantity (IntegerField): The available quantity of the Ingredient.
        price (IntegerField): The price per unit of the Ingredient.

    Methods:
        __str__: Returns the name of the Ingredient.
    """

    unit = {
        "unit": "unit",
        "eggs": "eggs",
        "oz": "oz",
        "lb": "lb",
        "g": "g",
        "kg": "kg",
    }

    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=unit.items())
    unit_price = models.DecimalField(
        decimal_places=1, max_digits=5, verbose_name="Price per unit"
    )

    def get_absolute_url(self):
        return "/ingredient"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def get_absolute_url(self):
        return "/menuitem"


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(decimal_places=1, max_digits=4)

    def get_absolute_url(self):
        return "/reciperequirement"


class Purchase(models.Model):
    """
    A purchase of ingredients for a MenuItem.

    Fields:
        menu_item (ForeignKey to MenuItem): The MenuItem being purchased.
        quantity (IntegerField): The quantity of the MenuItem being purchased.
        timestamp (DateTimeField): The timestamp of when the purchase was made.
    """

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/Purchase"

    """ The sum of the unit_price for each ingredient used in a menu_item"""

    def get_cost(self):
        recipe_objects = RecipeRequirement.objects.filter(menu_item=self.menu_item)
        return sum([z.ingredient.unit_price * z.quantity for z in recipe_objects])

    """ The price of the menu_item"""

    def get_revenue(self):
        return self.menu_item.price

    """ The revenue - the cost"""

    def get_profit(self):
        return float(self.get_revenue()) - float(self.get_cost())
