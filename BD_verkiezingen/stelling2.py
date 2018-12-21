
#%%
#%matplotlib inline

# module importeren om request te doen
import urllib.request

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.stats import norm

#import pylab as pl

import json

# VUL HIER DE GEWENSTE KIESKRING EN PARTIJ IN, PARTIJ HEEFT EEN NUMMER


KieskringArray = ['Brugge', 'Diksmuide', 'Kortrijk',
                  'Roeselare', 'Tielt', 'Ieper', 'Oostende']
kieskring = list()
kieskring.append({"gemeente":"dsfdfsd", "partij":"sdfdsfsf"})
# IS BIJNA ALTIJD DEZE PARTIJEN (WE GEBRUIKEN NUMMERS OMDAT DE NAMEN KUNNEN VERANDEREN ADHV COALITIES)
# 1 = SPA
# 2 = NVA
# 3 = CD&V
# 4 = GROEN
# 5 = VLAAMS BELANG
# 6 = OPEN VLD
# 7 = LIJST A
# 8 = PVDA

# variabele om requested data in te plaatsen
kieskringdata = urllib.request.urlopen(
    "http://www.rocre.be/verkiezingen/json.php?fields=kieskring,id,lijstnr,lijst,kiezers&duplicates=false").read()

# De data die we terugkeren gaan laden in JSON formaat
data = json.loads(kieskringdata)

# Een nieuwe lokale lijst maken van de stemmen
kieskring_partij = list()
kieskring_kiezers = list()
# Omdat de json data in een wrapper van results zit dit gaan vervangen zodat de code op volgende lijnen korter is.
data = data["results"]


found = False
def search(gemeente, partij):
       for d in kieskring:
            if(partij in d.values() and gemeente in d.values()):
                return True
            else: 
                found = False
       return found


for x in data:
    if(x["kieskring"] in KieskringArray):
     if(search(x["kieskring"], x["lijst"]) == False):
        if(x["lijst"] in kieskring_partij):
             index = kieskring_partij.index(x["lijst"])
             kieskring_kiezers[index] += float(x["kiezers"])
        else:
         kieskring_partij.append(x["lijst"])
         kieskring_kiezers.append(float(x["kiezers"]))
         thisdict = {
             "gemeente": x["kieskring"],
             
             "partij": x["lijst"]
         }
         kieskring.append(thisdict)


plt.pie(kieskring_kiezers, labels=kieskring_partij)
ax = plt.subplot(111)
plt.rcParams.update({'font.size': 10})
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])


ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()

