from django.db import models


# Create your models here.


class user_details(models.Model):
    user_id = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    admin = models.BooleanField(default=False, null=False)



