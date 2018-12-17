
#%%
# module importeren om request te doen
import urllib.request

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

import json


# variabele om requested data in te plaatsen
kieskringdata = urllib.request.urlopen("http://www.rocre.be/verkiezingen/json.php?fields=kieskring,naamstemmen,naam,id&duplicates=false").read()


data = json.loads(kieskringdata)

kieskring_naam = list()
kieskring_stemmen = list()

data = data["results"]
for x in data:
    if(x["kieskring"] == "Asse"):
        kieskring_naam.append(x["naam"])
        kieskring_stemmen.append(x["naamstemmen"])

print(kieskring_naam, kieskring_stemmen)
plt.bar(kieskring_naam, kieskring_stemmen, align='center', alpha=0.5)
plt.title('Stelling 1')
plt.show()
