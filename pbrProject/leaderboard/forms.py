from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review, University

# class TestimonialForm(forms.ModelForm):
#     class Meta:
#         model = UniversityTestimonial
#         fields = ['name', 'role', 'stars', 'quote']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Make 'name' optional
#         self.fields['name'].required = False
#         # All other fields will remain required by default

#         # Set labels and help texts
#         self.fields['stars'].label = "Rating (1-5 stars)"
#         self.fields['stars'].help_text = "Please rate this university's plant-based options and related progress from 1 to 5 stars"
        
#         # Custom widget attributes
#         self.fields['name'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Your Name (Optional)'
#         })
#         self.fields['role'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Your Role (e.g., Current Student, Alumni) (Required)'
#         })
#         self.fields['stars'].widget.attrs.update({
#             'class': 'form-control',
#             'min': 1,
#             'max': 5,
#             'type': 'number'
#         })
#         self.fields['quote'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Share your experience (Required)',
#             'rows': 4
#         })

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