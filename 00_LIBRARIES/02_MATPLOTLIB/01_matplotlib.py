# WORKING WITH OBJECT-ORIENTED APPROACH TO MATPLOTLIB PLOTS
# Santiago Garcia Arango, July 2020

import numpy as np
import matplotlib.pyplot as plt

# In this script, we will use the Object Oriented approach of...
# ... the matplotlib library. It is easier and gives us more...
# ... control of the different plots and its applications.

# We create the vectors for the plots
x_1 = np.linspace(0, 5, 1024)
y_1 = x_1**2

# ----------------OBJECT ORIENTED METHOD FOR FIGURES-------------------
# --->FIRST FIGURE...
# We define a figure for the creation of the plot
figure_1 = plt.figure(1)

# We create the axes that make possible the plots (like in MATLAB)
#  Note: fig.add_axes( self, *args, **kwargs), where:
#  rect           --> [LEFT,BOTTOM,WIDTH,HEIGHT] (in percentages)
#  projection     --> projection type of the Axes.
#  sharex,sharey  --> Parameters that share the "x" or "y" axis.
#  label          --> Label for the returned axes.

axes_1 = figure_1.add_axes([0.1, 0.1, 0.8, 0.8])

# We generate the plot to the figure_1 and its axes.
axes_1.plot(x_1, y_1, c='b', linewidth=3)

# We customize figure_1 with title, "x"-"y" labels
axes_1.set_title("MY COOL TITLE FOR FIGURE 1")
axes_1.set_xlabel("MY  \"X\"  LABEL")
axes_1.set_ylabel("MY  \"Y\"  LABEL")

# We change the background color of the external part
figure_1.patch.set_facecolor((0.2, 1, 1))

# --->SECOND FIGURE...
figure_2 = plt.figure(2)
axes_2 = figure_2.add_axes([0.2, 0.2, 0.6, 0.6])

axes_2.plot(x_1, -y_1, c='r', linewidth=4)
axes_2.set_title("MY COOL TITLE FOR FIGURE 2")
axes_2.set_xlabel("MY  \"X\"  LABEL")
axes_2.set_ylabel("MY  \"Y\"  LABEL")

figure_2.patch.set_facecolor('xkcd:mint green')


# We display the created figures of this script
plt.show()
