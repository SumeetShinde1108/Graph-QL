from django.contrib import admin
from ingredients.models import Category, Ingredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id', 'name')



@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'notes')
