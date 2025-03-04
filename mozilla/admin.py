from django.contrib import admin
from .models import Event,Project,Course,Deliverable,CurriculumInclusion,TeamMember,Registration

admin.site.register(Event)
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Deliverable)
admin.site.register(CurriculumInclusion)
admin.site.register(TeamMember)
admin.site.register(Registration)