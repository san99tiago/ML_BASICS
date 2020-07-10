# SIMPLE SCRIPT TO SAVE A SEABORN PLOT IN ANOTHER FOLDER IN SAME DIRECTORY
# Santiago Garcia Arango, July 2020

import os
import matplotlib.pyplot as plt

class SaveFigure:
    """
    -----------SaveFigure-----------
    plot: the plot generated from seaborn library.       
    folder_name: name of the output folder to save image.
    output_name: name of the desired figure name (include extension).
    """
    def __init__(self, folder_name, output_name):
        # Current folder obtained with "os" library (to locate files better)
        current_folder = os.path.dirname(__file__)

        # Get the path to the location where we want to save output
        path_to_output_folder = os.path.join(current_folder, folder_name)

        # In this case, I create the folder to save the output (more clean work)
        if not os.path.exists(path_to_output_folder):
            os.makedirs(path_to_output_folder)
        
        # Save the figure in the path indicated
        # Note: (extension is detected automatically)
        try:
            plt.savefig(
            os.path.join(path_to_output_folder, output_name),
            dpi=180,
            facecolor=(0.2, 1, 1)
            )
        except:
            print("Python module <save_figure> did not work properly.")
