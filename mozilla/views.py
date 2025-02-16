from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def course(request):
    return render(request, 'course.html')

def deliverables(request):
    return render(request, 'deliverables.html')

def event(request):
    return render(request, 'event.html')

def event_single(request):
    return render(request, 'event-single.html')

def projects(request):
    return render(request, 'projects.html')
