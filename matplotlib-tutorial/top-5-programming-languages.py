from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

df_dev_survery =  pd.read_csv("./data/data.csv")
print(df_dev_survery)
lang_counter = Counter()

ids = df_dev_survery["Responder_id"]
lang_resp = df_dev_survery["LanguagesWorkedWith"]

for lang in lang_resp:
  lang_counter.update(lang.split(";"))

slices = []
labels = []
explode = [0.05,0,0,0.05,0]

for item in lang_counter.most_common(5):
  slices.append(item[1])
  labels.append(item[0])



print(slices)
print(labels)

# plot pie chart top 5 programming languages
plt.pie(slices, labels=labels, explode=explode, startangle=100, autopct="%1.1f%%", shadow=True, 
        )

plt.title("Top 5 programming languages 2025")
plt.legend(loc="upper right")
plt.show()
