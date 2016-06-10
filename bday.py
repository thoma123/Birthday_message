import ctypes
import os
import winsound
import time
import subprocess
from datetime import date as date
user=ctypes.windll.User32
DESKTOP_SWITCHDESKTOP = 256
a=user.OpenDesktopA("default",0,False,DESKTOP_SWITCHDESKTOP)
bd=date.date(2016,1,8)
td=date.today()
while 1:
	if bd == td:
		break
	time.sleep(60)
while(1):
	c=user.SwitchDesktop(a)
	if(c == 0):
		break
while(1): 	
	c=user.SwitchDesktop(a)
	if(c != 0):
		break
list = ['thomasgeorge_c','aparna_s','sanjeev_s1','gopikavarma_k','randeepk','arunk','sinuwm','manuvivek','abhijith_sj','benwin_babu']
for ppl in list :
	subprocess.call(['C:/Users/thomasgeorge.c/Desktop/ip.exe','/MSG', ppl,'hiii'],shell=False)
time.sleep(5)
winsound.PlaySound('2.wav',1)
time.sleep(25)

