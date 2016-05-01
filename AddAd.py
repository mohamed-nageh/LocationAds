import MySQLdb as mdb
import os

con = mdb.connect('localhost', 'root' , ' ', 'AdsLocations')
os.system("clear")

print("Welcome to Location Based Advertising Company")
print("==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-")
print
print("Add a new Area -> 1")
print("Add a new Ad   -> 2")
print("-=-=-=-=-=-=-=-=-=-")
print

#choice = raw_input(" Enter Choice :")
choice = input(" Enter Choice : ")

if choice == 1:
   os.system("clear")
   print("Add a new Area")
   print("**************")
   print
   print("Existing Areas")
   print("-=-=-=-=-=-=-=")
   with con:
       cur = con.cursor()
       cur.execute("select AreaID,AreaName From AdsAreas")
       print("ID      Name")
       rows = cur.fetchall()
       for row in rows:
          print ("%s  ...  "+ row[1])%row[0]
          AreaID=row[0]
       print("-=-=-=-=-=-=-=-=-")
       #AreaID=
       AreaName=raw_input("Enter New Area Name :")
       StartLongitude=input("Enter Area's Start Longitude :")
       EndLongitude=input("Enter Area's End Longitude :")
       StartLatitude=input("Enter Area's Start Latitude :")
       EndLatitude=input("Enter Area's End Latiitude :")
       AreaID=AreaID+1
       cur.execute("INSERT INTO AdsAreas(AreaID,AreaName,StartLongitude,EndLongitude,StartLatitude,EndLatitude) VALUES (%s,%s,%s,%s,%s,%s)",(AreaID,AreaName,StartLongitude,EndLongitude,StartLatitude,EndLatitude))
       #query = "INSERT INTO AdsAreas (AreaID,AreaName,StartLongitude,EndLongitude,StartLatitude,EndLatitude) VALUES (%s,%s,%s,%s,%s,%s)",(AreaID,AreaName,StartLongitude,EndLongitude,StartLatitude,EndLatitude"
       #cur.execute(query)
elif choice == 2: #must contain at least one ad - adID
   os.system("clear")
   print("Add a new Advertisment")
   print("**********************")
   Advertiser=raw_input("Company Name (OneWord): ")
   with con:
       cur = con.cursor()
       cur.execute("select AdID FROM Ads")
       rows = cur.fetchall()
       for row in rows:
          AdID=row[0]
       AdID=AdID+1
       print("Select Area ID to add an Ad from the list below :")
       print
       cur = con.cursor()
       cur.execute("select AreaID,AreaName From AdsAreas")
       print("ID      Name")
       rows = cur.fetchall()
       for row in rows:
          print ("%s  ...  "+ row[1])%row[0]
       print("-=-=-=-=-=-=-=-=-")

       AreaID=input("Area ID : ")
       AdLink=raw_input("Paste picture url (.jpg) : ")
       picture = Advertiser+".jpg"
       cmd = "wget "+AdLink+" -q -O "+ picture
       os.system(cmd)
       cur = con.cursor()
       cur.execute("INSERT INTO Ads (AdID ,Advertiser ,AreaID, AdPicture) VALUES (%s,%s,%s,%s)",(AdID,Advertiser,AreaID,picture))
       print("Success")
