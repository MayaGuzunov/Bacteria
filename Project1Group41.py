#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 13:19:14 2021

@author: mayaguzunov
"""
import numpy as np #Used for the looping and if statements
import matplotlib.pyplot as plt

def dataLoad(filename):
    newdata=np.empty((0,3),int) #An empty array made for the output values that will be returned
    data=np.loadtxt(filename, delimiter=" ") #Imported the txt file as 2D array(Nx3) from the same folder where the program was saved
    valid_row=True #Identified the valid_row for the boolean function used later
    for row in range(data.shape[0]): #Used to make the program run through all of the rows in the matrix
        valid_row=True #Created in the loop to renew the variable as true on each cycle or row.
        if (data[row,0]<=10 or data[row,0]>=60): #Checks if the temperature is not in the range, to be included in the final matrix if the statemtnt is False
            print('Temperature out of the range 10-60 in line {}'.format(row)) #Prints the error message and the line where the error is
            valid_row=False #Used to skip the false row 
        if (data[row,1]<=0): #Checks if the column is negative 
            print('Growth rate is not positive in line {}'.format(row)) #Prints the error message and the row
            valid_row=False #Used to skip the false row
        if(np.all(data[row,2]!=[1,2,3,4])): #Checks if the bactheria column is not equal with at least one value from [1,2,3,4]
            print('Invalid bacteria name in line {}'.format(row)) #Prints the error message
            valid_row=False #Used to skip the false row
        if valid_row:
            newdata=np.vstack((data[row,:],newdata)) #Used to create the new matrix in columns where the boolean valid_row == True
    return newdata #Return the updated array with the correct values

print(dataLoad("test.txt"))

def dataStatistics(data, statistic):
    if statistic=='Mean temperature':
        result=np.mean(data[:,0])
    elif statistic=='Mean growth rate':
       result=np.mean(data[:1])
    elif statistic=='Std Temperature':
       result = np.std(data[:,0])
    elif statistic=='Std Growth rate':
        result=np.std(data[:,1])
    elif statistic=='Rows':
        result= np.shape(data)[0]
    elif statistic=='Mean Cold Growth rate':
        temp = data[:,0]
        result = np.mean(temp[temp < 20])
    elif statistic=='Mean Hot Growth rate':
        temp=data[:,0]
        result=np.mean(temp[temp>50])

        return result
print(dataStatistics(dataLoad("test.txt"), "Mean Temperature"))


def dataPlot(data):

#1st graph
 bacteria=data[:,2]           #state that bacteria is the data of the 3rd column
 number1=np.sum(bacteria==1)    #number of the bacteria "1" is the sum of the bacteria 1.
 number2=np.sum(bacteria==2)
 number3=np.sum(bacteria==3)
 number4=np.sum(bacteria==4)
 height = np.array([number1,number2,number3,number4])   #Create heights of bars
 tick_label = np.array(['Salmonella enterica','Bacillus cereus','Listeria','Brochothrix thermosphacta'])  #Create labels for bars 
 plt.bar(tick_label, height, width = 0.8, color = ['blue'])         # plotting a bar chart
 plt.xlabel('Bacteria type')  #Set the x-axis label
 plt.ylabel('Number of bacteria')   #Set the y-axis label
 plt.title('Number of bacteria for each type')  #Set the label of the graph
 plt.show()
    
    
#2nd graph
 data = data[np.argsort(data[:,0], axis=0)]
 bacteria = data[:,2]
 x1=data[:,0]#, bacteria==1                          #Create x,y- values
 x1 = x1[bacteria==1]
 y1=data[:,1]#, bacteria==1) 
 y1 = y1[bacteria==1]              #Do i just do it like that or do i create a loop here?                         #Create x,y- values
 x2=data[:,0]#, bacteria==2)                          #Create x,y- values
 x2=x2[bacteria==2]
 y2=data[:,1]#, bacteria==2) 
 y2=y2[bacteria==2]  
 x3=data[:,0]#, bacteria==3)                          #Create x,y- values
 x3=x3[bacteria==3]
 y3=data[:,1]#, bacteria==3) 
 y3=y3[bacteria == 3]  
 x4=data[:,0]#, bacteria==4)                          #Create x,y- values
 x4=x4[bacteria==4]
 y4=data[:,1]#, bacteria==4) 
 y4=y4[bacteria == 4]  
 plt.plot(x1,y1,'b-')                  #Do i just do it like that or do i create a loop here?
 plt.plot(x2,y2,'g-')
 plt.plot(x3,y3,'m-')
 plt.plot(x4,y4,'r-')
 plt.title('Growth rate of the bacteria depending on the temperature') #Set the title of the graph
 plt.xlabel('Temperature')        #Set the x-axis label
 plt.ylabel('Growth rate')       
 plt.legend (tick_label)
 plt.grid(True)             
 plt.show()

 
dataPlot(dataLoad("test.txt"))
         