from typing import Optional
import numpy as np
from tabulate import tabulate as tab

class Vehicle:
    def __init__(self, name, thruster, sensor, birth, hydrophones):
        self.name=name
        self.thruster=thruster
        self.sensor=sensor
        self.birth=birth
        self.hydrophones=hydrophones

    def infoAUV(self):
        ''' this will define my row(the auv info) for the table '''
        return np.array([self.name, self.thruster, self.sensor, self.birth,
        self.hydrophones])

    def showThisAUV(self):
        return np.array([[self.name, self.thruster, self.sensor, self.birth,
        self.hydrophones]])
    
    def birthInfo(self):
        return self.birth 

    def sensorsAUV(self):
        return np.array([self.name, self.sensor])

v1 = Vehicle("Lua",8 ,"SENSOR X1, SENSOR X2", 2022,4)
v2 = Vehicle("BrHUE",6,"SENSOR Y1, SENSOR Y2", 2021,4)

AUVs = [v1,v2]
numAUVs = range(0,len(AUVs))

def tableOfAUVs():
    ''' return a table with all auvs '''
    AUVsTable=[]
    for i in numAUVs:
        AUVsTable.append(AUVs[i].infoAUV())
    tHeader = ["Name", "Thruster", "Sensors", "Birth", "Hydrophones"]
    return tab(AUVsTable, headers=tHeader, tablefmt="fancy_grid")


def anAUV(x=0):
   ''' default argument to avoid errors '''
   tHeader = ["Name", "Sensor", "Thruster", "Birth", "Hydrophones"]
   return tab(AUVs[x].showThisAUV(), headers=tHeader, tablefmt="fancy_grid")

def newer():
    tHeader = ["Name", "Sensor", "Thruster", "Birth", "Hydrophones"]
    l =[]
    sortedB=[]
    for i in range(0, len(AUVs)):
        l.append(str(AUVs[i].birthInfo()))
    for i in range(0, len(l)):
        if max(l) in AUVs[i].infoAUV():
           sortedB.append(AUVs[i].infoAUV())
           l.remove(max(l))
    if len(l) > 0:
        for i in range(0,len(l)):
            if max(l) in AUVs[i].infoAUV():
                sortedB.append(AUVs[i].infoAUV())
                l.remove(max(l))
    return tab(sortedB, headers=tHeader, tablefmt="fancy_grid") 

def AUVsensor():
    sensors=[]
    tHeader=["Name", "Sensor"]
    for i in numAUVs:
        sensors.append(AUVs[i].sensorsAUV())    
    return tab(sensors,headers=tHeader, tablefmt="fancy_grid")

def menu():
    print('========= MENU =========')
    print('')
    print('1 - All AUVs')
    print('2 - Choose an AUV')
    print('3 - All AUVs (sorted by year)')
    print('4 - Sensors')
    print('0 - Close')
    print('')
    print('==================================')

while True:
   menu()
   option = input('Choose an option: ')
   if option == '1':
      print('')
      print(tableOfAUVs())
      print('')
   elif option == '2':
      print('')
      x = int(input(str.format('Digit an index [0-{}]: ', len(AUVs) - 1)))
      print('')
      print(anAUV(x))
      print('')
   elif option == '3':
      print('')
      print(newer())
      print('')
   elif option == '4':
      print('')
      print(AUVsensor())
      print('')
   elif option == '0':
      print('')
      print("""\u001b[34m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⢀⣤⣤⡄⠀⠀⠀⠀⠀⣴⣶⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡄⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠉⠛⠛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠋⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢤⣤⠄⠀⠀⢤⡤⠄⢤⡤⠤⢤⡄⠠⢤⡤⠤⣄⠀⠀⢤⣤⠄⢀⣀⣀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⡀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠀⠀⠀⠀⡇⠀⢸⡇⠀⢀⠁⠀⢸⡇⠀⣹⡇⠀⠀⣿⠀⢸⣿⣿⣦⠀⢸⣿⠀⣀⣀⣀⡀⠀⣀⡀⠀⣀⣀⣀⣾⣇⡀⣈⣉⡀⣿⡇⢀⣀⠀⢀⣀⠀⠀⣀⣀⣀⠀⠀
⠀⠀⠀⣿⠀⠀⠀⠀⡇⠀⢸⡟⠒⠻⠀⠀⢸⡗⢶⣏⠀⠀⠀⣿⠀⢸⣿⡇⢻⣧⣸⣿⠀⣻⣭⣿⣷⠀⣿⡇⠀⣿⣿⠉⣿⡏⠁⣿⣿⡇⣿⡇⢸⣿⠀⢸⣿⠀⣿⣿⣭⣉⠀⠀
⠀⠀⠀⢿⣄⠀⠀⣸⠃⠀⢸⡇⠀⠀⠀⠀⢸⡇⠀⢿⣄⠀⠀⣿⠀⢸⣿⡇⠀⢻⣿⣿⢸⣿⣃⣼⣿⠀⢿⣧⣀⣿⣿⠀⣿⣇⡀⣿⣿⡇⣿⡇⢸⣿⣄⣸⣿⠀⣀⣘⣻⣿⠀⠀
⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠋⠙⠃⠀⠀⠙⠋⠙⠀⠀⠉⠃⣸⠏⠀⠈⠉⠁⠀⠀⠉⠉⠀⠉⠉⠉⠉⠀⠈⠉⠉⠉⠉⠀⠈⠉⠁⠉⠉⠁⠉⠁⠀⠉⠉⠉⠉⠀⠉⠉⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      \u001b[0m""")
      print('')
      break
   else:
      print('')
      print('======> Invalid option')
      print('')
