from django.contrib import admin

from inventory.models import Product, Type


@admin.register(Type)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = (
        'image_tag_1',
        'image_tag_2',
        'image_tag_3',
        'image_tag_color',
    )
    list_filter = (
        'gender',
        'season',
        'color',
        'type',
        'size',
        'quality',
        'brand',
        'quality',
        'date_of_arrival',
        'in_stock',
    )
    search_fields = (
        'gender',
        'season',
        'color',
        'type',
        'size',
        'quality',
        'brand',
        'quality',
        'date_of_arrival',
        'in_stock',
    )
    list_display = (
        'id',
        'image_tag_1',
        'image_tag_2',
        'image_tag_3',
        'image_tag_color',
        'gender',
        'season',
        'color',
        'type',
        'size',
        'quality',
        'brand',
        'quality',
        'date_of_arrival',
        'in_stock',
    )
