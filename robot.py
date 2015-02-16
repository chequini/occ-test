## Sergio Roman Iturbe
## Feb 15, 2015

import pygame
import sys
import os.path
import re

class Robot:
	
	# Valid commands
	PLACE_CMD     = "PLACE"
	MOVE_CDM      = "MOVE"
	REPORT_CMD	  = "REPORT"
	TURN_LEFT     = "LEFT"
	TURN_RIGHT    = "RIGHT"
	ORIENTATION_N = "NORTH"
	ORIENTATION_S = "SOUTH"
	ORIENTATION_E = "EAST"
	ORIENTATION_W = "WEST"
	VALIDORIENTATIONS = [ORIENTATION_N,ORIENTATION_E,ORIENTATION_S,ORIENTATION_W]
	
	# Error message type
	LEVEL_INFO    = ["_INFO__",1]
	LEVEL_WARNING = ["WARNING",2]
	LEVEL_ERROR   = ["_ERROR_",3]
	
	# Error Level
	SHOW_ALL      = 3
	SHOW_WARNINGS = 2
	SHOW_INFO     = 1
	NO_SHOW		  = 0
	
	# Attributes
	isPlaced    = False
	orientation = None
	debugLevel  = None
	position    = {"x":None,"y":None}
	tableDimen  = {"w":5,"h":5} 				# Width,Height
	lineNo		= None
	
	def __init__(self,debugLevel = 0):
		self.debugLevel = debugLevel
	
	def checkNumber(self,number):
		try:
			return int(number)
		except ValueError:
			return -1
	
	def validPosition(self,nextPosition):
		if nextPosition["x"] < 0 or nextPosition["x"] >= self.tableDimen["w"]:
			return False
		if nextPosition["y"] < 0 or nextPosition["y"] >= self.tableDimen["h"]:
			return False
		return True
	
	def validOrientation(self,orientation):
		if orientation not in self.VALIDORIENTATIONS:
			return False
		return True
	
	def place(self,x,y,orientation):
		posX = self.checkNumber(x)
		posY = self.checkNumber(y)
		if posX == -1:
			self.error(self.LEVEL_WARNING,"05","Invalid X input ("+str(x)+"), an integer value is required, the command was ignored")
			return None			
		if posY == -1:
			self.error(self.LEVEL_WARNING,"06","Invalid Y input ("+str(y)+"), an integer value is required, the command was ignored")
			return None
		if not self.validOrientation(orientation):
			self.error(self.LEVEL_WARNING,"07","Invalid Orientation input ("+str(orientation)+"), the command was ignored")
			return None
		tmp_position = {"x":posX,"y":posY}
		if self.validPosition(tmp_position):
			self.position = tmp_position
			self.orientation = orientation
			self.isPlaced = True
		else:
			self.error(self.LEVEL_INFO,"08","Invalid new position, the command was ignored")
			return None
			
	def move(self):
		if self.orientation == self.ORIENTATION_N:
			nextPosition = {"x":self.position["x"],"y":self.position["y"]+1}			
		elif self.orientation == self.ORIENTATION_S:
			nextPosition = {"x":self.position["x"],"y":self.position["y"]-1}
		elif self.orientation == self.ORIENTATION_E:
			nextPosition = {"x":self.position["x"]+1,"y":self.position["y"]}
		elif self.orientation == self.ORIENTATION_W:
			nextPosition = {"x":self.position["x"]-1,"y":self.position["y"]}
			
		if self.validPosition(nextPosition):
			self.position = nextPosition
		else:
			self.error(self.LEVEL_INFO,"08","Invalid new position, the command was ignored")
	
	def rotate(self,movement):
		index = self.VALIDORIENTATIONS.index(self.orientation)
		if movement == self.TURN_LEFT:
			factor = -1 
		elif movement == self.TURN_RIGHT:
			factor = +1
		else:
			self.error(self.LEVEL_INFO,"09","Invalid new orientation, the command was ignored")	
			return None
		newIndex = index + factor
		newIndex = 3 if newIndex == -1 else newIndex
		newIndex = 0 if newIndex == 4 else newIndex
		self.orientation = self.VALIDORIENTATIONS[newIndex]
		
	def report(self):
		print self.position["x"],self.position["y"],self.orientation
	
	def loadFile(self,filePath):
		self.lineNo = 1
		if os.path.isfile(filePath):
			file = open(filePath, 'r')
			for line in file:
				self.lineProcessor(line)
				self.lineNo = self.lineNo + 1
		else:
			self.error(self.LEVEL_ERROR,"01","File does not exists")
			
	def checkPlace(self,command):
		if not self.isPlaced:
			self.error(self.LEVEL_INFO,"03","There is not a robot placed in the table, the command '"+command+"' was ignored")
			return False
		return True
		
	def dataSanitizer(self,data):
		tmp_data = data.replace('\n','');
		tmp_data = tmp_data.replace('\t','');
		tmp_data = tmp_data.replace(' ','');
		return tmp_data
		
	def lineProcessor(self,line):
		re.sub( '\s+', ' ', line ).strip()
		tokens = line.split(' ');
		keyCommand = self.dataSanitizer(tokens[0])
		if keyCommand == self.PLACE_CMD:
			params = self.dataSanitizer(tokens[1])
			params = params.split(',')
			if len(params) == 3:
				self.place(params[0],params[1],params[2])
			else:
				self.error(self.LEVEL_WARNING,"04","Invalid number of parameters passed by PLACE command, 3 expected")
		elif keyCommand == self.MOVE_CDM:
			if self.checkPlace(keyCommand):
				self.move()
		elif keyCommand == self.TURN_LEFT or keyCommand == self.TURN_RIGHT :
			if self.checkPlace(keyCommand):
				self.rotate(keyCommand)
		elif keyCommand == self.REPORT_CMD:
			if self.checkPlace(keyCommand):
				self.report()
		else:
			self.error(self.LEVEL_WARNING,"02","Invalid command '"+keyCommand+"'")
	
	def error(self,level,code,description):
		if self.lineNo is not None :
			_line = "Line:"+str(self.lineNo)
		if level[1] <= self.debugLevel:
			print "[",level[0]," Code:"+str(code)+" "+_line+"]:",description
	
def main(argv):	
	robot = Robot(3)
	if len(argv) == 2 :
		filePath = argv[1]
		robot.loadFile(filePath)
	else:
		print "\tUsage: python robot.py [CommandFile]"		
	
if __name__ == '__main__':
	main(sys.argv)
	
