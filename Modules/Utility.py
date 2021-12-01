import matplotlib.pyplot as plt
import csv
import numpy as np

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
#Extract values in float form (return -1 for blank values)
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


#Plot all lines for data
def plot_all_lines(inp, years, amt=1):
  for i in range(len(inp)):
    ax.plot(years, [x/amt for x in get_vals(i)], label=inp[i]["Race/Ethnicity"])
    
    
#Returns y-values for a best fir line according to a set of data
def linear_regression(x,y):
    x = np.array(x)
    y = np.array(y)
    
    #Get best fit coefficients
    fit = np.polyfit(x, y,1)
    poly = np.poly1d(fit)
    
    
    return [poly(i) for i in x]