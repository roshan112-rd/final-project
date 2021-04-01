from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Seeker(models.Model):    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True,null=True, upload_to='seeker/', default='user.jpg')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img=Image.open(self.image.path)
    #     if imag.height>300 or img.width>300:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)



    def __str__(self):
        return self.user.username

class SeekerAdditionalDetails(models.Model):    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    university = models.CharField(max_length=105,null=True)
    qualification = models.CharField(max_length=100, null=True)
    skills = models.CharField(max_length=100, null=True)
    preferred_job_category = models.CharField(max_length=100, null=True)
    available_for = models.CharField(max_length=100, null=True)
    preferred_location = models.CharField(max_length=100, null=True)
    work_experience = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.user.username

class SeekerSocialDetails(models.Model):    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    facebook = models.URLField(max_length=1005,null=True)
    instagram = models.URLField(max_length=1000, null=True)
    twitter = models.URLField(max_length=1000, null=True)
    others = models.URLField(max_length=1000, null=True) 

    def __str__(self):
        return self.user.username

class Recruiter(models.Model):    
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=100, null=True)
    company_type= models.CharField(max_length=100, null=True)
    company_name= models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='recruiter/')
    def __str__(self):
        return self.user.username