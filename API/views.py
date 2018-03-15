from django.shortcuts import render
from models import *
# Create your views here.
                                            #Defined what information we have of a robot
class robot:
    def __init__(self,Black,White,ID):
         self.b = Black
         self.w = White
         self.ID = ID

                                            #Test case
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
        b = r.b / r.w                       #Define black ratio
        if b > bratio:                      #Check if ratio is higher then highest
            bratio = b                      #Modify if this is the case
            bprio[1]=r.ID                   #Modify ID of the robot with the Highest ID

        w=r.w/r.b                           #Define black ratio
        if w > wratio:                      #Check if ratio is higher then highest
            wratio = w                      #Modify highest if this is the case
            wprio[1]=r.ID                   #Modify ID of the robot with the Highest ID
        elif w == wratio and b == bratio:
            x = Decision()
            print(x)
            wprio[1]=x
            bprio[1]=x
    priority = [bprio,wprio]                #put the answers in a list
    return Priority                         #Return said lis

def Action(self,):
    return 0