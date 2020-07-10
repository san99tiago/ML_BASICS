# BASIC DISTRIBUTION PLOTS WITH SEABORN
# Santiago Garcia Arango, July 2020

import save_figure
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random

# --------------------FIRST STEP: LOAD INFO-------------------------------
# We have to load info (usually with pandas or numpy)

# Create dataframe based on ( <DATA>, <HEADERS_VERTICAL>, <HEADERS_HORIZONTAL>)
data_frame = pd.DataFrame(
    [
        [15, 1.8, "Female", "No", "Sun", "Dinner", 2],
        [23, 2.05, "Male", "Yes", "Sun", "Dinner", 3],
    ],
    [0, 1],
    ["total_bill", "tip", "sex", "smoker", "day", "time", "size"]
    )

# We add extra columns to the dataframe (to make a "more real" exercise)
for i in range(49):
    # Create random info for each row of our data_frame
    new_bill = random.normalvariate(20, 8)
    new_tip = new_bill/10 + random.normalvariate(2, 0.5)
    new_sex = random.choice(["Female", "Male"])
    new_smoker = random.choice(["Yes", "No"])
    new_day = random.choice(["Sun", "Sat"])
    new_time = "Dinner"
    new_size = random.randint(1, 4)

    # Create the new row to be added to the data_frame
    new_row = []
    values = [
        new_bill, new_tip, new_sex, new_smoker, new_day, new_time, new_size
        ]
    cols = ["total_bill", "tip", "sex", "smoker", "day", "time", "size"]
    new_row = pd.Series(values, cols)

    data_frame = data_frame.append(new_row, ignore_index=True)

print("\n\ndata_frame =\n", data_frame)


# --------------------DISTRIBUTION PLOT (ONE VARIABLE)---------------------
# We pass a single column of a dataframe: "sns.displot(COLUMN)"
plot_1 = sns.distplot(data_frame["total_bill"], bins=50)
plot_1.set_title("DISTRIBUTION PLOT")

# Optional: save the figure (I created a simple module to do this)
save_figure.SaveFigure("output", "plot_1.pdf")

# --------------------JOINT PLOT (TWO VARIABLES)---------------------------
# We pass two columns of a dataframe and see the behavior
plot_2 = sns.jointplot(x="total_bill", y="tip", data=data_frame, kind="reg")

save_figure.SaveFigure("output", "plot_2.pdf")

# -----------------PAIRPLOT (N PAIRS OF VARIABLES)--------------------------
# This allows us to plot valuable info from numeric pairs of variables!
# Note: "hue" helps us to color the output based on other parameter!!!
plot_3 = sns.pairplot(data_frame, hue="sex")

save_figure.SaveFigure("output", "plot_3.pdf")


# --------------------------LAST STEP(NEVER FORGET)------------------------
# Always remember to show all the plots at the end!
plt.show()
