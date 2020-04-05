Data = {'gH':0,'bH':0,'gR':0,'bR':0,'rW':0,'yW':0,'rD':0,'yD':0}
Robot = {'pos':0, 'start':0, 'line':0}
Finish = []
Tray = []
LeftMotor = RightMotor = RightFloor=LeftFloor=ColorSight=Grabber=Lifter= None


from function import *

def runTime():
	LeftWheel = LargeMotor()
	LeftFloor = ColorSensor()
	RightWheel = LargeMotor()
	RightFloor = ColorSensor()
	Sight = Sensor(driver='ht-nxt-color-v2',address='')
	Grabber = ServoMotor()
	Lifter = ServoMotor()
	
	

### Start of Run ###

#runTime()
setHouse(1,3)