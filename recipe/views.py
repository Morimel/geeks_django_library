from django.shortcuts import render, get_object_or_404, redirect
from .models import RecipeModel
from ingridient.models import IngridientModel
from .forms import RecipeForm
from ingridient.forms import IngredientForm

def recipe_list(request):
    recipes = RecipeModel.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


def recipe_detail(request, pk):
    recipe = get_object_or_404(RecipeModel, pk=pk)
    ingredients = recipe.ingredients.all()  
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})


def delete_recipe(request, pk):
    recipe = get_object_or_404(RecipeModel, pk=pk)
    recipe.delete()
    return redirect('recipe_list')
