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
        

if __name__ == "__main__":
    filepath = "../data/DataSetA"
    filename = "../data/DataSetA/DataSetA-1000.dat"
    A = Data(filename)
    A.read()
    A.plot()
    print(A.attach_dataset())