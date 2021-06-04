import numpy as np
import os
import matplotlib.pyplot as plt


class Data(object):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.dataset = {}
        self.initialize
    
    @property
    def initialize(self):
        self.dataset[0] = []
        self.dataset[1] = []
    
    def get_upper_lower(self):
        minx = self.get_min_x()
        maxx = self.get_max_x()
        
        avg_x = (maxx-minx)/2
        
        a_x = np.argmin(np.abs(self.dataset[0][:,0] - avg_x))
        b_x = np.argmin(np.abs(self.dataset[1][:,0] - avg_x))
        
        a_y = self.dataset[0][a_x, 0]
        b_y = self.dataset[0][b_x, 0]
        
        sum_a = np.sum(self.dataset[0][:,1])
        sum_b = np.sum(self.dataset[1][:,1])
        
        if sum_a>sum_b:
            return 1
        elif sum_a<sum_b:
            return -1
        else:
            return 0
        
    def read(self):
        self.add_dataset(self.filepath)
        self.dataset[0] = np.array(self.dataset[0])
        self.dataset[1] = np.array(self.dataset[1])
    
    def add_dataset(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.rstrip()
                list_line = line.split("\t")
                list_line = [float(value) for value in list_line]
                self.dataset[int(list_line[2])].append(list_line[:2])
    
    def plot(self):
        plt.scatter(self.dataset[0][:,0], self.dataset[0][:,1], c="red")
        plt.scatter(self.dataset[1][:,0], self.dataset[1][:,1], c="blue")
        plt.show()
    
    def get_min_x(self):
        return min(np.min(self.dataset[0][:, 0]), np.min(self.dataset[1][:, 0]))

    def get_max_x(self):
        return max(np.max(self.dataset[0][:, 0]), np.max(self.dataset[1][:, 0]))

    def get_min_y(self):
        return min(np.min(self.dataset[0][:, 1]), np.min(self.dataset[1][:, 1]))

    def get_max_y(self):
        return max(np.max(self.dataset[0][:, 1]), np.max(self.dataset[1][:, 1]))
        
    def attach_dataset(self):
        return np.append(self.dataset[0], self.dataset[1], axis=0)
    
    def update_upper_lower(self):
        isupper_0 = self.get_upper_lower()
        if isupper_0 == -1:
            tmp=self.dataset[0]
            self.dataset[0] = self.dataset[1]
            self.dataset[1] = tmp
        
        
        

if __name__ == "__main__":
    filepath = "../data/DataSetA"
    filename = "../data/DataSetA/DataSetA-1000.dat"
    A = Data(filename)
    A.read()
    A.plot()
    print(A.attach_dataset())