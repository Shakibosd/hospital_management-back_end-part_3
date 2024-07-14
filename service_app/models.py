from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to='service_app/images/')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Services'