from ev3dev import *
from ev3dev2.led import Leds
from ev3dev2.button import*
from ev3dev2.motor import *
from ev3dev2.sensor.lego import ColorSensor,GyroSensor
from ev3dev2.sensor import Sensor
from __main__ import *
from cross import *
from direct import *



def setWheel(L,R):
	global LeftMotor,RightMotor
	LeftMotor = 12
	print(LeftMotor)
	#LargeMotor(L)
	#RightMotor = LargeMotor(R)

def setSensor(GyroSensor,Hitechnic):
	global Gyro,ColorSight
	Gyro = GyroSensor(GyroSensor)
	ColorSight = Sensor(driver='ht-nxt-color-v2',address=Hitechnic)
	
def setFloor(L,R):
	global LeftFloor,RightFloor
	LeftFloor = ColorSensor(L)
	RightFloor = ColorSensor(R)

def setHouse(gH,bH):
	global Data
	Data['gH'] = gH
	Data['bH'] = bH

def turn(side):
	if side == 'Left':
		print(side)
		#Left
	elif side == 'Right':
		print(side)
		#Right
	else :
		print('Turn Around!')
		#180 Degree

def walk(*args,**kwargs):
	color = kwargs.get('c',None)
	time = kwargs.get('t',None)
	distance = kwargs.get('d',None)
	
	if color.__class__ == str :
		print('Both Color : {}'.format(color))
		
	elif color.__class__ == list :
		print('Left : {}  Right : {}'.format(color[0],color[1]))
		
	pass
	
	
	
	if time.__class__ == int :
		print('Time : ',time)
		
		
	
	if distance.__class__ == int :
		print('Distance : ',distance)
		
		
	pass

def setPos(pos):
	pos1 = Robot['pos']
	pos2 = pos
	return pos1,pos2
	
	
def dCheck(pos):
	pos1,pos2 = setPos(pos)
	if pos1:
		if (pos1+pos2)%5:
			if (pos1+pos2)%2:
				return 1
			else:
				return 3
		else:
			return 2
	else:
		return 0
def go(pos):
	distance = dCheck(pos)
	print(distance)
	cal = bool(pos%2)
	side = ['Left','Right']
	if distance==0 :
		turn(side[pos<3])
		turn(side[cal])
	elif distance==1:
		turn('Through')
		#Walk Through
	elif distance==2:
		turn(side[cal])
		#Walk
		turn(side[cal])
	elif distance==3:
		turn(side[not(cal)])
		#Walk
		turn(side[cal])

