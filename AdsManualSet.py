import MySQLdb as mdb
import time
import webbrowser

import subprocess
import os


#con = mdb.connect('localhost', 'root' , ' ', 'AdsLocations')
con = mdb.connect('192.168.1.5', 'root' , ' ', 'AdsLocations')
while True:
 #x= 30.19 #Kafr ElDawar
 #y= 31.12
 x=29.94145
 y=31.21939 #Smouha SidiGaber
 #x=29.90421
 #y=31.204024        #Raml
 cur = con.cursor()
 cur.execute("SELECT AdPicture FROM Ads WHERE AreaID  in ( SELECT AreaID FROM AdsAreas WHERE %s > StartLongitude AND %s < EndLongitude  AND %s > StartLatitude AND %s < EndLatitude )",(x,x,y,y))
 #m=0
 for i in range(cur.rowcount):
        row = cur.fetchone()
        p=subprocess.Popen(["eog","-f",row[0]])
	time.sleep(5)
	p.kill()
        #if m==1:
          #z.kill()
          #m=0
        #row = cur.fetchone()
        #z=subprocess.Popen(["eog","-f",row[0]])
        #time.sleep(2)
	 #if m==0:
         # p.kill()
         # m=1
