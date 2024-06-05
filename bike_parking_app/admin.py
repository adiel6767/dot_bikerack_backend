from django.contrib import admin
from .models import User,BikeRackData,Achievements,Badge

# Register your models here.
admin.site.register(User)
admin.site.register(BikeRackData)
admin.site.register(Achievements)
admin.site.register(Badge)

