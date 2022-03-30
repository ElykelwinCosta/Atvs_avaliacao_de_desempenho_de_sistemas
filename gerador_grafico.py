import matplotlib.pyplot as plt
import os
import pandas as pd


def carregar_dados(nome_sub_dir):
    diretorio = 'output-bench-primos\{}'.format(nome_sub_dir)
    files_list = os.listdir(diretorio)
    temp = []
    for file in files_list:
        with open('{}\{}'.format(diretorio, file), 'r') as f2:
            data = f2.read().split()
            temp.append(
                [int(data[5]), int(data[6]), float(int(data[8]) / 1000), float("{:.2f}".format(float(data[9]) * 100))])

    df = pd.DataFrame(temp, columns=['NumThreads', 'NumeroMaximo', 'ElapsedTime', 'MeanUtilization'])
    return df


def grafico_time():
    df = carregar_dados("ElapsedTime")
    df.sort_values(by="NumThreads", inplace=True)
    x = df.NumThreads
    y = df.ElapsedTime
    width = 0.7

    fig, ax = plt.subplots()
    bar = ax.bar(x, y, width, label="Tempo decorrido")
    ax.plot(x, y, color='red')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Tempo decorrido (Segundos)')
    ax.set_xlabel('Número de threads')
    ax.set_title('Tempo decorrido considerando número de threads')
    ax.set_xticks(x)
    ax.bar_label(bar, fmt="%.f")
    ax.legend()
    plt.show()


def grafico_mean_cpu():
    df = carregar_dados("ElapsedTime")
    df.sort_values(by="NumThreads", inplace=True)
    x = df.NumThreads
    y = df.MeanUtilization
    width = 0.7

    fig, ax = plt.subplots()
    bar = ax.bar(x, y, width, label="Porcentagem média de uso da CPU")
    ax.plot(x, y, color='red')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Média de uso da CPU (%)')
    ax.set_xlabel('Número de threads')
    ax.set_title('Porcentagem média de uso da CPU considerando número de threads')
    ax.set_xticks(x)

    ax.legend()
    plt.show()


def grafico_escalabilidade():
    df = carregar_dados("Escalabilidade")
    df.sort_values(by="NumeroMaximo", inplace=True)
    x = df.NumeroMaximo / 100000
    y = df.ElapsedTime
    y2 = [((k - df.NumeroMaximo[0]) / df.NumeroMaximo[0] * 100) for k in df.NumeroMaximo]
    y3 = [((k - df.ElapsedTime[0]) / df.ElapsedTime[0] * 100) for k in df.ElapsedTime]

    width = 0.7

    fig, ax = plt.subplots()
    bar = ax.bar(x, y, width, label="Tempo decorrido")
    ax.plot(x, y2, color='orange', label="Porcentagem de aumento da carga em relação à primeira execução")
    ax.plot(x, y3, color='green', label="Porcentagem de aumento do tempo em relação à primeira execução")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Tempo decorrido (Segundos)')
    ax.set_xlabel('Número Máximo X 100000')
    ax.set_title('Tempo decorrido considerando número máximo')
    ax.set_xticks(x)
    ax.bar_label(bar)
    ax.legend()
    plt.show()


grafico_time()
grafico_mean_cpu()
grafico_escalabilidade()
