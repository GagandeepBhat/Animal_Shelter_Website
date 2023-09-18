from django.forms import ModelForm
from .models import AppliedAdoption
class AdoptionForm(ModelForm):
    class Meta:
        model=AppliedAdoption
        fields='__all__'