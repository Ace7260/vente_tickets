from django.db import models
from .user import User
from .ticket import Ticket
class User_ticket(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, blank=True, null=True)
 