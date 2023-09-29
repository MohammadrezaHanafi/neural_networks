
import math
import matplotlib.pyplot as plt
import csv


t_min = 18
t_max = 1100

beta = 0.2
gamma = 0.1
tao = 17
n = 10


x = []
for i in range(1, t_min) :
    x.append(0.0)
x.append(1.2)

for t in range(t_min, t_max):
    h = x[t-1] + (beta * x[t-tao-1] / (1 + math.pow(x[t-tao-1], n))) - (gamma * x[t-1])
    h = float("{:0.4f}".format(h))
    x.append(h)  
    

plt.plot(range(t_min, t_max+1), x[t_min-1:t_max])


data = []
x = x[t_min-1:t_max]

for t in range(3, len(x)):
    d = []
    d.append(x[t-3])
    d.append(x[t-2])
    d.append(x[t-1])
    d.append(x[t])
    data.append(d)

with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerows(data)
