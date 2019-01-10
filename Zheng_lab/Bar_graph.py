#!/usr/bin/env python

"""
Script to generate bar graph

"""


import numpy as np
import matplotlib.pyplot as plt
 
x_tick_names = ('(-) ctrl', '0.5', '1h', '4', '6', "9", "12", "24") #x axis labels for each set
x_pos = np.arange(len(x_tick_names)) #not sure what this does
y_val = [1,0.837,0.895,0.557,0.497,0.327,0.333, 0.271] #y values corresponding to each position in the x_tick_names variable
 
fig = plt.figure()
plt.bar(x_pos, y_val, align='center', color = "green",linewidth=1, edgecolor='black')
plt.xticks(x_pos, x_tick_names, rotation=90)
plt.ylabel('Y label')
plt.xlabel('X label')
plt.title('Title')

plt.tight_layout()

plt.savefig("bar_graph.png", dpi=600)     # Save figure as .png
plt.close(fig)   