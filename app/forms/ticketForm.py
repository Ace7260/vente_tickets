from django import forms
from app.models import Ticket, Category

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"
        widgets = {
          'categorie': forms.Select(attrs={'class': 'form-control'}),
          'description': forms.TextInput(attrs={'class': 'form-control'}),
          'place': forms.TextInput(attrs={'class': 'form-control'}),
          'price': forms.TextInput(attrs={'class': 'form-control'}),
          'image': forms.FileInput(attrs={'class': 'form-control'}),
          'status': forms.CheckboxInput(attrs={'class': 'checkbox'}),
          'expiration': forms.DateTimeInput(attrs={'class': 'form-control'}),
          }