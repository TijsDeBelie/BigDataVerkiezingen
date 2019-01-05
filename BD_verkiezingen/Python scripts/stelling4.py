
#%%
#%matplotlib inline
# module importeren om request te doen
import urllib.request

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.stats import norm
from scipy.stats.stats import pearsonr

import xlrd

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'requirements/lijst.xlsx')

sheet_data = []
wb = xlrd.open_workbook(filename)
p = wb.sheet_names()
for y in p:
   sh = wb.sheet_by_name(y)
   for rownum in range(sh.nrows):
      sheet_data.append((sh.row_values(rownum)))

import re
import json


kieskringdata = urllib.request.urlopen(
    "http://www.rocre.be/verkiezingen/json.php?fields=naam,lijst,verkozen,naamstemmen&duplicates=false").read()

# De data die we terugkeren gaan laden in JSON formaat
data = json.loads(kieskringdata)
data = data["results"]

mannen = 0
vrouwen = 0
onbekend = 0
MannenAantal = 0
VrouwenAantal = 0
OnbekendAantal = 0
#lijstarray = ["Groen"]
for x in data :
    #if x["lijst"] in lijstarray :
        name = x["naam"].split()
        firstname = name[-1]
        re.sub('[^A-Za-z0-9]+', '', firstname)
        try:
            for i in sheet_data:
                if(i[0] == firstname):
                    gender = i[1].upper()
                
            #print(gender)
            if(len(gender) < 1 ):
                gender = "onbekend"
        except UnicodeEncodeError:
            pass
        if(gender == "M"):
            mannen += float(x["naamstemmen"])
            MannenAantal +=1
        elif(gender == "F"):
            VrouwenAantal +=1
            vrouwen += float(x["naamstemmen"])
        else:
            OnbekendAantal+=1
            onbekend += float(x["naamstemmen"])

stemarray = list()
stemlabels = list()
#print(mannen,vrouwen,onbekend)
#stemarray = [295568.0,85098.0,0]
stemarray = [mannen, vrouwen, onbekend]
print(stemarray)
stemlabels = ["Man", "Vrouw","Onbekend"]
width = 1/1.5

plt.bar(stemlabels,stemarray, width, color="blue")
plt.xlabel("\nGeslacht")
plt.ylabel("Aantal naamstemmen")
plt.title("Som van de naamstemmen per geslacht voor " + str(MannenAantal) + " mannelijke en " + str(VrouwenAantal) + " vrouwelijke kandidaten")
plt.show()

#Deze verkiezing halen mannen meer stemmen dan vrouwen ondanks de verplichte man/vrouw afwisseling van de samenstelling van de lijsten