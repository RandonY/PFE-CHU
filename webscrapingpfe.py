# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:56:13 2021

@author: yoann
"""
PATH_TO_SAVE = "D:\csv_pfe"


import requests
import json
from bs4 import BeautifulSoup
import time
import pandas as pd

def getDataOfDay(day,month,year):

    PATH = "https://www.infoclimat.fr/observations-meteo/archives/{}/{}/{}/orly-athis-mons/07149.html".format(day,month,year)
    
    page = requests.get(PATH)
    
    soup = BeautifulSoup(page.text, 'html.parser')
    
#   hours = ["00","23","22","21","20","19","18","17","16","15","14","13","12","11","10","09","08","07","06","05","04","03","02","01"]
    hours = ["01","00","23","22","21","20","19","18","17","16","15","14","13","12","11","10","09","08","07","06","05","04","03","02"]
 
    
    info = []
    temperature = []
    pluie = []
    vent = []
    humidite = []
    pression = []
    
    for x in soup.find_all('td') :
        info.append(x.text)
    
    if ((len(info) == 270) or (len(info) == 272) or (len(info) == 282)):
        del info[0:7]
        del info[239:]
        
        for i in range(len(info)):
            if (i % 10 == 0):
                if (info[i] != ""):
                    info[i] = info[i][0:5].replace("°C","").replace("°","")
                    temperature.append(float(info[i]))
                else:
                    temperature.append("NaN")
            elif (i % 10 == 2):
                if (info[i] != ""):
                    info[i] = info[i][0:5].replace("mm/1h","").replace("mm/","").replace("m","")
                    pluie.append(float(info[i]))
                else:
                    pluie.append("NaN")
            elif (i % 10 == 3):
                if (info[i] != ""):
                    info[i] = info[i][0:2]
                    vent.append(float(info[i]))
                else:
                    vent.append("NaN")
            elif (i % 10 == 4):
                if (info[i] != ""):
                    info[i] = info[i].replace("%","")
                    humidite.append(float(info[i]))
                else:
                    humidite.append("NaN")
            elif (i % 10 == 7):
                if (info[i] != ""):
                    info[i] = info[i].replace("hPa","").replace("=","")
                    pression.append(float(info[i]))
                else:
                    pression.append("NaN")
                    
    elif(len(info) == 248):
        del info[0:7]
        del info[215:]
        
        for i in range(len(info)):
            if (i % 9 == 0):
                if (info[i] != ""):
                    info[i] = info[i][0:5].replace("°C","").replace("°","")
                    temperature.append(float(info[i]))
                else:
                    temperature.append("NaN")
            elif (i % 9 == 2):
                if (info[i] != ""):
                    info[i] = info[i][0:5].replace("mm/1h","").replace("mm/","").replace("m","")
                    pluie.append(float(info[i]))
                else:
                    pluie.append("NaN")
            elif (i % 9 == 3):
                if (info[i] != ""):
                    info[i] = info[i][0:2]
                    vent.append(float(info[i]))
                else:
                    vent.append("NaN")
            elif (i % 9 == 4):
                if (info[i] != ""):
                    info[i] = info[i].replace("%","")
                    humidite.append(float(info[i]))
                else:
                    humidite.append("NaN")
            elif (i % 9 == 6):
                if (info[i] != ""):
                    info[i] = info[i].replace("hPa","").replace("=","")
                    pression.append(float(info[i]))
                else:
                    pression.append("NaN")
         
    data = pd.DataFrame();
    data["heure"] = hours
    data["temperature"] = temperature
    data["pluie"] = pluie
    data["vent"] = vent
    data["humidite"] = humidite
    data["pression"] = pression
    
    data.to_csv(PATH_TO_SAVE+"\data_{}_{}_{}.csv".format(day,month,year),index=False)
    
    return data
#day_possible  = ["1er","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
day_possible  = ["1er","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
#month_possible = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
month_possible = ["octobre","novembre","decembre"]
#year_possible = ["2015","2016","2017","2018","2019"]
year_possible = ["2019"]

for year in year_possible:
    for month in month_possible:
        if month in ["janvier","mars","mai","juillet","aout","octobre","decembre"] :
            for day in day_possible:
                getDataOfDay(day,month,year)
                time.sleep(5) 
        elif month in ["avril","juin","septempbre","novembre"] :
            for day in day_possible[0:30] : 
                getDataOfDay(day,month,year)
                time.sleep(5) 
        else :
            if (year == "2016"):
                for day in day_possible[0:29]:
                    getDataOfDay(day,month,year)
                    time.sleep(5) 
            else : 
                for day in day_possible[0:28]:
                    getDataOfDay(day,month,year)
                    time.sleep(5) 
            
            
            

        





    



