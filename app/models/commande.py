from django.db import models
from .user import User
class Commande(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True) 
    status = models.CharField(max_length=200, null=True, blank=True)
    total_trans = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)  
    
    @property 
    def get_panier_total(self):
        """ prix total des articles dans le panier"""
        commande_ticket= self.commande_ticket_set.all()
        total = sum([ticket.get_total for ticket in commande_ticket])
        return total  

    @property
    def get_panier_article(self):
        """ Nombre total des articles dans le panier"""
        commande_ticket = self.commande_ticket_set.all()
        quantite_total = sum([ticket.quantite for ticket in commande_ticket])
        return quantite_total

