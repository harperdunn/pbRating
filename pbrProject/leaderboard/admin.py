from django.contrib import admin
from .models import University
from . models import UniversityImage
# Register your models here.

class UniversityImageInline(admin.TabularInline):  # Allows adding images inline in the University admin
    model = UniversityImage
    extra = 1  # Number of empty image forms to display

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [UniversityImageInline]  # Add the inline for images

@admin.register(UniversityImage)
class UniversityImageAdmin(admin.ModelAdmin):
    list_display = ('university', 'caption', 'image')
