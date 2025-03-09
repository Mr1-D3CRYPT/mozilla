from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("about", views.about, name="about"),
    path("course", views.course, name="course"),
    path("deliverables", views.deliverables, name="deliverables"),
    path("event", views.event, name="event"),
    path("event-single", views.event_single, name="event_single"),
    path("projects", views.projects, name="projects"),
    path("registration", views.registration, name="registration"),
    path('place-order', views.place_order, name='place-order'),
    path('create_account', views.create_account, name='create_account'),
    path("account", views.account, name="account"),
    path("logout_view", views.logout_view, name="logout"),
    path("login_view", views.login_view, name="login"),
]
