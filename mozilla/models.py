from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/') 
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country_code = models.CharField(max_length=5, default="+91")
    institution = models.CharField(max_length=255)
    selected_events = models.TextField()  # Stores selected events
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=255, unique=True)
    payment_status = models.CharField(max_length=20, default="Pending")  # Can be "Success" or "Failed"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.payment_id}"

    
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
