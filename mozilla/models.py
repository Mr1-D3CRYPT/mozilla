from django.db import models
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True 

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/') 
    description = models.TextField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, related_name="registration")
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    country_code = models.CharField(max_length=5, default="+91")
    institution = models.CharField(max_length=255)
    selected_events = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=255, unique=True)
    payment_status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.payment_id}"
   
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) 
    sections = models.JSONField() 
    duration = models.CharField(max_length=50)  
    eligibility = models.CharField(max_length=255)
    syllabus = models.FileField(upload_to='syllabus/') 
    availability_status = models.CharField(max_length=255, default="Course will be available soon.") 

    def __str__(self):
        return self.name   

class Deliverable(models.Model):
    title = models.CharField(max_length=255, default="Deliverables")
    items = models.JSONField() 

    def __str__(self):
        return self.title

class CurriculumInclusion(models.Model):
    title = models.CharField(max_length=255, default="Curriculum Inclusion")
    items = models.JSONField()  

    def __str__(self):
        return self.title
    
class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/') 

    def __str__(self):
        return self.name
