#resume_upload
from django.db import models


STATE_CHOICE = (
    (
        ('mp','mp'),
        ('up','up'),
        ('cg','cg'),
        ('gujrat','gujrat'),
        ('punjab','punjab')
    )
)

class Person(models.Model):
    person_name = models.CharField(max_length=300)
    person_email = models.EmailField(max_length=300)
    person_dob_time = models.DateTimeField(auto_now=False,auto_now_add=False)
    person_state = models.CharField(max_length=200)
    person_gender = models.CharField(max_length=200)
    person_location = models.CharField(max_length=300)
    person_image = models.ImageField(upload_to = 'image',blank=True)
    person_document = models.FileField(upload_to='document',blank=True)
    