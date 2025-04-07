from django.contrib import admin
from .models import University
from . models import UniversityImage, UniversityTestimonial, Review
# Register your models here.

class UniversityImageInline(admin.TabularInline):  # Allows adding images inline in the University admin
    model = UniversityImage
    extra = 1  # Number of empty image forms to display

class UniversityTestimonialInline(admin.TabularInline):
    model=UniversityTestimonial
    extra=1

class ReviewInline(admin.TabularInline):
    model=Review


class ReviewAdmin(admin.ModelAdmin):
    # Display fields in list view
    list_display = ('user', 'university', 'get_role_display', 'stars', 'created_at')
    
    # Add filters
    list_filter = ('university', 'role', 'stars', 'created_at')
    
    # Make the list searchable
    search_fields = ('user__email', 'review_text', 'university__fullname')
    
    # Group fields in detail view
    readonly_fields = ('created_at',)  # Add this

    fieldsets = (
        ('User Info', {
            'fields': ('user', 'created_at')
        }),
        ('Review Content', {
            'fields': ('university', 'role', 'review_text', 'stars')
        }),
        ('Permissions', {
            'fields': ('photo_permission', 'name_permission'),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
    )
    
    
    # Automatically set the user when adding from admin
    def save_model(self, request, obj, form, change):
        if not change:  # Only for new objects
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Review, ReviewAdmin)

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = [UniversityImageInline, UniversityTestimonialInline]  # Add the inline for images


@admin.register(UniversityImage)
class UniversityImageAdmin(admin.ModelAdmin):
    list_display = ('university', 'caption', 'image')

@admin.register(UniversityTestimonial)
class UniversityTestimonialAdmin(admin.ModelAdmin):
    list_display=('university', 'name', 'role', 'stars', 'quote')

