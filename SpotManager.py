import json
from tabulate import tabulate
from termcolor import colored
from MyTypes import *

class SpotManager:
    SpotData = namedtuple('SpotData', ['currency', 'open_date', 'buy_price', 'amount', 'sell_price', 'profit', 'close_date'])

    def __init__(self, file_path):
        self.file_path = file_path
        self.spots = []
        self.read_from_json()

    def __del__(self):
        self.save_to_json()

    def read_from_json(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.spots = [self.SpotData(spot_dict['currency'], spot_dict['open_date'], spot_dict['buy_price'], spot_dict['amount'],
                                            spot_dict['sell_price'], spot_dict['profit'], spot_dict['close_date'])
                              for spot_dict in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Could not read data from {self.file_path}. Starting with empty list.")


    def save_to_json(self):
        with open(self.file_path, 'w') as f:
            data = [spot._asdict() for spot in self.spots]
            json.dump(data, f, default=str, indent=4)

    def add_trade(self):
        currency = input('Enter currency: ')
        open_date = input('Enter open date: ')
        buy_price = float(input('Enter buy price: '))
        amount = float(input('Enter amount: '))
        sell_price = 0
        close_date = ''
        profit = 0
        new_trade = SpotData(currency, open_date, buy_price, amount, sell_price, profit, close_date)
        self.spots.append(new_trade)
        self.save_to_json()
        print('New trade added successfully.')

    def print_open_positions(self):
        table = []
        for i, trade in enumerate(self.spots):
            if not trade.close_date:
                if trade.profit and trade.profit > 0:
                    pnl_colored = colored(str(trade.profit), "green")
                elif trade.profit and trade.profit < 0:
                    pnl_colored = colored(str(trade.profit), "red")
                else:
                    pnl_colored = "-"
                table.append([i+1, trade.currency, trade.open_date, trade.buy_price, trade.amount, pnl_colored])
        headers = ["#", "Currency", "Open Date", "Buy Price", "Amount", "Profit"]
        print(tabulate(table, headers, tablefmt="fancy_grid", numalign="center"))

    def close_trade(self):
        self.print_open_positions()
        trade_index = input("Enter the number of the trade to close: ")
        try:
            trade_index = int(trade_index)
            trade = self.spots[trade_index - 1]
            if trade.close_date != '':
                print(f"Trade {trade_index} already closed on {trade.close_date}")
                return
            sell_price = float(input("Enter the sell price for the trade: "))
            close_date = input("Enter the close date for the trade (in format dd.mm): ")
            profit = ((trade.amount / trade.buy_price) * sell_price) - trade.amount
            trade = trade._replace(close_date=close_date, sell_price=sell_price, profit=profit)
            self.spots[trade_index - 1] = trade
            self.save_to_json()
            print(f"Trade {trade_index} closed successfully.")
        except (IndexError, ValueError):
            print("Invalid input. Please try again.")
    
    def print_all(self):
        headers = ['Currency', 'Open Date', 'Buy Price', 'Amount', 'Sell Price', 'Profit', 'Close Date']
        rows = []
        for spot in self.spots:
            row = [spot.currency, spot.open_date, spot.buy_price, spot.amount, spot.sell_price, spot.profit, spot.close_date]
            if spot.sell_price is None:
                row[4] = colored('Open', 'green')
                row[5] = colored('Open', 'green')
            elif spot.profit < 0:
                row[4] = colored(row[4], 'red')
                row[5] = colored(row[5], 'red')
            else:
                row[4] = colored(row[4], 'green')
                row[5] = colored(row[5], 'green')
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
    
    def print_sorted_by_profit_descending(self):
        sorted_spots = sorted(self.spots, key=lambda x: x.profit, reverse=True)
        headers = ["Currency", "Open Date", "Buy Price", "Amount", "Sell Price", "Profit", "Close Date"]
        table = []
        for spot in sorted_spots:
            color = 'green' if spot.profit >= 0 else 'red'
            row = [spot.currency, spot.open_date, spot.buy_price, spot.amount, spot.sell_price, colored(spot.profit, color), spot.close_date]
            table.append(row)
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    
    def print_sorted_by_profit_ascending(self):
        spots_sorted = sorted(self.spots, key=lambda x: x.profit)
        table = []
        for i, spot in enumerate(spots_sorted):
            color = "red" if spot.profit < 0 else "green"
            table.append([i+1, spot.currency, spot.open_date, spot.buy_price, spot.amount, spot.sell_price, spot.profit, spot.close_date, colored(spot.profit, color)])
        print(tabulate(table, headers=["No.", "Currency", "Open Date", "Buy Price", "Amount", "Sell Price", "Profit", "Close Date", "Profit Color"], tablefmt="fancy_grid"))

    def print_closed_positions(self):
        headers = ['Currency', 'Open Date', 'Buy Price', 'Amount', 'Sell Price', 'Profit', 'Close Date']
        rows = []
        for spot in self.spots:
            if spot.close_date != '':
                pnl_color = 'green' if spot.profit >= 0 else 'red'
                row = [spot.currency, spot.open_date, spot.buy_price, spot.amount, spot.sell_price, colored(spot.profit, pnl_color), spot.close_date]
                rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid', numalign='center', stralign='center'))