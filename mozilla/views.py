from django.shortcuts import render
from .models import Event

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def course(request):
    return render(request, 'course.html')

def deliverables(request):
    return render(request, 'deliverables.html')

def event(request):
    events = Event.objects.all() 
    return render(request, 'event.html', {'events': events}) 

def event_single(request):
    return render(request, 'event-single.html')

def projects(request):
    return render(request, 'projects.html')
