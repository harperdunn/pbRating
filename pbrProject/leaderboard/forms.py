from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review, University

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['university', 'role', 'review_text', 'stars', 'photo_permission', 'name_permission']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set university choices
        self.fields['university'].queryset = University.objects.all().order_by('fullname')
        
        # Add CSS classes to form fields
        self.fields['university'].widget.attrs.update({'class': 'form-select'})
        self.fields['role'].widget.attrs.update({'class':'form-select'})
        self.fields['review_text'].widget = forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3
        })
        self.fields['stars'].widget.attrs.update({
            'class': 'form-control',
            'min': 1,
            'max': 5
        })
        self.fields['photo_permission'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['name_permission'].widget.attrs.update({'class': 'form-check-input'})