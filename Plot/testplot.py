# Import libraries
from matplotlib import pyplot as plt
import numpy as np


# Creating dataset
cars = []
data = []

file = open('Plot/result2.txt', 'r')
list = file.readlines()
for item in list:
    temp1, temp2 = item.split(',')
    # print(temp1)

    # print(temp2)
    if float(temp2) > 10000 and float(temp2) < 60000:
        cars.append(temp1)
        data.append(temp2)

# Creating plot
fig = plt.figure(figsize=(10, 8))
plt.pie(data, labels=cars)

# show plot
plt.show()

# plt.bar(data, cars)
# plt.show()
