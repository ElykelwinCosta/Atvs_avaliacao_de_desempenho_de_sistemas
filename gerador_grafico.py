import matplotlib.pyplot as plt
import os
import pandas as pd


def carregar_dados_primos(nome_dir):
    diretorio = nome_dir
    files_list = os.listdir(diretorio)
    temp = []
    for file in files_list:
        with open('{}\{}'.format(diretorio, file), 'r') as f2:
            data = f2.read().split()
            temp.append([int(data[5]), int(data[6]), float(int(data[8]) / 1000), float("{:.2f}".format(float(data[9]) * 100))])

    df = pd.DataFrame(temp, columns=['NumThreads', 'NumeroMaximo', 'ElapsedTime', 'MeanUtilization'])
    return df


def carregar_dados_memoria(nome_dir):
    diretorio = nome_dir
    files_list = os.listdir(diretorio)
    temp = []
    for file in files_list:
        with open('{}\{}'.format(diretorio, file), 'r') as f2:
            data = f2.read().split()
            temp.append([int(data[7]), int(data[8]), int(int(data[9]) / 100000000), int(data[10]), int(data[12])])

    df = pd.DataFrame(temp, columns=['KBinMemory', 'ArraySize', 'SearchRepetitions', 'PopulateTime', 'TotalTime'])
    return df


def grafico_time():
    df = carregar_dados_primos("output-bench-primos\ElapsedTime")
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
    df = carregar_dados_primos("output-bench-primos\ElapsedTime")
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
    df = carregar_dados_primos("output-bench-primos\Escalabilidade")
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


def grafico_tempo_busca():
    df = carregar_dados_memoria("output-bench-memoria/range_1_a_1000000")
    df.sort_values(by="KBinMemory", inplace=True)
    fig, ax = plt.subplots()

    x = ["1", "10", "100", "1000", "10000", "100000", "1000000"]
    y = df.TotalTime
    y2 = [(int((k - df.KBinMemory[0]) / df.KBinMemory[0])/100) for k in df.KBinMemory]
    y3 = [((k - df.TotalTime[0]) / df.TotalTime[0] * 100) for k in df.TotalTime]

    ax.plot(x, y2, color='orange', label="Porcentagem de aumento do array em relação à primeira execução /100")
    ax.plot(x, y3, color='green', label="Porcentagem de aumento do tempo em relação à primeira execução")

    width = 0.7
    #bar = ax.bar(x, y, width, label="Tempo decorrido")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Tempo de busca')
    ax.set_xlabel('Tamanho do array (Kbytes)')
    ax.set_title('Tempo decorrido considerando tamanho do array')
    ax.set_xticks(x)
    #ax.bar_label(bar, fmt="%.f")
    ax.legend()
    plt.show()


grafico_time()
grafico_mean_cpu()
grafico_escalabilidade()
grafico_tempo_busca()