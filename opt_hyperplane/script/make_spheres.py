import numpy as np


x=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
y=[1.0 ,2.0 ,1.0 ,2.0, 1.0, 2.0]
label = [1, 0 , 1, 0, 1, 0]

x_dummy = []
y_dummy = []
label_dummy = []

for x1, y1, l in zip(x, y, label):
    for _ in range(40):
        x_dummy.append(x1 + 0.3*(2*np.random.rand()-1))
        y_dummy.append(y1 + 0.3*(2*np.random.rand()-1))
        label_dummy.append(l)

with open("DataSetC-10.dat", "w+") as f:    
    for x1, y1, l in zip(x_dummy, y_dummy, label_dummy):
        string = str(x1) + str("\t") + str(y1) + str("\t") + str(l) + "\n"
        f.write(string)
    
    