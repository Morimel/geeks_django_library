from django.shortcuts import render, get_object_or_404, redirect
from .models import IngridientModel
from .forms import IngredientForm
from recipe.models import RecipeModel

def add_ingredient(request, recipe_id):
    recipe = get_object_or_404(RecipeModel, pk=recipe_id)
    
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe  
            ingredient.save()
            return redirect('recipe_detail', pk=recipe_id)
    else:
        form = IngredientForm()

    return render(request, 'add_ingredient.html', {'form': form, 'recipe': recipe})
