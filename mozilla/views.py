from django.http import JsonResponse
from .models import CurriculumInclusion, Deliverable, Event, Project, Course, TeamMember, Registration
import json
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    registrations = Registration.objects.filter(username=request.user) if request.user.is_authenticated else []
    return render(request, 'event-single.html', {'registrations': registrations})


@login_required(login_url='/login_view')
def registration(request):
    return render(request, 'registration.html',{'user_email': request.user.email})

@login_required(login_url='/login_view')
def account(request):
        try:
            registration = Registration.objects.filter(username=request.user)
        except Registration.DoesNotExist:
            registration = None

        return render(request, "account.html", {
            "registration": registration,
            "user": request.user 
        })


def logout_view(request):
    logout(request)
    return redirect("create_account")


def create_account(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already taken. Please choose another one.")
            return render(request, "create_account.html")
   
        else: 
            user = User.objects.create_user(username=name, email=email, password=password)
            login(request, user)

            return redirect("account") 

    return render(request, "create_account.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("account")  
        else:
            messages.error(request, "Incorrect username or password. Please try again.")
            return redirect("create_account") 

    elif request.user.is_authenticated:
        return redirect("account")

    else:
        messages.error(request, "You must logged-in to proceed!")
        return redirect("create_account")  

@csrf_exempt
@login_required(login_url='/login_view')
def place_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))

            name = data.get("name")
            phone = data.get("phone")
            country_code = data.get("country_code", "+91")
            institution = data.get("institution")
            selected_events = ", ".join(data.get("selected_events", []))
            total_amount = data.get("total_amount")
            payment_id = data.get("payment_id")

            user = request.user
            email = user.email 

            # Ensure all required fields are received
            if not all([name, phone, institution, selected_events, total_amount, payment_id]):
                return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)

            # Store in the database
            Registration.objects.create(
                username=user,
                name=name,
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
