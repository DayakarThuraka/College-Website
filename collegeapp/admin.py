from django.contrib import admin
from .models import Branches

class AdminBranches(admin.ModelAdmin):
    list_display=['branch_name','fee','duration','start_year','passedout_year','typeof_college','location']

admin.site.register(Branches, AdminBranches)
