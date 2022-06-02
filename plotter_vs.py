import os

import matplotlib.pyplot as plt
import pandas as pd


class parsers:
    def __init__(self):
        self.table = {}
        for item in (os.listdir(".")):
            if os.path.isdir(item) and os.path.isdir(item) not in self.table.keys():
                self.table[item.split()[0]] = []

    def vina_score(self):
        for k, v in self.table.items():
            with open('Summary_chart.txt', 'r') as vina:
                for line in vina:
                    if line.__contains__(k):
                        # self.table[k] =
                        self.table[k] = [float(line.split()[1])]

    def post_docking(self):
        for k, v in self.table.items():
            with open('Summary_post_docking.txt', 'r') as post:
                for line in post:
                    if line.__contains__(k):
                        self.table[k] += [float(line.split()[12])]
                        self.table[k] += [float(line.split()[14])]
                        self.table[k] += [float(line.split()[2]) / 100]

    def GetDf(self):
        return self.table


test = parsers()
test.vina_score()
test.post_docking()

df = pd.DataFrame.from_dict(test.GetDf(), orient='index')
df.index = df.index.str.split(pat="_").str[0]
df[0] = df[0].abs()
df[3] = df[3].abs()

ax = df.plot.bar(edgecolor='black')
ax.set_ylim([0, 8])
plt.xticks(rotation=45)
plt.ylabel("Score\n (Final score/100)")
ax.legend(['vina score', 'avg RMSD', 'SD RMSD', 'Final Score'], frameon=False, ncol=2, prop={'size': 10})
plt.show()
plt.close()
