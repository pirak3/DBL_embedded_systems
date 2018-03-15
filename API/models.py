from django.db import models

# Create your models here.
class Robot(models.model):
    ID = models.IntegerField(primary_key=True)
    Black = models.IntegerField()
    White = models.IntegerField()

class Action(models.model):
    ID = models.ForeignKey(Robot, on_delete=models.CASCADE)
    Action = models.CharField(max_length=256)
    Time = models.DateTimeField(auto_now_add=True)

class Error(models.model):
    ID = models.ForeignKey(Robot, on_delete=models.CASCADE)
    Error = models.Charfield(max_length=256)
    Time = models.DateTimeField(auto_now_add=True)

class Active(models.model):
    ID = models.ForeignKey(Robot, on_delete=models.CASCADE)
    Last = models.DateTimeField(auto_now=True)
