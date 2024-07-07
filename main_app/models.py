from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='user_info_images/')

class Experience(models.Model):
    p_year=models.CharField(max_length=300)
    sc=models.CharField(max_length=300)
    adress=models.CharField(max_length=400)
    det=models.TextField()
    
    class Meta:
        verbose_name_plural="Experince"
        
    def __str__(self):
        return self.p_year
    
    
        


        