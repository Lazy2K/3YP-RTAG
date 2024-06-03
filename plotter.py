import matplotlib.pyplot as plt
import numpy as np
import csv

x_points = []
y_points = []

tmp_x = []

xpoint = 0

with open('data/data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        tmp_x.append(float(row[0]))
        if (len(tmp_x) >= 20):
            y_points.append(np.mean(tmp_x))
            x_points.append(xpoint)
            tmp_x = []
            xpoint += 10


plt.plot(x_points, y_points)
plt.show()
