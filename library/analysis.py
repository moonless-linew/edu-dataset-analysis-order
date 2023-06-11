"""
Файл с функциями анализа
"""
import matplotlib.pyplot as plt
import pandas as pd


def top_by_rating(count, data_frame, reverse=False):
    """
    Функция для определения топа ноутбуков по рейтингу

    :param count: Количество в топе
    :param data_frame: Таблица
    :param reverse: В каком порядке отсортирован топ
    :return out: Словарь ноутбуков
    """
    df_sorted = data_frame.sort_values(["Rating", "Company"],
                                       ascending=[reverse, True]).head(count)

    df_sorted = df_sorted[["Company", "TypeName", "Memory", "OpSys", "Rating"]]
    out = []
    sorted_values_list = df_sorted.values.tolist()
    keys = df_sorted.keys()
    for i in range(len(sorted_values_list)):
        dict_of_vals = {}
        for j in range(len(keys)):
            dict_of_vals[keys[j]] = sorted_values_list[i][j]
        out.append(dict_of_vals)
    return out


def laptop_by_price(count, data_frame, reverse=False):
    """
    Функция для определения самых дорогих
    и дешевых ноутбуков

    :param count: Количество в топе
    :param data_frame: Таблица
    :param reverse: В каком порядке отсортирован топ
    :return out: Словарь ноутбуков
    """
    df_sorted = data_frame.sort_values(["Price_euros", "Company"],
                                       ascending=[reverse, True]).head(count)
    df_sorted = df_sorted[["Company", "TypeName", "Memory", "OpSys", "Rating", "Price_euros"]]

    out = []
    sorted_values_list = df_sorted.values.tolist()
    keys = df_sorted.keys()
    for i in range(len(sorted_values_list)):
        dict_of_vals = {}
        for j in range(len(keys)):
            dict_of_vals[keys[j]] = sorted_values_list[i][j]
        out.append(dict_of_vals)
    return out


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


def prices_of_company(company, data_frame):
    """
    Функция для вычисления средней цены
    разных моделей ноутбуков компании

    :param company: Название компании
    :param data_frame: Таблица
    :return: График на экран, график в output
    """
    df_sorted = data_frame.loc[data_frame["Company"] == company]
    df_graph = df_sorted.groupby("Product", as_index=False)["Price_euros"].mean()

    plt.figure(figsize=(15, 8))
    plt.bar(df_graph["Product"], df_graph["Price_euros"], color="r")

    plt.xlabel("Product", fontsize=16)
    plt.xticks(rotation=90)
    plt.ylabel("Average price", fontsize=16)
    plt.title(company, fontsize=18)

    plt.savefig("../output/price_of_company.png")
    plt.show()


def corr_matrix(data_frame):
    """
    Функция для построения матрицы корреляций

    :param data_frame: Таблица
    :return: Матрица корреляций на экран, матрица корреляций в output
    """
    corr = data_frame.corr()
    fig, ax = plt.subplots(figsize=(11, 9))
    im = ax.imshow(corr, interpolation='nearest')
    fig.colorbar(im, orientation='vertical', fraction=0.05)

    plt.xticks(range(data_frame.select_dtypes(['number']).shape[1]),
               data_frame.select_dtypes(['number']).columns,
               fontsize=14)
    plt.yticks(range(data_frame.select_dtypes(['number']).shape[1]),
               data_frame.select_dtypes(['number']).columns,
               fontsize=14)

    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            ax.text(j, i, round(corr.to_numpy()[i, j], 3),
                    ha="center", va="center", color="black")
    plt.title('Матрица корреляций', fontsize=16)
    plt.show()
    plt.savefig("../output/corr_matrix.png")
