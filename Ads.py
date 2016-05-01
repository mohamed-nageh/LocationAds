from gps import *
import os
import MySQLdb as mdb
import time
import subprocess


#x=30.196601833
#y=31.131138833
#y=31.219
#print (gvar)
#print(x)
#print(y)

con = mdb.connect('localhost', 'root' , ' ', 'AdsLocations')
def my_gps():
 global x
 global y
 session = gps(mode=WATCH_ENABLE)
 try:
  while True:
   data = session.next()
   if data['class'] == "TPV":
    os.system('clear')
    #m=1
    #x= 30.19 #Kafr ElDawar
    #y= 31.12
    #x=29.94145
    #y=31.21939 #Smouha SidiGaber
    #x=29.90421
    #y=31.204024        #Raml
    x = session.fix.longitude
    print(x)
    y = session.fix.latitude
    print(y)
    cur = con.cursor()
    cur.execute("SELECT AdPicture FROM Ads WHERE AreaID  in ( SELECT AreaID FROM AdsAreas WHERE %s > StartLongitude AND %s < EndLongitude  AND %s > StartLatitude AND %s < EndLatitude )",(x,x,y,y))
    for i in range(cur.rowcount):
       row = cur.fetchone()
       p=subprocess.Popen(["eog","-f",row[0]])
       time.sleep(5)
       #if m==0:
       # z.kill()
       # m=1
       #row = cur.fetchone()
       #z=subprocess.Popen(["eog","-f",row[0]])
       #time.sleep(5)
       #if m==1:
       # p.kill()
        #m=0
       p.kill()
 except KeyError:
  pass
 except KeyboardInterrupt:
  print
  print ("Closed By User")
 except StopIteration:
  print
  print ("GPSD has stopped")
 finally:
  session = None

my_gps()
