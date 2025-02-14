from django.db import models

# Create your models here.
class University(models.Model):
    fullname=models.CharField(max_length=255)
    overallScore=models.FloatField(default=0)
    overallGrade=models.CharField(max_length=255, default='B')
    detailsOverview=models.TextField(default='none')
  
    # High-Impact Questions (100 points each)
    animal_based_percentage = models.IntegerField(null=True, blank=True, default=100)  # 0-100%
    #per_capita_emissions = models.IntegerField(null=True, blank=True)  # 1-5 ranking
    formal_commitments = models.IntegerField(null=True, blank=True, default=0)  # 0, 1, 2
    vegan_meals = models.FloatField(null=True, blank=True, default=0)  # vegan meals per average dinner day, 0-3+
    
    # Medium-Impact Questions (50 points each)
    sustainable_page = models.BooleanField(default=False)
    default_veg_program = models.IntegerField(null=True, blank=True, default=0)  # 0(never), 1(piloted), 2(currently implemented)
    culinary_training = models.IntegerField(null=True, blank=True, default=0)  # 0(never), 1(past), 2(recent- past 2 years)
    recent_changes = models.IntegerField(null=True, blank=True, default=0) #0(none), 1(minor), 2(major)
    plant_breakfast_options = models.IntegerField(null=True, blank=True, default=0)  # 0-5+
    student_satisfaction = models.IntegerField(null=True, blank=True, default=0)  # 0 (no survey data), 1(mixed/negative), 2(positive)



    # Low-Impact Questions (20 points each)
    plant_desserts = models.IntegerField(null=True, blank=True, default=0)  # 0- never, 1-occasionally , 2- always
    salad_protein = models.IntegerField(null=True, blank=True, default=0)  # 0-4+
    transition_provider = models.BooleanField(default=False) 
    promotional_materials = models.BooleanField(default=False)
    sustainability_guidebook = models.BooleanField(default=False)
    labeling = models.IntegerField(null=True, blank=True, default=0)  # 0- no labeling, 1- inconsistent, 2- clear and consistent
    naming = models.IntegerField(null=True, blank=True, default=0)  # 0, 1, 2
    meatless_monday = models.IntegerField(null=True, blank=True, default=0)  # 0, 1, 2

    def get_animal_based_percentage_points(self):
        if self.animal_based_percentage>80:
            return 0
        elif self.animal_based_percentage>60:
            return 25
        elif self.animal_based_percentage>40:
            return 50
        elif self.animal_based_percentage>20:
            return 75
        else: return 100

    def get_formal_commitments_points(self):
        if self.formal_commitments==2: return 100 #multiple commitments signed
        elif self.formal_commitments==1: return 75
        else: return 0

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
        return self.get_animal_based_percentage_points()+self.get_formal_commitments_points()+self.get_vegan_meals_points()
                                
    
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
   
    #overriding the save function, ensuring that overallscore gets updated whenever an attribute changes
    def save(self, *args, **kwargs):
        #Automatically update overallScore before saving.
        self.overallScore = self.get_overall_score()
        super().save(*args, **kwargs)  # Call the parent class's save method

    


