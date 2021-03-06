#!/usr/bin/python
# _*_ coding: utf-8 -*-


import time
import RobotApi

RobotApi.ubtRobotInitialize()
#------------------------------Connect----------------------------------------
gIPAddr = ""

robotinfo = RobotApi.UBTEDU_ROBOTINFO_T()
#The robot name you want to connect
robotinfo.acName="Yanshee_8F83"
ret = RobotApi.ubtRobotDiscovery("SDK", 15, robotinfo)
if (0 != ret):
	print ("Return value: %d" % ret)
	exit(1)

gIPAddr = robotinfo.acIPAddr
ret = RobotApi.ubtRobotConnect("SDK", "1", gIPAddr)
if (0 != ret):
	print ("Can not connect to robot %s" % robotinfo.acName)
	exit(1)

#--------------------------Test servo 6------------------------------------

servoinfo = RobotApi.UBTEDU_ROBOTSERVO_T()
servoinfo.SERVO2_ANGLE = 60
servoinfo.SERVO3_ANGLE = 40
ret = RobotApi.ubtSetRobotServo(servoinfo, 20)


#--------------------------DisConnection--------------------------------- 
RobotApi.ubtRobotDisconnect("SDK","1",gIPAddr)
RobotApi.ubtRobotDeinitialize()

