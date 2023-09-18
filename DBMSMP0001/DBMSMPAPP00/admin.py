from django.contrib import admin
from .models import Feature
from .models import Animal_Shelters
from .models import Adoption
from .models import AppliedAdoption
from .models import Volunteering
from .models import AppliedVolunteering

# Register your models here.
admin.site.register(Feature)
admin.site.register(Animal_Shelters)
admin.site.register(Adoption)
admin.site.register(AppliedAdoption)
admin.site.register(Volunteering)
admin.site.register(AppliedVolunteering)