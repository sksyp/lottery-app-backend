from django.db import models

# Create your models here.
from user_dashboard.models import user_details


class lobby_details(models.Model):
    lobby_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    fee = models.FloatField(null=False)
    active = models.BooleanField(null=False, default=True)
    winner_user_id = models.ForeignKey(user_details, on_delete=models.SET_NULL, blank=True, null=True)
    revenue = models.FloatField(null=True)
    max_members_allowed = models.IntegerField(null=False, default=2)


class lobby_user_map(models.Model):
    user_id = models.ForeignKey(user_details, on_delete=models.CASCADE)
    lobby_id = models.ForeignKey(lobby_details, on_delete=models.CASCADE)


class user_winnings(models.Model):
    lobby_id = models.ForeignKey(lobby_details, on_delete=models.SET_NULL, null=True, blank=True)
    amount_won = models.FloatField(null=True)
