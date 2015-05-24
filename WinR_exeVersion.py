import os

def createReg():
	header = 'Windows Registry Editor Version 5.00'
	regPath = '[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths]'

	#get user input
	print "Enter name of .exe file in this folder."
	print "Exmaple: chrome.exe"
	exePath = raw_input("> ")
	callName = raw_input("Enter the name you want to call this program with > ")
	os.chdir('..')
	containPath = os.getcwd()
	exePath = os.getcwd() + '\\' + exePath

    #edit input strings
	editCallName = "[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\\" + callName + ".exe]"
	editExePath = "@=" + '"' + exePath + '"'
	editContainPath = '"Path"=' + '"' + containPath + '"'
	editExePath = editExePath.replace("\\", "\\\\")
	editContainPath = editContainPath.replace("\\", "\\\\")

	#write edited input to .reg file
	filename = callName + '.reg'
	target = open(filename, 'w')
	target.write(header + '\n')
	target.write(regPath + '\n')
	target.write(editCallName + '\n')
	target.write(editExePath + '\n')
	target.write(editContainPath)
	target.close()
	os.startfile(filename)
	return;

createReg()
