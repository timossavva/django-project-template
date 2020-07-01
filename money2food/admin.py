from django.contrib import admin

from money2food.models import *


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'measure_unit')


class FoodCombinationThroughInline(admin.TabularInline):
    model = FoodCombinationThrough
    extra = 3


@admin.register(FoodCombinationThrough)
class FoodCombinationThroughAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodCombination)
class FoodCombinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_price')
    filter_horizontal = ('ingredients',)
    inlines = (FoodCombinationThroughInline,)
    readonly_fields = ['total_price']
