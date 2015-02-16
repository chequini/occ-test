import sys
import os

base = "./tests/"

testCases = [
		["Test-01","Generic test 1 (Example 1)",base+"test1"],
		["Test-02","Generic test 2 (Example 2)",base+"test2"],
		["Test-03","Generic test 3 (Example 3)",base+"test3"],
		["Test-04","The robot is not placed",base+"test4"],
		["Test-05","Invalid command in file",base+"test5"],
		["Test-06","Invalid number of paramenters in PLACE command",base+"test6"],
		["Test-07","Invalid place inputs",base+"test7"],
		["Test-08","Invalid new position after PLACE or MOVE",base+"test8"],
		["Test-09","Multiple PLACE command and movements",base+"test9"],
	]

def main():	
	print "Running test cases:\n"
	for tc in testCases:
		print "::::::::::::::: "+str(tc[0])+" ::::::::::::::::"
		print "Description: "+str(tc[1])+"\n"
		print ">> Input <<"
		with open(str(tc[2]), 'r') as fin:
			print fin.read()
		print "<< Output >>"
		os.system("python robot.py "+str(tc[2]))
		print "\n::::::::::::::::::::::::::::::::::::::::\n"	
	
if __name__ == '__main__':
	main()
