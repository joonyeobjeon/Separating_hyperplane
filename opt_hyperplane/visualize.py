from opt_hyperplane.io.dataset import Data
import matplotlib.pyplot as plt
import numpy as np


class Visualize(object):
    def __init__(self, data: Data):
        self.data = data
        self.coefficient = []
        self.order = None
        
    def set_scatter(self):
        plt.scatter(self.data.dataset[0][:,0], self.data.dataset[0][:,1], c="red")
        plt.scatter(self.data.dataset[1][:,0], self.data.dataset[1][:,1], c="blue")
    
    def set_coefficient(self, coeff):
        self.coefficient = coeff
    
    def set_order(self, order: int):
        self.order = order
    
    def get_order_function_value(self, x: np.array):
        for order in range(self.order):
            if order == 0:
                f_value = self.coefficient[order] * np.power(x, order+1)
            else:
                f_value = f_value + self.coefficient[order] * np.power(x, order+1)
        f_value = -f_value - self.coefficient[self.order+1]
        f_value = f_value / self.coefficient[self.order]
        return f_value
    
    def set_plot(self):
        minx = self.data.get_min_x()
        maxx = self.data.get_max_x()
        x=np.arange(minx, maxx, (maxx-minx)/2000)
        y=self.get_order_function_value(x)
        plt.plot(x, y)
        
    def show_plot(self):
        minx = np.floor(self.data.get_min_x())
        maxx = np.ceil(self.data.get_max_x())
        miny = np.floor(self.data.get_min_y())
        maxy = np.ceil(self.data.get_max_y())
        print(minx, miny)
        plt.xlim([minx, maxx])
        plt.ylim([miny, maxy])
        plt.show()