# Lines starting with # are comments and are not run by Python.
"""
Multi-line comments are possible with triple quotes like this.
"""
# pandas is a common library for working with data in Python, we usually import it like so:
import pandas as pd
import matplotlib.pyplot as plt
import time

# This data comes from the UCI ML repository:
# https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset
# It is the daily number of users from a bike share program
#filename = "C:\Users\mlee013\Documents\GitHub\MSDS600Week1IntroPythonExercisesUploaded\day.csv"


df = pd.read_csv("Documents\GitHub\MSDS600Week1IntroPythonExercisesUploaded\day.csv")


# shows a preview of the data
df.head()
print(df.head())

print("LINE BREAK")
# shows some basic stats of the data
print(df.describe())

# Use the examples in the jupyter notebook to help you here.
# calculate the mean and standard deviation of the hourly data counts (the 'cnt' column)

# Mean
Mean = df["cnt"].mean()
print("The mean of the cnt column is ",Mean)

# standard deviation
#standdeviation = statistics.stdev([2.5, 3.25, 5.5, 11.25, 11.75])  ##examples
standdeviation = df["cnt"].std()
print("The standard deviation is ",standdeviation)


# plot the counts ('cnt' column)
x=list(range(df["cnt"].count()))
iteration = (df["cnt"].count())  ##test to see it iterates 731 times for counts
print(iteration)                 ##print test

# Create a for loop from length 0 to iteration
counts =[]   
for i in range(0, iteration):
      counts.append(df["cnt"][i])

#pause before I can see the graph
time.sleep(3)

# using plt.scatter() to create a x,y plot
plt.scatter(x,counts, c=counts, cmap='Spectral')  #color added
plt.xlabel('day')         # lable the x axis
plt.ylabel("cnt Values")  # lable the y axis
plt.title('Counts')       # title the plot
plt.show()                # show the plot
