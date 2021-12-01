import Modules.Utility as util
import matplotlib.pyplot as plt

"""
Reference for get_vals() function:
0 = Total
1 = White
2 = Black
3 = Indigenous American / Alaska Native
4 = Asian
5 = Hawaiian or Pacific Islander
6 = Other
7 = Hispanic
"""



#All population lines
#util.plot_all_lines(util.data,util.years, 1e6)

#Scatterplot: Asian (x-axis) and H/PI (y-axis)
#util.ax.scatter([x/1000000 for x in util.get_vals(1)], [x/1000000 for x in util.get_vals(7)])

#Graph points for a set of data and perform a linear regression on it
for i in range(len(util.data)):
    util.ax.scatter(util.years, [x/1000000 for x in util.get_vals(i)])
    util.ax.plot(util.years,util.linear_regression(util.years, [x/1000000 for x in util.get_vals(i)]))

    plt.ticklabel_format(axis="y", style="plain")
    plt.title(util.data[i]["Race/Ethnicity"] + " Population Over Time")
    plt.xlabel("Year")
    plt.ylabel("Population Per Million")
    plt.savefig("Linear Regressions/" + util.data[i]["Race/Ethnicity"] + ".png")
    plt.cla()


#Show legend
#plt.legend()

#Change number formatting from Sci. Not. to Standard
#plt.ticklabel_format(axis="y", style="plain")

#Set Title and Labels
#plt.title("White to Hispanic Population Change")
#plt.ylabel("Hispanic")
#plt.xlabel("White")

#Save figure as file
#plt.savefig("Total_Population.png")

#Show graph
#plt.show()