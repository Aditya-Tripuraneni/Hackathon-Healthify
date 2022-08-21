import sqlite3
import os
from matplotlib import pyplot as plt
import datetime
from datetime import date

plt.style.use('ggplot')


USER_PATH = os.path.join(os.getcwd(), "Database")


def send_weight_data(query, data):
    connection = sqlite3.connect(os.path.join(USER_PATH, "health.db"))
    cur = connection.cursor()
    weight = int(data)
    cur.execute(f"INSERT INTO {query} VALUES (:payed)", {"payed": weight})
    connection.commit()
    connection.close()

def get_data(query):
    connection = sqlite3.connect(os.path.join(USER_PATH, "health.db"))
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM {query}")
    data = cur.fetchall()
    connection.commit()
    connection.close()
    return data


def graph_weight():
    weight_data = get_data("weight")
    plt.plot(range(1, len(weight_data) + 1), weight_data)
    plt.title(f"History of Weight (kg) ")
    plt.xlabel("Weight Entry")
    plt.ylabel("Weight (Kg)")
    plt.show()






