from django.db import models
from recipe.models import RecipeModel

class IngridientModel(models.Model):
    UNIT_CHOICE = (
        ("граммы", "граммы"),
        ("килограммы", "килограммы"),
        ("миллилитры", "миллилитры"),
        ("литры", "литры"),
        ("штуки", "штуки"),
    )
    
    name = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    unit = models.TextField(choices=UNIT_CHOICE)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name="ingredients")
    
    def __str__(self):
        return self.name