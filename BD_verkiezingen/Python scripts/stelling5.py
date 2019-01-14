
# %%
# %matplotlib inline




# module importeren om request te doen
import urllib.request

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.stats import mstats
from scipy.stats import norm
from scipy.stats.stats import pearsonr

import pandas as pd

import re
import json
import math

plt.style.use('seaborn')
plt.rcParams.update({'figure.max_open_warning': 0})

kieskringdata = urllib.request.urlopen(
    "http://www.rocre.be/verkiezingen/json.php?fields=naam,naamstemmen,verkozen&duplicates=false").read()

# De data die we terugkeren gaan laden in JSON formaat
data = json.loads(kieskringdata)
data = data["results"]

eindarray = list()

def search(letter):
       found = False
       for d in eindarray:
            if(letter in d.values()):
                return True
            else: 
                found = False
       return found

for x in data:
    if len(x["verkozen"]) >= 1:
        name = x["naam"][:1]
        if(search(name) == True):
            for y in eindarray:
                if(y["letter"] == name):
                    y["stemmen"].append(float(x["naamstemmen"]))
                    y["aantal"] +=1
                    
        else :
            thisdict = {
                "letter": name,
                "stemmen": [float(x["naamstemmen"])],
                "aantal" : 1,
                "std": 0
            }
            eindarray.append(thisdict)


eindarray = sorted(eindarray, key=lambda k: k['letter']) 

dataframe = pd.DataFrame(eindarray)
print(dataframe)


index = 0

for a in eindarray:
    
    plt.figure(index+1)
    mean = np.mean(a["stemmen"])
    

    
    a["std"] = np.std(a["stemmen"])
    a["stemmen"] = sorted(a["stemmen"])
    y = norm.pdf(a["stemmen"], np.mean(a["stemmen"]), a["std"])
    plt.plot(a["stemmen"],y, '-o', label='Data')
    plt.axvline(mean, color='k', linestyle='dashed', linewidth=1)
    plt.xlabel("Aantal naamstemmen voor de verkozen kandidaat")
    plt.ylabel("Kansdichtheid")

    plt.title("Curve voor beginletter " + a["letter"].lower() + " van de achternaam")
    
    mu, std = norm.fit(a["stemmen"])
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 10000)
    p = norm.pdf(x, mu, std)

    plt.plot(x, p, 'k', linewidth=2)

    if(len(a["stemmen"]) >= 20):
        z,pval = mstats.normaltest(a["stemmen"])

        if(pval < 0.04284731):
            print("Er is geen Normaalverdeling!")
        else:
            print("Er is een Normaalverdeling!")
    else:
        print("Er waren niet genoeg gegevens om dit te berekenen!")
    
    som = 0
    index +=1
    for x in a["stemmen"]:
        som += float(x)
    a["stemmen"] = som

plt.show()

dataframe = pd.DataFrame(eindarray)
print(dataframe)

x_as = list()
y_as = list()
aantal_as = list()
standaarddev = list()
for d in eindarray:
    x_as.append(str(d["letter"]))
    y_as.append(float(d["stemmen"]))
    aantal_as.append(d["aantal"])
    standaarddev.append(d["std"])


gemiddelde = list()

i = 0
for e in y_as:
    gemiddelde.append(e/aantal_as[i])
    i+=1




plt.xlabel("Eerste letter achternaam")
plt.ylabel("Totaal aantal stemmen")
plt.title("Totaal aantal stemmen per eerste letter van de achternaam voor de verkozen kandidaten")
plt.bar(x_as, y_as)
plt.show()


ax = plt.subplot(111)
N = len(x_as)
ind = np.arange(N) 

width = 0.35 

plt.bar(ind, gemiddelde, width, label='Gemiddelde')
plt.bar(ind + width, standaarddev, width,
    label='Standaarddeviatie')

plt.ylabel('Aantal stemmen')
plt.title('')
plt.xticks(ind + width / 2, x_as)
plt.xlabel("Eerste letter achternaam")
plt.title("Gemiddeld aantal stemmen en standaarddeviatie per eerste letter van de achternaam voor de verkozen kandidaten")
plt.legend(loc='best')
plt.show()

 


#Er is een verband tussen de eerste letter van de achternaam en het aantal stemmen voor de verkozen kandidaten
#Er is een verband tussen de eerste letter en het achternaam en het aantal stemmen dat nodig is om verkozen te geraken.


#Gemiddeld gezien hebben mensen met achternaam dat start met Y meer stemmen nodig om verkozen te worden. 