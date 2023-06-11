import sys
import pandas as pd
from PyQt5 import QtWidgets


def setup():
    ui.top_type.addItems(top_types)
    ui.count_parameter.addItems(count_of_laptops_parameters)
    ui.key_parameter.addItems(key)
    ui.number_parameter.addItems(number)
    ui.company.addItems(companies)
    ui.memory_type.addItems(memory_type)
    ui.number_parameter_memory.addItems(number_memory)
    ui.build_top.clicked.connect(lambda: build_top(ui.top_type.currentText()))
    ui.count_laptops.clicked.connect(lambda: count_of_laptops(ui.count_parameter.currentText(), df))
    ui.correlation.clicked.connect(lambda: corr_matrix(df))
    ui.average_bar.clicked.connect(
        lambda: average_bar(ui.key_parameter.currentText(), ui.number_parameter.currentText(), df))
    ui.average_price.clicked.connect(lambda: prices_of_company(ui.company.currentText(), df))
    ui.average_memory.clicked.connect(
        lambda: memory_to_number_param(ui.memory_type.currentText(), ui.number_parameter_memory.currentText(), df))


def build_top(top_type):
    ui.top_list.clear()
    top_dict = dict()
    if top_type == "Rating":
        top_dict = top_by_rating(ui.max_number.value(), df, ui.reverse.isChecked())
    elif top_type == "Price_euros":
        top_dict = laptop_by_price(ui.max_number.value(), df, ui.reverse.isChecked())
    for i in range(len(top_dict)):
        current = top_dict[i]
        ui.top_list.addItem(
            f"{current['Company']}-{current['Product']} ({current[top_type]})")


if __name__ == "__main__":
    sys.path.insert(0, "..")
    from library.main import Ui_MainWindow
    from library.analysis import *

    df = pd.read_csv("../data/data.csv", sep=";")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    setup()
    MainWindow.show()
    sys.exit(app.exec_())
