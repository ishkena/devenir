from django.contrib import admin
from .models import Book, Case, Skill, Case_Skill, User, Interview, Interviewee, Interviewer
admin.site.register(Book)
admin.site.register(Case)
admin.site.register(Skill)
admin.site.register(Case_Skill)
admin.site.register(User)
admin.site.register(Interview)
admin.site.register(Interviewee)
admin.site.register(Interviewer)

# Register your models here.
