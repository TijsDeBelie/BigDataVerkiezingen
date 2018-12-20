
#%%
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

zitErIn = False
def search(gemeente, partij):
    if(len(kieskring) == 0):
        return True
    else:
     for index in range(len(kieskring)):
        print(kieskring[index].get("gemeente"), kieskring[index].get("partij"))
        print(kieskring[index].get("gemeente") == gemeente and kieskring[index].get("partij") == partij)
        if (kieskring[index].get("gemeente") == gemeente and kieskring[index].get("partij") == partij):
                print("FUCK")
                zitErIn = False
        else:
                zitErIn = True


# Gaan kijken voor de gekozen kieskring en partij of er data inzit en deze dan bijhouden in de lokale lijst
for x in data:
    search(x["kieskring"], x["lijst"])
    if(x["kieskring"] in KieskringArray and zitErIn):
         zitErIn = False
         #print(x["kieskring"])
         kieskring_partij.append(x["lijst"])
         kieskring_kiezers.append(float(x["kiezers"]))
         thisdict = {
             "gemeente": x["kieskring"],
             "partij": x["lijst"]
         }
         kieskring.append(thisdict)

print(kieskring)


# als er geen stemmen zijn moet het programma stoppen
#if(len(kieskring_partij) == 0) :
#print("ERROR")
#exit()


# de Y as gaan bepalen adhv de normaalverdeling
plt.pie(kieskring_kiezers, labels=kieskring_partij)


#plt.xlabel("Aantal kiezers")
#plt.ylabel("Partij")

#plt.title("Stelling 1 in : " + KieskringNaam + " voor partijnr : "  + str(Partijnummer))

# Een histogram tekenen om makkelijk te gaan kijken of het een normaalverdeling is
#plt.hist(kieskring_stemmen,density=True)
plt.show()

# We kunnnen duidelijk zien dat het geen normaalverdeling is
