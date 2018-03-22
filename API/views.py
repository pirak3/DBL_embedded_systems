from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from API.models import *
from django.utils import timezone
import datetime
from random import randint
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin
# Create your views here.
                                            #Defined what information we have of a robot
# class robot:
#     def __init__(self,Black,White,ID):
#          self.b = Black
#          self.w = White
#          self.ID = ID
#
#                                             #Test case
# prio = 1
# def Decision():
#     global prio
#     if prio % 2 == 1:
#         prio += 1
#         return 1
#     else:
#         prio += 1
#         return 2
#                                             #Ratio function
#                                             #We put in Multiple robots and it outputs the one with the highest priority for each color.
# def Ratio(ratio):
#                                             #Start values defined
#     bratio = 0
#     wratio = 0
#     bprio = ['Black',0]
#     wprio = ['White',0]
#                                             #Start looping through all robots
#     for r in ratio:
#         b = r.b / r.w                       #Define black ratio
#         if b > bratio:                      #Check if ratio is higher then highest
#             bratio = b                      #Modify if this is the case
#             bprio[1]=r.ID                   #Modify ID of the robot with the Highest ID
#
#         w=r.w/r.b                           #Define black ratio
#         if w > wratio:                      #Check if ratio is higher then highest
#             wratio = w                      #Modify highest if this is the case
#             wprio[1]=r.ID                   #Modify ID of the robot with the Highest ID
#         elif w == wratio and b == bratio:
#             x = Decision()
#             print(x)
#             wprio[1]=x
#             bprio[1]=x
#     Priority = [bprio,wprio]                #put the answers in a list
#     return Priority                         #Return said list


class RobotList(APIView):
    def get(self,request,format=None):
        Robots=Robot.objects.all()
        serializer=RobotSerializer(Robots, many=True)
        return Response(serializer.data)


    def post(self,request):
        print(request)
        serializer=RobotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status =status.HTTP_400_BAD_REQUEST)

class ActionList(APIView):
    def get(self,request):
        Actions = Action.objects.all()
        serializer = ActionSerializer1(Actions, many= True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.Time = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ErrorList(APIView):
    def get(self,request):
        Errors = Error.objects.all()
        serializer = ErrorSerializer1(Errors, many= True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ErrorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)