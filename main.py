
import matplotlib.pyplot as plt


# 1

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
#plt.plot(x, y)
plt.title("Simple Line Plot")
plt.show()



# 2

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels)
plt.title("Simple Pie Chart")
plt.show()




import numpy as np


# 1
arr1 = np.arange(0 , 15 , 3 )
print("Number one = "+ str(arr1))
print("\n")

#2
arr2 = np.zeros((3,3))
print("Number two = " + "\n" + str(arr2))
print("\n")

#3
arr3 = np.ones((4,5))
print(arr3)
print("\n")



