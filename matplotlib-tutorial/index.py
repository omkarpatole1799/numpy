from matplotlib import pyplot as plt

dev_x = [25,26,27,29,30]

dev_y =  [1000, 2000, 2040, 4500, 3040]

plt.plot(dev_x, dev_y)

plt.title("Salay by age (INR)")
plt.xlabel("Age")
plt.ylabel("Salary (INR)")

plt.show()