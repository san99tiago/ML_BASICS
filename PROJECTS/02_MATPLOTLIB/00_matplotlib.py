#BASICS ON MATPLOTLIB LIBRARY
#Santiago Garcia Arango, June 2020

#----------------------------------------------------------------
#Matplot lib is an amazing library that gives us the control...
#...of figures, graphs, plots, and data-visualization.

#It's one of the most popular libraries to generate great plots.

#It has a lot of similarities with the MATLAB figures!!!
#Other libraries are built based on matplotlib.
#It is really simple to use!!!
#You should check the documentation to have a look of everything.
#   https://matplotlib.org/gallery/index.html

#IMPORTANT: 
# you must install it (for example with <pip install matplotlib>)

#-----------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


#IMPORTANT: There are two main ways to work with matplotlib...
# 1. Functional Method (we will use it in this script)
# 2. Object Oriented Method (the best one!... next scripts)

#The best one is the object oriented one, because it allows us...
#...to create figures "objects" and call methods of them. 



#------------------FIGURE 1(FUNCTIONAL METHOD)---------------------
#Vectors "x" and "y" for the plot...
x_1 = np.linspace(0,5,1024)
y_1 = x_1 ** 2

plt.figure(1)
plt.plot( x_1, y_1, 'r' ) #Create the actual plot
plt.xlabel("X LABEL") #Label the x axis as desired
plt.ylabel("Y LABEL") #Label the y axis as desired
plt.title("MY FIGURE 1 TITLE") #Title for the figure
#WARNING: look at the end ( the plt.show() method is necessary!!!)


#------------------FIGURE 2(FUNCTIONAL METHOD)---------------------
#If we want multiple plots, we can use the "subplot()" method...
plt.figure(2)
plt.subplot(1,2,1)
plt.plot(x_1, y_1, 'g')

plt.subplot(1,2,2)
plt.plot(x_1,-y_1, 'b')
#WARNING: look at the end ( the plt.show() method is necessary!!!)



#--------------------SHOW ALL CREATED FIGURES----------------------
#IMPORTANT: Always run this method at the end (show all figures)
plt.show()
