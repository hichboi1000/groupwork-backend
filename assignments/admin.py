from django.contrib import admin
from .models import Unit, Assignment, GroupAssignment, Submission

admin.site.register(Unit)
admin.site.register(Assignment)
admin.site.register(GroupAssignment)
admin.site.register(Submission)