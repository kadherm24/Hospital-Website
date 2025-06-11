from django.db import models

# Create your models here.
class Doctor(models.Model):

    CATEGORY_CHOICES = [
    ('GENERAL', 'General'),
    ('CARDIOLOGY', 'Cardiology'),
    ('DERMATOLOGY', 'Dermatology'),
    ('ENDOCRINOLOGY', 'Endocrinology'),
    ('GASTROENTEROLOGY', 'Gastroenterology'),
    ('HEMATOLOGY', 'Hematology'),
    ('INFECTIOUS_DISEASE', 'Infectious Disease'),
    ('NEPHROLOGY', 'Nephrology'),
    ('NEUROLOGY', 'Neurology'),
    ('OBSTETRICS_GYNECOLOGY', 'Obstetrics & Gynecology'),
    ('ONCOLOGY', 'Oncology'),
    ('OPHTHALMOLOGY', 'Ophthalmology'),
    ('ORTHOPEDICS', 'Orthopedics'),
    ('OTOLARYNGOLOGY', 'Otolaryngology (ENT)'),
    ('PEDIATRICS', 'Pediatrics'),
    ('PSYCHIATRY', 'Psychiatry'),
    ('PULMONOLOGY', 'Pulmonology'),
    ('RHEUMATOLOGY', 'Rheumatology'),
    ('SURGERY', 'Surgery'),
    ('UROLOGY', 'Urology'),
    ('RADIOLOGY', 'Radiology'),
    ('ANESTHESIOLOGY', 'Anesthesiology'),
    ('EMERGENCY_MEDICINE', 'Emergency Medicine'),
    ('FAMILY_MEDICINE', 'Family Medicine'),
    ('GENETICS', 'Genetics'),
    ('GERIATRICS', 'Geriatrics'),
    ('IMMUNOLOGY', 'Immunology'),
    ('INTERNAL_MEDICINE', 'Internal Medicine'),
    ('OCCUPATIONAL_MEDICINE', 'Occupational Medicine'),
    ('PATHOLOGY', 'Pathology'),
    ('PHYSICAL_MED_REHAB', 'Physical Medicine & Rehabilitation'),
    ('PLASTIC_SURGERY', 'Plastic Surgery'),
    ('PREVENTIVE_MEDICINE', 'Preventive Medicine'),
    ('SPORTS_MEDICINE', 'Sports Medicine'),
    ('TRANSPLANT_SURGERY', 'Transplant Surgery'),
    ('TRAUMA_SURGERY', 'Trauma Surgery'),
    ('VASCULAR_SURGERY', 'Vascular Surgery'),
    ]
    image = models.ImageField(upload_to='doctors/', null = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    category = models.CharField(choices= CATEGORY_CHOICES, null=True )


    def __str__(self):
        return f"Dr. {self.first_name.capitalize()} {self.last_name.capitalize()}"