from django.contrib import admin
from dietapp.models import UserProfile, RecipeActivity, ActivityEvent, ActivityType,Diet,DietUser

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(RecipeActivity)
admin.site.register(ActivityType)
admin.site.register(ActivityEvent)
admin.site.register(Diet)
admin.site.register(DietUser)