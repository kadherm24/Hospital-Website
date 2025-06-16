from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_patients')
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others')   
    ]

    RELATION_CHOICES = [
    ('SELF', 'Self'),
    ('FATHER', 'Father'),
    ('MOTHER', 'Mother'),
    ('BROTHER', 'Brother'),
    ('SISTER', 'Sister'),
    ('SPOUSE', 'Spouse'),
    ('SON', 'Son'),
    ('DAUGHTER', 'Daughter'),
    ('GRANDFATHER', 'Grandfather'),
    ('GRANDMOTHER', 'Grandmother'),
    ('UNCLE', 'Uncle'),
    ('AUNT', 'Aunt'),
    ('COUSIN', 'Cousin'),
    ('FRIEND', 'Friend'),
    ('OTHER', 'Other'),
    ]

    image = models.ImageField(upload_to= 'patients/', null=True)
    full_name = models.CharField()
    gender = models.CharField(choices= GENDER_CHOICES)
    age = models.IntegerField()
    phone = models.IntegerField(max_length=10)
    relation_type = models.CharField(choices = RELATION_CHOICES)

def __str__(self):
        return f"Dr. {self.full_name.capitalize()}"