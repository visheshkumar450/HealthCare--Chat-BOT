import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt
#After that give the file location
deaths = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Hack@HMR.csv")
#then we are going to print the following data
deaths.replace(nan, 0, inplace = True)

for column in ["World-deaths", "India-deaths"] :
    deaths[column] = deaths[column].map(lambda x : int(x.replace(",", "")))
#After that we will be plotting the graph
plt.clf()          # clf is clear data frame
# plt.figure(figsize = (18, 14), dpi=120)

# Preparing bars for Average DR
barDR = plt.bar(deaths["Diseases"], deaths["India-deaths"], width = 0.55, align = 'center', color = 'red',
                label = 'Diseases')                                      #This will plot bar graph

# Setting graph properties
# plt.yticks(range(0, 6000, 250))
# plt.xticks(range(len(deaths["Diseases"])), deaths["Diseases"])
plt.ylabel("India-deaths")               # The labling of y axis will be here
plt.xlabel("Diseases")                   # The labeling of x axis will be here
plt.title("Deaths in India due to Disease")   #  This will give the title to the plot
plt.legend(fontsize='small')
plt.grid()                           # This gives the grid in the graph
# for (rect, label) in zip(barDR, yrly_avg_DR[-1::-1]):
#     plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 150, format(label, '.2f'), ha='center', va='top')
# In order to show the whole graph use:
plt.show()
# Then print the deaths
print(deaths)
#Finally the Death is printed
# Now I am going to print another dataset of deaths due to major diseases in every country
#for that we are going to use pandas
diseases = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Deaths (1).csv")

print(4)
print(diseases)

plt.clf()          # clf is clear data frame

# plt.figure(figsize = (18, 14), dpi=120)

# Preparing bars for Average DR
barDR = plt.bar(diseases["Country"], diseases["Heart"], width = 0.45, align = 'center', color = 'blue',
                label = 'Diseases')                                      #This will plot bar graph

# Setting graph properties
# plt.yticks(range(0, 6000, 250))
# plt.xticks(range(len(deaths["Diseases"])), deaths["Diseases"])
plt.ylabel("Heart diseases")               # The labling of y axis will be here
plt.xlabel("Country")                   # The labeling of x axis will be here
plt.title("Deaths in every country due to heart Disease")   #  This will give the title to the plot
plt.legend(fontsize='small')
plt.grid()                           # This gives the grid in the graph
# for (rect, label) in zip(barDR, yrly_avg_DR[-1::-1]):
#     plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 150, format(label, '.2f'), ha='center', va='top')
# In order to show the whole graph use:
plt.show()
# Then print the deaths
print(diseases)
causes = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Book1.csv")
print(causes)
#After that we will be plotting the graph
plt.clf()          # clf is clear data frame
# plt.figure(figsize = (18, 14), dpi=120)

# Preparing bars for Average DR
barDR = plt.bar(causes["Year"], causes["Inst. Deaths"], width = 0.65, align = 'center', color = 'magenta',
                label = 'Inst. Deaths')                                      #This will plot bar graph
# Setting graph properties
# plt.yticks(range(0, 6000, 250))
# plt.xticks(range(len(deaths["Diseases"])), deaths["Diseases"])
plt.ylabel("Instant Deaths")               # The labling of y axis will be here
plt.xlabel("Year")                   # The labeling of x axis will be here
plt.title("Past 10 year data of deaths due to heart attack in Delhi")   #  This will give the title to the plot
plt.legend(fontsize="small")
plt.grid()                           # This gives the grid in the graph
# for (rect, label) in zip(barDR, yrly_avg_DR[-1::-1]):
#     plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 150, format(label, '.2f'), ha='center', va='top')
# In order to show the whole graph use:
plt.show()
# Then print the deaths
print(causes)
death_rate = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Book3.csv")
plt.clf()          # clf is clear data frame
# plt.figure(figsize = (18, 14), dpi=120)

# Preparing bars for Average DR
barDR = plt.bar(diseases["Country"], diseases["Heart"], width = 0.45, align = 'center', color = 'blue',
                label = 'Diseases')
# Setting graph properties
# plt.yticks(range(0, 6000, 250))
# plt.xticks(range(len(deaths["Diseases"])), deaths["Diseases"])
plt.ylabel("Heart diseases")               # The labling of y axis will be here
plt.xlabel("Country")                   # The labeling of x axis will be here
plt.title("Deaths in every country due to heart Disease")   #  This will give the title to the plot
plt.legend(fontsize='small')
plt.grid()                           # This gives the grid in the graph
# for (rect, label) in zip(barDR, yrly_avg_DR[-1::-1]):
#     plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 150, format(label, '.2f'), ha='center', va='top')
# In order to show the whole graph use:
plt.show()
# Then print the deaths
print(diseases)
#This is dataset 3
causes = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Book1.csv")
print(causes)
#After that we will be plotting the graph
plt.clf()          # clf is clear data frame
# plt.figure(figsize = (18, 14), dpi=120)

# Preparing bars for Average DR
barDR = plt.bar(death_rate["Age grp."], death_rate["Male"], width = 0.65, align = 'center', color = 'green',
                label = 'Age groups')                                      #This will plot bar graph

# Setting graph properties
# plt.yticks(range(0, 6000, 250))
# plt.xticks(range(len(deaths["Diseases"])), deaths["Diseases"])
plt.ylabel("Male")               # The labling of y axis will be here
plt.xlabel("Age groups")                   # The labeling of x axis will be here
plt.title("Age wise deaths due to heart attack in Delhi")   #  This will give the title to the plot
plt.legend(fontsize="small")
plt.grid()                           # This gives the grid in the graph
# for (rect, label) in zip(barDR, yrly_avg_DR[-1::-1]):
#     plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 150, format(label, '.2f'), ha='center', va='top')
# In order to show the whole graph use:
plt.show()
# Then print the deaths
print(death_rate)
