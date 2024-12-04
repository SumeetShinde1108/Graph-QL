import graphene 
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        Model = Category
        fields = ('id', 'name', 'ingredients')


class IngredientType(DjangoObjectType):
    class Meta:
        Model = Ingredient
        fields = ('id', 'name', 'notes', 'category')


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.List(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_categorooy_by_name(root, info, name):
        try:
            name=Category.objects.get(name=name)
        except Category.DoesNotExists:
            return None 

schema = graphene.schema(query=Query)




