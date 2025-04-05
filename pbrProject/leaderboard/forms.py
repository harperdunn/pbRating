from django import forms
from .models import UniversityTestimonial
from django.contrib.auth.models import User

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = UniversityTestimonial
        fields = ['name', 'role', 'stars', 'quote']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make 'name' optional
        self.fields['name'].required = False
        # All other fields will remain required by default

        # Set labels and help texts
        self.fields['stars'].label = "Rating (1-5 stars)"
        self.fields['stars'].help_text = "Please rate this university's plant-based options and related progress from 1 to 5 stars"
        
        # Custom widget attributes
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Name (Optional)'
        })
        self.fields['role'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Role (e.g., Current Student, Alumni) (Required)'
        })
        self.fields['stars'].widget.attrs.update({
            'class': 'form-control',
            'min': 1,
            'max': 5,
            'type': 'number'
        })
        self.fields['quote'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Share your experience (Required)',
            'rows': 4
        })