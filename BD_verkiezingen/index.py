
#%%
# module importeren om request te doen
import urllib.request

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.stats import norm
#import pylab as pl

import json


# variabele om requested data in te plaatsen
kieskringdata = urllib.request.urlopen("http://www.rocre.be/verkiezingen/json.php?fields=kieskring,naamstemmen,naam,id,lijstnr&duplicates=false").read()


data = json.loads(kieskringdata)

kieskring_naam = list()
kieskring_stemmen = list()

data = data["results"]

for x in data:
    if(x["kieskring"] == "Merchtem" and x["lijstnr"] == "2"):
        kieskring_naam.append(x["naam"])
        kieskring_stemmen.append(int(x["naamstemmen"]))


mean = np.mean(kieskring_stemmen)
std = np.std(kieskring_stemmen)
print(np.std(kieskring_stemmen))
print(norm.pdf(kieskring_stemmen,mean,np.std(kieskring_stemmen)))


kieskring_stemmen = sorted(kieskring_stemmen)
print(kieskring_stemmen)


fit = norm.pdf(kieskring_stemmen, np.mean(kieskring_stemmen), np.std(kieskring_stemmen))
plt.plot(kieskring_stemmen,fit,'-o')



plt.hist(kieskring_stemmen,density=True)
plt.show()

