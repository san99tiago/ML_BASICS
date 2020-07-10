# REGRESSION PLOTS WITH SEABORN
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


# -------------------CONFIGURE STYLE OF PLOTS-----------------------------
# Look in documentation for multiple styles!!!
sns.set_style("ticks")

# Great way to change the "general context" and fontsize of the figures
sns.set_context("notebook", font_scale=1.2)


# ----------------------REGRESSION PLOTS-----------------------------------
# We can easily create regression plots with seaborn (with great styles)
sns.lmplot(x="total_bill", y="tip", data=data_frame)

save_figure.SaveFigure("output", "plot_6.pdf")


# We can now divide plots with extra "columns"/"rows" information like this:
sns.lmplot(
    x="total_bill",
    y="tip",
    data=data_frame,
    col="sex"
    )

save_figure.SaveFigure("output", "plot_7.pdf")


# A great advantage of seaborn, is that it's built on top of matplotlib...
# ... giving us the possibility of changing parameters as in matplotlib.
# Now we can "customize" this regression plots even more!
plot_8 = sns.lmplot(
    x="total_bill",
    y="tip",
    data=data_frame,
    hue="sex",
    palette="Set1",
    markers=['o', 'v']
    )

# We access the "axes" of the plot created and change the title!
plot_8.axes[0, 0].set_title("MY LINEAR REGRESSION PLOT")

# We add our name to the plot (for customizing it even more)
plot_8.axes[0, 0].text(
        0.98,
        0.02,
        'Santiago Garcia Arango',
        verticalalignment='bottom',
        horizontalalignment='right',
        transform=plot_8.axes[0, 0].transAxes,
        color='blue',
        fontsize=10
        )

plt.tight_layout()
save_figure.SaveFigure("output", "plot_8.pdf")


# --------------------------LAST STEP(NEVER FORGET)------------------------
# Always remember to show all the plots at the end!
plt.show()
