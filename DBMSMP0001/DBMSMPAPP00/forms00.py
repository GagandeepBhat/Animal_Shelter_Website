from django.forms import ModelForm
from .models import AppliedVolunteering
class VolunteeringForm(ModelForm):
    class Meta:
        model=AppliedVolunteering
        fields='__all__'