from django.db import models

# Create your models here.
class Feedback(models.Model):
    email = models.CharField(max_length=50, null=True)
    feedback = models.CharField(max_length=1050, null=True)
    image = models.ImageField(blank=True,null=True, upload_to='feedback/')

    def __str__(self):
        return self.email