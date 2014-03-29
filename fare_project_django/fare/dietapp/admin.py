from django.contrib import admin
from dietapp.models import Ingredient,Recipe,Diet,DietsCombinations,DietsUser

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Diet)
admin.site.register(DietsCombinations)
admin.site.register(DietsUser)