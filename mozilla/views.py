from django.http import JsonResponse
from django.shortcuts import render
from .models import CurriculumInclusion, Deliverable, Event, Project, Course, TeamMember, Registration
import json

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

def registration(request):
    return render(request, 'registration.html')

def place_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Received Data:", data)  # Debugging

            # Extract data
            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            country_code = data.get("country_code")
            institution = data.get("institution")
            selected_events = ", ".join(data.get("selected_events", []))  
            total_amount = data.get("total_amount")
            payment_id = data.get("payment_id")

            # Save to database
            new_registration = Registration.objects.create(
                name=name,
                email=email,
                phone=phone,
                country_code=country_code,
                institution=institution,
                selected_events=selected_events,
                total_amount=total_amount,
                payment_id=payment_id,
                payment_status="Success"
            )

            print("✅ Registration saved successfully!")

            return JsonResponse({
                "status": "success",
                "message": "Registration Successful!",
                "redirect_url": "/event-single/"  # Redirect directly to event page
            })

        except Exception as e:
            print("❌ Error:", e)  # Debugging
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)



def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
