from django import forms
from . import models, parser_mybook

class ParserForm(forms.Form):
    MEDIA_CHOICES = {
        ('rezka', 'rezka'),
        ('knigochet', 'knigochet'),
    }
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    
    class Meta:
        fields = [
            'media_type',
        ]
        
    def parser_data(self):
        if self.data['media_type'] == 'knigochet':
            file_mybook = parser_mybook.parsing()
            for i in file_mybook:
                models.MybookParser.objects.create(**i)
                
        elif self.data['media_type'] == 'rezka':
            file_mybook = parser_mybook.parsing()
            for i in file_mybook:
                models.MybookParser.objects.create(**i)