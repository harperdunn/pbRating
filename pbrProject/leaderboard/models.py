from django.db import models
from pathlib import Path
import os

# Create your models here.
class University(models.Model):
    fullname=models.CharField(max_length=255)
    overallScore=models.IntegerField(default=0)
    overallGrade=models.CharField(max_length=255, default='B')
    detailsOverview=models.TextField(default='Details Overview Goes Here')
    images=models.ImageField


    # High-Impact Questions (100 points each)
    animal_based_percentage = models.FloatField(null=True, blank=True, default=79)  # 0-100%
    #per_capita_emissions = models.IntegerField(null=True, blank=True)  # 1-5 ranking
    formal_commitments = models.FloatField(null=True, blank=True, default=0)  # 0, 1, 2, 3
    transition_provider = models.BooleanField(default=False) 
    vegan_meals = models.FloatField(null=True, blank=True, default=0)  # vegan meals per average dinner day, 0-3+
    
    # Medium-Impact Questions (50 points each)
    sustainable_page = models.BooleanField(default=False)
    default_veg_program = models.IntegerField(null=True, blank=True, default=0)  # 0(never), 1(piloted), 2(currently implemented)
    culinary_training = models.IntegerField(null=True, blank=True, default=0)  # 0(never), 1(past), 2(recent- past 2 years)
    recent_changes = models.IntegerField(null=True, blank=True, default=0) #0(none), 1(minor), 2(major)
    plant_breakfast_options = models.FloatField(null=True, blank=True, default=0)  # 0-5+
    student_satisfaction = models.IntegerField(null=True, blank=True, default=0)  # 0 (no survey data), 1(mixed/negative), 2(positive)


    # Low-Impact Questions (20 points each)
    plant_desserts = models.IntegerField(null=True, blank=True, default=0)  # 0- never, 1-occasionally , 2- always
    salad_protein = models.FloatField(null=True, blank=True, default=0)  # 0-4+
    promotional_materials = models.BooleanField(default=False)
    sustainability_guidebook = models.BooleanField(default=False)
    labeling = models.FloatField(null=True, blank=True, default=0)  # 0- no labeling, 1- inconsistent, 2- clear and consistent
    naming = models.FloatField(null=True, blank=True, default=0)  # 0, 1, 2
    meatless_monday = models.IntegerField(null=True, blank=True, default=0)  # 0, 1, 2

    def get_animal_based_percentage_points(self):
        if self.animal_based_percentage>80:
            return 0
        elif self.animal_based_percentage>70:
            return 25
        elif self.animal_based_percentage>60:
            return 50
        elif self.animal_based_percentage>50:
            return 75
        else: return 100

    def get_commitments_points(self):
        if self.formal_commitments>=2: return 100 #multiple commitments signed
        elif self.formal_commitments>=1: return 75 #1 individual commitment signed
        elif self.transition_provider: return 50 #working with transition provider
        elif self.formal_commitments>0: return 25 #1+ informal commitment
        else: return 0

    def get_only_formal_commitments(self): #this excludes the informal commitements by truncating bc the informals are worth 0.5 points
        return int(self.formal_commitments)

    def get_vegan_meals_points(self):
        if self.vegan_meals>=3:
            return 100
        elif self.vegan_meals>=2:
            return 75
        elif self.vegan_meals>=1:
            return 50
        elif self.vegan_meals>=0.5:
            return 25
        else:
            return 0
        
    def get_high_impact_questions_points(self):
        return self.get_animal_based_percentage_points()+self.get_commitments_points()+self.get_vegan_meals_points()
                                
    
    def get_medium_impact_questions_points(self):
        score=0
        # if self.vegan_station:
        #     score+=50
        if self.sustainable_page:
            score+=20
        if self.default_veg_program==2:
            score+=50
        elif self.default_veg_program==1:
            score+=25
        if self.culinary_training==2:
            score+=50
        elif self.culinary_training==1:
            score+=25
        if self.plant_breakfast_options>4:
            score+=50
        elif self.plant_breakfast_options>3:
            score+=40
        elif self.plant_breakfast_options>2:
            score+=20
        elif self.plant_breakfast_options>1:
            score+=10
        if self.student_satisfaction==2:
            score+=50
        elif self.student_satisfaction==1:
            score+=20
        return score
    
    def get_low_impact_questions_points(self):
        score=0
        if self.transition_provider:
            score+=20
        if self.sustainability_guidebook:
            score+=20
        if self.plant_desserts==2:
            score+=20
        elif self.plant_desserts==1:
            score+=10
        if self.salad_protein>=4:
            score+=20
        elif self.salad_protein>=2:
            score+=10
        if self.promotional_materials:
            score+=20
        if self.labeling==2:
            score+=20
        elif self.labeling==1:
            score+=10
        if self.naming==2:
            score+=20
        elif self.naming==1:
            score+=10
        if self.meatless_monday==2:
            score+=20
        elif self.meatless_monday==1:
            score+=10
        return score
        
    def get_overall_score(self):
        return self.get_high_impact_questions_points()+self.get_medium_impact_questions_points()+self.get_low_impact_questions_points()

    def get_grade(self):
        score = self.overallScore
        if score >= 400:
            return 'A-'
        elif score >= 375:
            return 'B+'
        elif score >= 350:
            return 'B'
        elif score >= 325:
            return 'B-'
        elif score >= 300:
            return 'C+'
        elif score >= 275:
            return 'C'
        elif score >= 250:
            return 'C-'
        elif score >= 200:
            return 'D+'
        elif score >= 150:
            return 'D'
        elif score >= 75:
            return 'D-'
        else:
            return 'F'
    def get_labeling_star_rating(self):
        #naming has more weight
        value=(self.naming*1.5)+self.labeling
        if value>=5:
            return 5
        elif value>=4:
            return 4
        elif value>=3:
            return 3
        elif value>=2:
            return 2
        elif value>=1: 
            return 1
        else: return 0
        
    #overriding the save function, ensuring that overallscore gets updated whenever an attribute changes
    def save(self, *args, **kwargs):
        #Automatically update overallScore before saving.
        self.overallScore = self.get_overall_score()
        self.overallGrade=self.get_grade()
        super().save(*args, **kwargs)  # Call the parent class's save method
        #this automatically creates the folder to store the images in

    
    @property
    def image_folder(self):
        # Dynamically generate the folder name based on the university name
        return f"university_images/{self.fullname.replace(' ', '_').lower()}"

