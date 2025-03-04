from django.shortcuts import render
from .models import CurriculumInclusion, Deliverable, Event,Project,Course, TeamMember

def index(request):
    team_members = TeamMember.objects.all()
    return render(request, 'index.html', {'team_members': team_members})

def about(request):
    return render(request, 'about.html')

def deliverables(request):
    deliverables = Deliverable.objects.first()
    curriculum_inclusion = CurriculumInclusion.objects.first()

    deliverables_list = deliverables.items if deliverables else []
    curriculum_list = curriculum_inclusion.items if curriculum_inclusion else []

    return render(request, 'deliverables.html', {
        'deliverables': deliverables_list,
        'curriculum_inclusion': curriculum_list
    })


def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

def event(request):
    events = Event.objects.all() 
    return render(request, 'event.html', {'events': events}) 

def event_single(request):
    return render(request, 'event-single.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
