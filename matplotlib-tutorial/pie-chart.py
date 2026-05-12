from matplotlib import pyplot as plt

slices = [60,40,20,10]
labels = ["L1","L2", "L3","L4"]
colors=["#008ed592", "#28b395a9", "#99c4219b", "#b115a9a9"]

plt.pie(slices,labels=labels,colors=colors, wedgeprops={"edgecolor": "#000000"})

plt.legend()

plt.title("My Awesome pie chart")
plt.show()
