from django.db import models
from django.utils import timezone
# Create your models here.
class Robot(models.Model):
    ID = models.IntegerField(primary_key=True)
    Black = models.IntegerField()
    White = models.IntegerField()

class Action(models.Model):
    ID = models.ForeignKey(Robot, on_delete=models.CASCADE)
    Action = models.CharField(max_length=256)
    Time = models.DateTimeField()
    def save(self, *args,**kwargs):
        if not self.id:
            self.Time = timezone.now()
        return super(Action,self).save(*args,**kwargs)

class Error(models.Model):
    ID = models.ForeignKey(Robot, on_delete=models.CASCADE)
    Error = models.CharField(max_length=256)
    Time = models.DateTimeField(auto_now_add=True)

class Active(models.Model):
    ID = models.ForeignKey(Robot, on_delete=models.CASCADE)
    Last = models.DateTimeField(auto_now=True)
