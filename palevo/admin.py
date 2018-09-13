from django.contrib import admin
from .models import Group, Solution, User, Teacher, Subject, Semester


admin.site.register(Group)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Solution)
admin.site.register(User)
