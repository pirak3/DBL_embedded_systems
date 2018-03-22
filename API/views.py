from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from API.models import *
from django.utils import timezone
from django.http import Http404
from django.utils.six import BytesIO
import datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
                                            #Defined what information we have of a robot



class RobotList(APIView):
    def get(self,request,format=None):
        Robots=Robot.objects.all()
        serializer=RobotSerializer(Robots, many=True)
        return Response(serializer.data)
    def post(selfs, request):
        serializer = RobotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RobotAdd(APIView):
    def get_object(self, pk):
        try:
            return Robot.objects.get(pk=pk)
        except Robot.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        Rob = self.get_object(pk)
        serializer = RobotUpdateSerializer(Rob, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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

class robotratio:
    def __init__(self,Black,White,ID):
         self.ID = ID
         self.b = Black
         self.w = White
class decis:
    def __init__(self,ID,Decision):
        self.ID = ID
        self.decision = Decision

def get_robot():
    r1 = Robot.objects.get(pk=1)
    r2 = Robot.objects.get(pk=2)
    ratio = [robotratio(r1.ID,r1.Black,r1.White),robotratio(r2.ID,r2.Black,r2.White)]
    return ratio
prio = 1
def Decision():
    global prio
    if prio % 2 == 1:
        prio += 1
        return 1
    else:
        prio += 1
        return 2
                                            #Ratio function
                                            #We put in Multiple robots and it outputs the one with the highest priority for each color.
def Ratio(ratio):
                                            #Start values defined
    bratio = 0
    wratio = 0
    bprio = ['Black',0]
    wprio = ['White',0]
                                            #Start looping through all robots
    for r in ratio:
        if r.b == 0:
            wratio=10
            wprio[1]=r.ID
        elif r.w == 0:
            bratio=10
            bprio[1]=r.ID
        else:
            try:
                b = r.b / r.w#Define black ratio
                if b > bratio:  # Check if ratio is higher then highest
                    bratio = b  # Modify if this is the case
                    bprio[1] = r.ID

                w=r.w/r.b #Define black ratio
                if w > wratio:  # Check if ratio is higher then highest
                    wratio = w  # Modify highest if this is the case
                    wprio[1] = r.ID  # Modify ID of the robot with the Highest ID
                elif w == wratio and b == bratio:
                    x = Decision()
                    print(x)
                    wprio[1] = x
                    bprio[1] = x
                print(bprio,wprio)
            except ZeroDivisionError:
                print('divided by zero')
                           #Modify ID of the robot with the Highest ID

    Priority = [bprio,wprio]                #put the answers in a list
    return Priority                         #Return said list

class Priority(APIView):
    def post(self, request):
        priorities=Ratio(get_robot())
        inserializer = priorityserializer(data=request.data)
        if inserializer.is_valid():
            myDict=dict(request.data)
            if myDict['Color'] == ['Black']:
                if myDict['ID'][0] == str(priorities[0][1]):
                    return Response(1,status=status.HTTP_200_OK)
                else:
                    return Response(0, status=status.HTTP_200_OK)
            elif myDict['Color'] == ['White']:
                if myDict['ID'][0] == str(priorities[1][1]):
                    return Response(1, status=status.HTTP_200_OK)
                else:
                    return Response(0, status=status.HTTP_200_OK)
        return Response('Error',status=status.HTTP_500_INTERNAL_SERVER_ERROR)
