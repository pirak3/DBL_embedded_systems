from rest_framework import serializers
from .models import *

#Translators for Action Model. First one for posting and last one for retrieving
class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields=('ID','Action')

class ActionSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields=('ID','Action','Time')
#Translators for Error Model. First one for posting and last one for retrieving
class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields='__all__'

class ErrorSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields=('ID','Error','Time')
#Translator for robot model
class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model= Robot
        fields = '__all__'

class RobotUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ['Black','White']


class priorityserializer(serializers.Serializer):
    ID = serializers.IntegerField()
    Color = serializers.CharField(max_length=10)
