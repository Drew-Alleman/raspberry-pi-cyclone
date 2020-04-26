import  RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinOUT = [13,26,19,16,20,21,12]
pinIN = 18

easy_time = .1
medium_time = .05
hard_time = .03

def PinSetup():
	for pin in pinOUT:
		GPIO.setup(pin,GPIO.OUT)
	GPIO.setup(pinIN,GPIO.IN)

def blinkLED(pin):
	count = 0
	while count <= 6:
		t.sleep(.1)
		GPIO.output(pin,True)
		t.sleep(.1)
		GPIO.output(pin,False)
		count+=1
	exit()

def game():
	print(
'''
Select Your Difficulty
[1] --> Easy
[2] --> Meduim
[3] --> Hard
''')
	difficulty = input(">> ")
	if difficulty == "1":
		time = easy_time
	elif difficulty == "2":
		time = medium_time
	elif difficulty == "3":
		time = hard_time
	else:
		time = easy_time
	while True:
		for pin in pinOUT:
			GPIO.output(pin,True)
			if GPIO.input(pinIN) == 0:
				blinkLED(pin)
			t.sleep(time)
			GPIO.output(pin,False)
		pinOUT.reverse()

PinSetup()
game()
