import graphene
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")


class CategoryType(DjangoObjectType):
    ingredients = graphene.List(IngredientType)

    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

    def resolve_ingredients(self, info):
        return self.ingredient_set.all()


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)