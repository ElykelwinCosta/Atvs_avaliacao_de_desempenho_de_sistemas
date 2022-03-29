import matplotlib.pyplot as plt
import os
import pandas as pd

diretorio = 'output-bench-primos'
files_list = os.listdir(diretorio)
temp = []
for file in files_list:
    with open('{}\{}'.format(diretorio, file), 'r') as f2:
        data = f2.read().split()
        temp.append([int(data[5]), data[6], data[8], "{:.2f}".format(float(data[9]) * 100)])

df = pd.DataFrame(temp, columns=['NumThreads', 'NumeroMaximo', 'ElapsedTime', 'MeanUtilization'])
print(df.sort_values(by="NumThreads", inplace=True))

x = df.NumThreads
y = df.ElapsedTime
height=0.5
fig, ax = plt.subplots()
bar = ax.bar(x, y, 5bottom=None, align="center")
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Elapsed Time')
# ax.set_title('Scores by group and gender')
# ax.set_ticks(x)
ax.legend()

fig.tight_layout()

plt.show()
