from django.db import models
from django.utils.safestring import mark_safe


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=99999, decimal_places=2)
    quantity = models.IntegerField()
    measure_unit = models.CharField(
        max_length=10,
        choices=[
            ('g', 'grams'),
            ('ml', 'milliliter'),
            ('pcs', 'pieces'),
        ]
    )

    def __str__(self):
        return '{} | €{:.2F} -> {} {}'.format(self.name, self.price, self.quantity, self.measure_unit)


class FoodCombination(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, through='FoodCombinationThrough')

    def total_price(self):
        total = 0
        for x in self.foodcombinationthrough_set.all():
            total += calc_price(x.ingredient.price, x.ingredient.quantity, x.quantity)
        return mark_safe('{}'.format(round(total, 2)))

    total_price.short_description = 'Total price'

    def __str__(self):
        return self.title


class FoodCombinationThrough(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    food_combination = models.ForeignKey(FoodCombination, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.ingredient.name + ' | ' + self.food_combination.title


def calc_price(price, quantity, v):
    return price * v / quantity
