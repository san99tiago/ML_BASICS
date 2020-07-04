#WORKING WITH SUBPLOTS IN A SINGLE FIGURE
#Santiago Garcia Arango, July 2020

import os
import numpy as np
import matplotlib.pyplot as plt

#We create the vectors for the plots
x_1 = np.linspace(0,5,1024)
y_1 = x_1**2
y_2 = 25*np.cos( x_1 )

#-------------------CREATING FIGURES WITH SUBPLOTS--------------------
#For creating multiple sub-plots in a figure, we use "plt.subplots(N,M)"
fig, axes = plt.subplots( nrows=1, ncols=2)

#Now, "fig" and "axes" are arrays, to handle the information easier
#Note: "len(axes)" gives us the amount of objects "axes" created
#we iterate through them, to add the titles and their properties.
#Remark: we could do this manually (axes[0]..., axes[1]..., etc)
for current_ax in range( len(axes) ):
    axes[current_ax].set_title("TITLE {}".format(current_ax) )
    axes[current_ax].set_xlabel("MY  X  LABEL")
    axes[current_ax].set_ylabel("MY  Y  LABEL")

#Now we add the plot vectors to the figure axes
axes[0].plot( x_1, y_1 )
axes[1].plot( x_1, -y_1 )



#-------------------CREATE FIGURES WITH SIZE AND DPI------------------
#We can now change the size and "resolution" of the figures...
#  figsize --> change the actual size of the figure
#  dpi     --> "dots per inch" (similar to resolution)

#1. Create figure with size and dpi specifications (may need to adjust)
fig = plt.figure( figsize=(8,4), dpi=180 )

#2. Create the axes based on the proportions of figure-axis plot
ax = fig.add_axes([0.12,0.12,0.8,0.78])

#3. Create the actual plot(s) based on the vectors
#   Note:"labels" are added when we have different plots and need legends
ax.plot( x_1, y_1, label="System 1", c="purple", linewidth=3)
ax.plot( x_1, y_2, label="System 2", c="green", linewidth=3 )

#4. Add title and labels to axis of the plot
ax.set_title("FIRST HD SANTI'S PLOT", color="blue", fontsize=20)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")

#5. Add legends to the plot (optional)... must add labels in step #3
#   Note: we can change location, based on another parameter "loc"
ax.legend()

#6. Change the background-color of the external part of plot
fig.patch.set_facecolor( (0.2,1,1) )



#------------------------------SAVE FIGURES------------------------------
#Current folder obtained with "os" library (to locate files better)
current_folder = os.path.dirname( __file__ ) 

#Get the path to the location where we want to save output
path_to_output_folder = os.path.join(current_folder, 'output')

#In this case, I create the folder to save the output (more clean work)
if not os.path.exists( path_to_output_folder ):
    os.makedirs( path_to_output_folder )

#Save the figure in the path indicated (extension is detected automatically)
fig.savefig( path_to_output_folder + "\\figure_1.pdf", dpi=180, facecolor = (0.2,1,1))



#--------------------------FIX SIZES CORRECTLY----------------------------
#Remark: If we want to "shrink" the layouts to fit, we call "plt.tight_layout()"
plt.tight_layout()

#We show and plot everything on the screen
plt.show()