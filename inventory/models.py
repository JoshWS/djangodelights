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
    unit_price = models.FloatField(verbose_name="Price per unit")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    menu_items = models.ManyToManyField(
        Ingredient, through="RecipeRequirement", related_name="menu_items_for_menu_item"
    )

    def __str__(self):
        return f"{self.name} - ${self.price}"


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    class Meta:
        unique_together = ("menu_item", "ingredient")

    def __str__(self):
        return f"{self.menu_item.name} needs {self.quantity}x {self.ingredient.name}"


class Purchase(models.Model):
    """
    A purchase of ingredients for a MenuItem.

    Fields:
        menu_item (ForeignKey to MenuItem): The MenuItem being purchased.
        quantity (IntegerField): The quantity of the MenuItem being purchased.
        timestamp (DateTimeField): The timestamp of when the purchase was made.
    """

    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item.name} - {self.quantity} @ {self.timestamp}"
