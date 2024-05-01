from django.contrib import admin
from .models import Course, Lecture, Assignment, Submission

# Register your models here.
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Assignment)
admin.site.register(Submission)