
#%%
#%matplotlib inline
# module importeren om request te doen
import urllib.request

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.stats import norm


import json



Mandaten = list()
Blanco = list()
kieskring = list()
kieskring.append({"gemeente":"dsfdfsd", "partij":"sdfdsfsf"})



# variabele om requested data in te plaatsen
kieskringdata = urllib.request.urlopen(
    "http://www.rocre.be/verkiezingen/json.php?fields=mandaten,blanco_ongeldig,kieskring,lijst&duplicates=false").read()

# De data die we terugkeren gaan laden in JSON formaat
data = json.loads(kieskringdata)

# Omdat de json data in een wrapper van results zit dit gaan vervangen zodat de code op volgende lijnen korter is.
data = data["results"]


def search(gemeente, partij):
       for d in kieskring:
            if(gemeente in d.values()):
                return True
            else:
                found = False
       return found


for x in data:
    if(search(x["kieskring"], x["lijst"]) == False):
        thisdict = {
        "gemeente": x["kieskring"],
        "partij": x["lijst"],
        "mandaten" : float(x["mandaten"]),
        "blanco" : float(x["blanco_ongeldig"])
        }
        kieskring.append(thisdict)

kieskring.pop(0)

newlist = sorted(kieskring, key=lambda k: k['mandaten']) 

print(len(newlist))

for p in newlist:
        Mandaten.append(p["mandaten"])
        Blanco.append(p["blanco"])

plt.scatter(Mandaten, Blanco)

z = np.polyfit(Mandaten, Blanco, 1)
p = np.poly1d(z)
plt.plot(Mandaten,p(Mandaten),"r--")


plt.show()

