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
util.ax.scatter([x/1000000 for x in util.get_vals(1)], [x/1000000 for x in util.get_vals(7)])

#Graph points for a set of data and perform a linear regression on it
#util.ax.scatter(util.years, [x/1000000 for x in util.get_vals(1)])
#util.ax.plot(util.years,util.linear_regression(util.years, [x/1000000 for x in util.get_vals(1)]))

#Show legend
#plt.legend()

#Change number formatting from Sci. Not. to Standard
plt.ticklabel_format(axis="y", style="plain")

#Set Title and Labels
plt.title("White to Hispanic Population Change")
plt.ylabel("Hispanic")
plt.xlabel("White")

#Save figure as file
#plt.savefig("Total_Population.png")

#Show graph
plt.show()