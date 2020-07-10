# CATEGORICAL PLOTS WITH SEABORN
# Santiago Garcia Arango, July 2020

import save_figure
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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


# -------------------SIMPLE BAR PLOT (BASED ON MEAN)-----------------------
# Create plot based on categorical data (and plot value such as the mean)
# It is like visualization of the mean, of selected category possibilities
fig_4, ax_4 = plt.subplots()
sns.barplot(x="sex", y="total_bill", data=data_frame)
ax_4.set_title("TOTAL BILL MEAN (BASED ON SEX)")

save_figure.SaveFigure("output", "plot_4.pdf")

# ---------------------BAR PLOT BASED ON ESTIMATOR-------------------------
# This allows us to create a barplot based on a category and another ...
# ... estimator (different than the <mean>, which is the default one)

# Lets suppose that the estimator wanted is the standard deviation:
fig_5, ax_5 = plt.subplots()
sns.barplot(
    x="sex",
    y="total_bill",
    data=data_frame,
    estimator=np.std,
    hue="smoker"
    )
ax_5.set_title("TIPS MEAN (BASED ON SEX)")

save_figure.SaveFigure("output", "plot_5.pdf")

# ---------------------------VIOLIN PLOT-----------------------------------
# Lets suppose that the estimator wanted is the standard deviation:
fig_6, ax_6 = plt.subplots()
sns.violinplot(
    x="day",
    y="total_bill",
    data=data_frame
    )
ax_6.set_title("VIOLIN PLOT (BASED ON DAY)")

save_figure.SaveFigure("output", "plot_5.pdf")

# --------------------------LAST STEP(NEVER FORGET)------------------------
# Always remember to show all the plots at the end!
plt.show()
