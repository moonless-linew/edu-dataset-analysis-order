"""
Файл с функциями анализа
"""
import matplotlib.pyplot as plt
import pandas as pd


def average_bar(key, number, data_frame):
    """
    Функция для построения графика среднего
    количественного параметра от количественного

    :param key: Качественный параметр
    :param number: Количественный параметр
    :param data_frame: Таблица
    :return: График на экран, график в output
    """
    df_graph = data_frame.groupby(key, as_index=False)[number].mean()
    plt.figure(figsize=(15, 8))
    plt.bar(df_graph[key], df_graph[number], color="r")

    plt.xlabel(key, fontsize=16)
    plt.xticks(rotation=45)
    plt.ylabel(number, fontsize=16)
    plt.title(f"Average {number} of {key}", fontsize=18)
    plt.savefig("../output/average_bar.png")
    plt.show()
