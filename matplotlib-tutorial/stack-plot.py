from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1,2,3,4,5,6,7,8,9]

# player points
p1 = [1,2,3,3,4,4,4,4,4]
p2 = [1,1,1,1,2,2,2,3,4]
p3 = [1,1,1,2,2,2,3,3,3]

labels = ["p1",'p2','p3']


plt.stackplot(minutes, p1,p2,p3, labels=labels)

plt.legend(loc="upper left")
plt.xlabel("Minutes")
plt.ylabel("Total Points")

plt.title("Stak plot")
plt.show()