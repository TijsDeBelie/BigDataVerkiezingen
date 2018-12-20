
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



Mandaten = list()
Blanco = list()
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
    "http://www.rocre.be/verkiezingen/json.php?fields=mandaten,blanco_ongeldig&duplicates=false").read()

# De data die we terugkeren gaan laden in JSON formaat
data = json.loads(kieskringdata)

# Een nieuwe lokale lijst maken van de stemmen

# Omdat de json data in een wrapper van results zit dit gaan vervangen zodat de code op volgende lijnen korter is.
data = data["results"]


for x in data:
    Mandaten.append(x["mandaten"])
    Blanco.append(x["blanco_ongeldig"])




# als er geen stemmen zijn moet het programma stoppen
#if(len(kieskring_partij) == 0) :
#print("ERROR")
#exit()


# de Y as gaan bepalen adhv de normaalverdeling
plt.scatter(Mandaten, Blanco)


#plt.xlabel("Aantal kiezers")
#plt.ylabel("Partij")

#plt.title("Stelling 1 in : " + KieskringNaam + " voor partijnr : "  + str(Partijnummer))

# Een histogram tekenen om makkelijk te gaan kijken of het een normaalverdeling is
#plt.hist(kieskring_stemmen,density=True)
plt.show()

# We kunnnen duidelijk zien dat het geen normaalverdeling is
