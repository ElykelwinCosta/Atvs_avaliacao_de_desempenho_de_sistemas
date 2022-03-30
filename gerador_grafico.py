import matplotlib.pyplot as plt
import os
import pandas as pd

diretorio = 'output-bench-primos'
files_list = os.listdir(diretorio)
temp = []
for file in files_list:
    with open('{}\{}'.format(diretorio, file), 'r') as f2:
        data = f2.read().split()
        temp.append([int(data[5]), int(data[6]), float(int(data[8])/1000), float("{:.2f}".format(float(data[9]) * 100))])

df = pd.DataFrame(temp, columns=['NumThreads', 'NumeroMaximo', 'ElapsedTime', 'MeanUtilization'])
df.sort_values(by="NumThreads", inplace=True)
print(df)

def grafico_time(NumThreads, ElapsedTime):
    x = NumThreads
    y = ElapsedTime
    width = 0.7

    fig, ax = plt.subplots()
    bar = ax.bar(x, y, width, label = "Tempo decorrido")
    ax.plot(x, y, color='red')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Tempo decorrido (Segundos)')
    ax.set_xlabel('Número de threads')
    ax.set_title('Tempo decorrido considerando número de threads')
    ax.set_xticks(x)
    ax.bar_label(bar, fmt="%.f")
    ax.legend()
    plt.show()


def grafico_mean_cpu(NumThreads, MeanUtilization):
    x = NumThreads
    y = MeanUtilization
    width = 0.7

    fig, ax = plt.subplots()
    bar = ax.bar(x, y, width, label = "Porcentagem média de uso da CPU")
    ax.plot(x, y, color='red')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Média de uso da CPU (%)')
    ax.set_xlabel('Número de threads')
    ax.set_title('Porcentagem média de uso da CPU considerando número de threads')
    ax.set_xticks(x)

    ax.legend()
    plt.show()

grafico_time(df.NumThreads, df.ElapsedTime)
grafico_mean_cpu(df.NumThreads, df.MeanUtilization)