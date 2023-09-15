from django import forms
from app.models import Ticket, Category

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['description','place','price','date_ajout','expiration','categorie','image','status']
        widgets = {
          'categorie': forms.Select(attrs={'class': 'form-control'}),
          'description': forms.TextInput(attrs={'class': 'form-control'}),
          'place': forms.TextInput(attrs={'class': 'form-control'}),
          'price': forms.TextInput(attrs={'class': 'form-control'}),
          'image': forms.FileInput(attrs={'class': 'form-control'}),
           'expiration': forms.DateInput(attrs={'class': 'form-control','min': '2023-01-01','type':'date'}),
           'date_ajout': forms.DateInput(attrs={'class': 'form-control','min': '2023-01-01','type':'date'}),
        }