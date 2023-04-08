from django.db import models

# Create your models here.
class mission(models.Model):
    mission_title = models.CharField(max_length=300)
    mission_completed = models.BooleanField()
    
    
    def __str__(self):
        return self.mission_title
    


