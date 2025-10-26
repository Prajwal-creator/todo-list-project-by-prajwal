from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class log(models.Model):

    srno=models.AutoField(auto_created=True,primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    ryzen=models.DateTimeField(default=datetime.now)

def __str__(self):
    return self.username
