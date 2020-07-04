#CUSTOMIZING APPEARANCE OF MATPLOTLIB FIGURES 
#Santiago Garcia Arango, July 2020

import os
import numpy as np
import matplotlib.pyplot as plt


#We create the vectors for the plots (in this case, McLauren Series expansion)
x_1 = np.linspace(0,10,1024)
y_1 = np.sin( x_1 )
y_2 = x_1
y_3 = x_1 - x_1**3/(3*2)
y_4 = x_1 - x_1**3/(3*2) + x_1**5/(5*4*3*2)

#1. Create figure with size and dpi specifications (may need to adjust)
# -->figsize: change the actual size of the figure
# -->dpi: "dots per inch" (similar to resolution)
# -->facecolor: the color of the background (external part)
fig = plt.figure( figsize=(8,4), dpi=180, facecolor=(0.2,1,1))


#2. Create the axes based on the proportions of figure-axis plot
# --> [LEFT,BOTTOM,WIDTH,HEIGHT] (in percentages)
ax = fig.add_axes([0.12,0.12,0.8,0.78])


#3. Create the actual plot(s) based on the vectors
# --> label: indicates the name of the plot for the legends (only if needed)
# --> color: indicates the color of the line generated
# -->linewidth: changes the linewidth of the plots
# -->alpha: changes the "transparency" of the linecolor (1 is default)
# -->linestyle: changes the way that the line is displayed (look documentation)
# -->marker: they help to see the "dots" that create plot (look documentation)
# -->markersize: change the size of the markers of the plot (look documentation)
ax.plot( x_1, y_1, label="sin(x) [real]", color="blue", alpha=2, linewidth=2)
ax.plot( x_1, y_2, label="Taylor[1 term]", color="yellow", alpha=0.6, linewidth=2 )
ax.plot( x_1, y_3, label="Taylor[2 terms]", color="green", alpha=0.6, linewidth=2 )
ax.plot( x_1, y_4, label="Taylor[3 terms]", color="red", alpha=0.6, linewidth=2 )


#4. Set the limits in "x" and "y" axis (this can be omitted if not needed)
ax.set_xlim(0,7)
ax.set_ylim(-2,2)


#5. Add title and labels to axis of the plot
ax.set_title("MACLAURIN SERIES OF <sin(x)>", color="black", fontsize=16)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Position [m]")


#6. Add legends to the plot (optional)... must add labels in step #3
#   Note: we can change location, based on another parameter "loc"
ax.legend()


#------------------------------SAVE FIGURES------------------------------
#Current folder obtained with "os" library (to locate files better)
current_folder = os.path.dirname( __file__ ) 

#Get the path to the location where we want to save output
path_to_output_folder = os.path.join(current_folder, 'output')

#In this case, I create the folder to save the output (more clean work)
if not os.path.exists( path_to_output_folder ):
    os.makedirs( path_to_output_folder )

#Save the figure in the path indicated (extension is detected automatically)
fig.savefig( path_to_output_folder + "\\figure_2.pdf", dpi=180, facecolor = (0.2,1,1))


#--------------------------LAST STEP(NEVER FORGET)------------------------
#Always remember to show all the plots at the end!
plt.show()