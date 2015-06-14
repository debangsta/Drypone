import subprocess
import RPI.GPIO as GPIO
from pygame import mixer

#init
status = "OK"
mixer.init()
red= int(11)
green= int(15)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.output(red,GPIO.LOW)
GPIO.output(green, GPIO.HIGH)

#infinite loop so that sensor is always polling
infinite = "inf"
while infinite =="inf":
#loop to poll pcsc_scan every second
		while status=="OK" :
				buf =subprocess.Popen("timeout is pcsc_scan",stdout= subprocess.PIPE, shell=True)
				
				(output, err) = buf.communicate()
				
				det = "Card inserted"
				
				txt = str(output)
				
				if det in output:
						status = "Warning!"
						
				print "="
		#outputs when item detected
		print status,"Item Detected"
		GPIO.output(red,GPIO.HIGH)
		GPIO.output(green, GPIO.LOW)
		
		while status == "Warning!" :
				subprocess.call(["aplay","police_s.wav"])
				det2= "Card removed"
				
				buf= subprocess.Popen("timeout is pcsc_scan", stdout=subprocess.PIPE, shell=True)
				(output,err)= buf.communicate()
				
				if det2 in output:
						status = "OK"
				GPIO.output(red,GPIO.LOW)
				GPIO.output(green,GPIO.HIGH)