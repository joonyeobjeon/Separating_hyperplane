# Separate hyperplane with Linear programing
This assignment was made as a term project for the class of Optimal Nonlinear Design for the 2021-1 semester. The goal of this task is to separate the dummy of points using a hyperplane. There are two types of datasets in this task. One can split two dummy with a linear-hperplane and the other can split two dummy with a non-linear-hyperplane.
![linear_dummy](./images/Figure_1.png)
![nonlinear_dummy](./images/Figure_2.png)

The example of dummies(datasetA-5000, datasetB-5000)


## Installation
Before anything else, you must have the cplex-env virtual environment installed. Everything proceeds under the assumption that the cplex-env virtual environment is installed.

```
# You must be on the enviroment of `cplex`
pip setup.py install
pip install -e .
```

## Results
### DataSetA-1000.dat
![linear_hyperplane1](./images/Figure_3.png)
### DataSetB-1000.dat
![nonlinear_hyperplane1](./images/Figure_4.png)
### DataSetA-2000.dat
![linear_hyperplane2](./images/Figure_5.png)
### DataSetB-2000.dat
![nonlinear_hyperplane2](./images/Figure_6.png)
### DataSetA-3000.dat
![linear_hyperplane1](./images/Figure_7.png)
### DataSetB-3000.dat
![nonlinear_hyperplane1](./images/Figure_8.png)
### DataSetA-4000.dat
![linear_hyperplane1](./images/Figure_9.png)
### DataSetB-4000.dat
![nonlinear_hyperplane1](./images/Figure_10.png)
### DataSetA-5000.dat
![linear_hyperplane1](./images/Figure_11.png)
### DataSetB-5000.dat
![nonlinear_hyperplane1](./images/Figure_12.png)

## Example
To check the generalized code, I tried to obtain the hyperplane separation by changing only the order using an arbitrary dumy.
![nonlinear_hyperplane](./images/Figure_13.png)
### Order 1
![nonlinear_hyperplane1](./images/Figure_14.png)
### Order 2
![linear_hyperplane1](./images/Figure_15.png)
### Order 5
![nonlinear_hyperplane1](./images/Figure_16.png)