def upload_to_university_images(instance, filename):
    # instance: The UniversityImage instance being saved
    # filename: The original name of the uploaded file
    #instance.university means the University object that corresponds to this image (model instance actually)
    return f"{instance.university.image_folder}/{filename}"


#um idk ab this
class UniversityImage(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to_university_images)
    caption = models.CharField(max_length=255, blank=True)  # Optional caption

    def __str__(self):
        return f"Image for {self.university.fullname}"
    
    #overriding the save method makes sure files are cleaned up appropriately
    def save(self, *args, **kwargs):
        # Check if the instance already exists in the database
        if self.pk:
            # Get the old image file path
            old_instance = UniversityImage.objects.get(pk=self.pk) #pk means primary key
            if old_instance.image and old_instance.image != self.image:
                # Delete the old file if it exists
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)

        # Call the parent save method
        super().save(*args, **kwargs)

    #overriding the delete method so files are cleaned up when a University model with images is deleted on the admin side.
    def delete(self, *args, **kwargs):
        # Delete the file from the filesystem
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        # Call the parent delete method
        super().delete(*args, **kwargs)


class UniversityTestimonial(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='testimonials')
    name=models.CharField
    role=models.CharField
    quote=models.TextField

    def __str__(self):
        return f"Testimonial for {self.university.fullname}"



