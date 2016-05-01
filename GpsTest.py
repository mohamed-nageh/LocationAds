from gps import *
import os

def my_gps():
 session = gps(mode=WATCH_ENABLE)
 try:
  while True:
   data = session.next()
   if data['class'] == "TPV":
    os.system('clear')
    print
    print (' GPS Readings')

    print ('latitude      ' , session.fix.latitude)
    print ('longitude     ' , session.fix.longitude)


    print ('velocity (m/s) ' , session.fix.speed)
    print

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
