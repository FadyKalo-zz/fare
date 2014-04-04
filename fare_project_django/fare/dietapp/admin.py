from django.contrib import admin
from dietapp.models import UserProfile, RecipeActivity, ActivityEvent, ActivityType

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(RecipeActivity)
admin.site.register(ActivityType)
admin.site.register(ActivityEvent)