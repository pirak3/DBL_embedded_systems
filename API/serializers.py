from rest_framework import serializers
from .models import *

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields=('ID','Action')

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model= Robot
        fields = '__all__'