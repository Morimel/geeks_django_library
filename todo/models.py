from django.db import models
from library.models import Books

class TodoModel(models.Model):
    CHECK = (
        ("✅", "✅"),
        ("❌", "❌")
    )
    task = models.TextField()
    checked = models.CharField(choices=CHECK, max_length=10)
    choice_movie = models.ForeignKey(Books, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField
    
    def __str__(self):
        return f'{self.task}--{self.checked}'