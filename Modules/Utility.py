import matplotlib.pyplot as plt
import csv
import numpy as np

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


"""
D A T A   I M P O R T
"""
with open('CensusData.csv') as file:
  reader = csv.DictReader(file)
  data = [row for row in reader]


"""
V A R I A B L E S
"""

#Figure (fig) and Subplot (ax) for graphing
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot()

#Year labels
years = list(data[0].keys())
years.pop(0)
years = [int(x) for x in years]
years.reverse()
  
  
"""
F U N C T I O N S
"""
#----Extract values in float form (return -1 for blank values)----
def get_vals(row_number):
  input = data[row_number]
  output = []
  keys = list(data[row_number].keys())
  
 #Extract values past first dict key
  for i in range(len(keys)):
    if(i == 0):
      continue
    else:
      output += [data[row_number][keys[i]]]
    
  #Change blanks for 0
  for i in range(len(output)):
    if output[i] == "":
      output[i] = 0
      
 #Convert all strings to floats and reverse list order so it matches years in ascending order
  output = [float(x) for x in output]
  output.reverse()
  
  return output


#----Plot all line graphs for data----
def plot_all_lines():
  for i in range(len(data)):
    ax.plot(years, [x/1000000 for x in get_vals(i)], label=data[i]["Race/Ethnicity"])

  plt.legend()
  plt.title("Total US Population Change In The Last 100 Years")
  plt.ylabel("Population Per Million")
  plt.xlabel("Year")
  plt.savefig("Graphs/Misc Graphs/General.png")
  plt.cla()
    
    
#----Returns y-values for a best fir line according to a set of data----
def linear_regression(x,y):
    x = np.array(x)
    y = np.array(y)
    
    #Get best fit coefficients
    fit = np.polyfit(x, y,1)
    poly = np.poly1d(fit)
    
    
    return [poly(i) for i in x]

#----Scatter plot generation----
def scatter():
  for j in range(len(data)):
    for i in range(len(data)):
        if i == 0:
            continue
        else:
            ax.scatter([x/1000000 for x in get_vals(j)], [x/1000000 for x in get_vals(i)])
            plt.title(data[j]["Race/Ethnicity"] + " to " + data[i]["Race/Ethnicity"] + " population")
            plt.xlabel( data[i]["Race/Ethnicity"] + " Population Per Million")
            plt.ylabel( data[j]["Race/Ethnicity"] + " Population Per Million")
            plt.savefig("Graphs/Scatterplots/" + data[j]["Race/Ethnicity"] + "/to " + data[i]["Race/Ethnicity"] +".png")
            plt.cla()

#----GRAPH POINTS FOR A SET OF DATA AND PERFORM A LINEAR REGRESSION ON IT----
def regressions():
    for i in range(len(data)):
      ax.scatter(years, [x/1000000 for x in get_vals(i)])
      ax.plot(years,linear_regression(years, [x/1000000 for x in get_vals(i)]))

      plt.ticklabel_format(axis="y", style="plain")
      plt.title(data[i]["Race/Ethnicity"] + " Population Over Time")
      plt.xlabel("Year")
      plt.ylabel("Population Per Million")
      plt.savefig("Graphs/Linear Regressions/" + data[i]["Race/Ethnicity"] + ".png")
      plt.cla()

#----Graph demographic percentages over time----
def percentages(white=True):

  percents = []
  total = get_vals(0)

  if white == True:
    add = 1
    for i in range(len(data)):
      if i == 0:
        continue
      else:
        percents += [[round((get_vals(i)[x]/total[x])*100, 2) for x in range(len(get_vals(i)))]]
  else:
    add = 2
    for i in range(len(data)):
      if i == 0 or i == 1:
        continue
      else:
        percents += [[round((get_vals(i)[x]/total[x])*100, 2) for x in range(len(get_vals(i)))]]

    
  # Make the plot
  gap = .8 / len(percents)
  for i, p_row in enumerate(percents):
    X = np.arange(len(p_row))
    plt.bar(X + i * gap, p_row, width = gap, align="center", label=data[i+add]["Race/Ethnicity"])

  # Add xticks on the middle of the group bars
  plt.xlabel('group', fontweight='bold')
  plt.xticks([r + gap for r in range(len(percents[0]))], years)
    
  
  plt.title("Population Percentages Over Time")
  plt.legend()
  if white == True:
    plt.savefig("Graphs/Misc Graphs/percents.png")
  else:
    plt.savefig("Graphs/Misc Graphs/percents_no_white.png")
  plt.cla()

