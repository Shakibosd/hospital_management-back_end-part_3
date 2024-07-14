from django.db import models
from django.contrib.auth.models import User 
from patient_app.models import Patient

class Specialization(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class availableTime(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor_app/images/')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(availableTime)
    fees = models.IntegerField()
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f'Dr. {self.user.first_name} {self.user.last_name}'
    
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]    
class Review(models.Model):
    reviewr = models.ForeignKey(Patient, on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10)  

    def __str__(self):
        return f'Patient :  {self.reviewr.user.first_name}; Doctor : {self.doctor.user.first_name}' 
    
         
