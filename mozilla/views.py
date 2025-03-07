from django.http import JsonResponse
from django.shortcuts import render
from .models import CurriculumInclusion, Deliverable, Event, Project, Course, TeamMember, Registration
import json
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def place_order(request):
    if request.method == "POST":
        try:
            # Read JSON data from request body
            data = json.loads(request.body)

            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            country_code = data.get("country_code", "+91")
            institution = data.get("institution")
            selected_events = ", ".join(data.get("selected_events", []))
            total_amount = data.get("total_amount")
            payment_id = data.get("payment_id")

            # Ensure all required fields are received
            if not all([name, email, phone, institution, selected_events, total_amount, payment_id]):
                return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)

            # Store in the database
            registration = Registration.objects.create(
                name=name,
                email=email,
                phone=phone,
                country_code=country_code,
                institution=institution,
                selected_events=selected_events,
                total_amount=total_amount,
                payment_id=payment_id,
                payment_status="Paid"
            )

            # Construct the email message
            subject = "NCEDA 2025 - Registration Confirmation"
            message = f"""
            Dear {name},

            Thank you for registering for NCEDA 2025. Your payment has been successfully processed.

            Details:
            - Name: {name}
            - Email: {email}
            - Phone: {country_code} {phone}
            - Institution: {institution}
            - Selected Events: {selected_events}
            - Total Amount Paid: ₹{total_amount}
            - Payment ID: {payment_id}

            We look forward to seeing you at the event!

            Best Regards,  
            NCEDA 2025 Team
            """
            from_email = "ashish.23pmc111@mariancollege.org"
            recipient_list = [email]

            # Send confirmation email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Return JSON response with redirect URL
            return JsonResponse({
                "status": "success",
                "message": "Order placed and confirmation email sent!",
            })

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
