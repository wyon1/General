#!/usr/bin/env python3

"""
Script to generate a pie graph for GO data. Need to make it more generalizable, but it works.
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


cytoskeleton = 0
cytosol = 0
cytosolic_ribosomal_subunit = 0
ER = 0
mitochondrion = 0
nucleus = 0
plasma_membrane = 0
cytosolic_ribosomal_subunit = 0
secreted = 0
uncharacterized = 0
vesicle = 0




f = pd.read_csv(sys.argv[1])
f_df = pd.DataFrame(f)
subcell_loc_df = f_df.iloc[:,2]
subcell_loc = subcell_loc_df.values.tolist()

for i in subcell_loc:
	if i == "actin filament" or i == "microtubule":
		cytoskeleton += 1
	elif i == "chaperonin-containing T-complex":
		cytosol += 1
	elif i== "cytoplasm":
		cytosol += 1
	elif i == "cytosolic large ribosomal subunit" or i == "cytosolic small ribosomal subunit":
		cytosolic_ribosomal_subunit += 1
	elif i == "ER":
		ER += 1
	elif i == "mitochondrion":
		mitochondrion += 1
	elif i == "nucleus":
		nucleus += 1
	elif i == "plasma membrane":
		plasma_membrane += 1
	elif i == "secreted":
		secreted += 1
	elif i == "uncharacterized":
		uncharacterized += 1
	elif i== "autophagosome" or i == "clathrin coated vesicles" or i == "endosome" or i == "early endosome" or i == "lysosome":
		vesicle += 1
"""
print(actin_fil)
print(autophagosome)
print(clathrin_ves)
print(cytosol)
print(cytosolic_large_ribosomal_subunit)
print(cytosolic_small_ribosomal_subunit)
print(endosome)
print(ER)
print(microtubule)
print(mitochondrion)
print(nucleus)
print(plasma_membrane)
print(secreted)
print(uncharacterized)
print(endosome)
"""

label = ["cytoskeleton", "cytosol", "cytosolic ribosomal subunit", "ER", "mitochondrion", "nucleus", "plasma membrane", "secreted", "vesicle", "uncharacterized"]
val = (cytoskeleton, cytosol, cytosolic_ribosomal_subunit, ER, mitochondrion, nucleus, plasma_membrane, secreted, vesicle, uncharacterized)



fig, ax = plt.subplots(figsize=[7,7])
plt.pie(val)
ax.legend(label, loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)
fig.savefig("clean_pie.png", dpi=600, bbox_inches="tight")                 # Save the figure 
plt.close(fig) 


