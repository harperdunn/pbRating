from django.contrib import admin
from .models import University
from . models import UniversityImage, UniversityTestimonial
# Register your models here.

class UniversityImageInline(admin.TabularInline):  # Allows adding images inline in the University admin
    model = UniversityImage
    extra = 1  # Number of empty image forms to display

class UniversityTestimonialInline(admin.TabularInline):
    model=UniversityTestimonial
    extra=1

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [UniversityImageInline]  # Add the inline for images


@admin.register(UniversityImage)
class UniversityImageAdmin(admin.ModelAdmin):
    list_display = ('university', 'caption', 'image')

@admin.register(UniversityTestimonial)
class UniversityTestimonialAdmin(admin.ModelAdmin):
    list_display=('university', 'name', 'role', 'stars', 'quote')

