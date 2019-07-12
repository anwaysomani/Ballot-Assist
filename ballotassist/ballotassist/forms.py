from django import forms
from .models import ballot_record

class ballot_record(forms.ModelForm):
    class Meta:
        model = ballot_record
        fields = {'balloters_name', 'ballotees_name'}

