from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patient_app/images/')
    mobile_no = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    class Meta:
        verbose_name_plural = 'Patient'