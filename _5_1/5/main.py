import sqlite3
import matplotlib.pyplot as plt

def get_data(start_date, end_date):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data WHERE date BETWEEN ? AND ? ORDER BY date ", (start_date, end_date))
    res = cur.fetchall()
    con.close()
    dates = [res[i][0] for i in range(len(res))]
    prices = [res[i][1] for i in range(len(res))]
    return dates, prices


def plot_dollar_exchange_rate(dates, prices):
    plt.figure(figsize=(15, 10))
    plt.plot(dates, prices, marker='o', color='b', linestyle='-')
    plt.title('Dollar Exchange Rate')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.show()

# Пример использования функции
# dates = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04']
# prices = [74.5, 75.0, 74.8, 75.2]

dates, prices = get_data('2022-01-02', '2023-01-02')

plot_dollar_exchange_rate(dates, prices)
