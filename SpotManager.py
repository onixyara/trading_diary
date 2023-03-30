from collections import namedtuple
import json
from typing import List
from collections import namedtuple
from datetime import datetime
import json
from tabulate import tabulate
from termcolor import colored

SpotData = namedtuple('SpotData', ['currency', 'open_date', 'buy_price', 'amount', 'sell_price', 'profit', 'close_date'])

class SpotManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.spot_data = []
        self.read_from_json()

    def __del__(self):
        self.save_to_json()

    def read_from_json(self):
        try:
            with open(self.file_path) as file:
                data = json.load(file)
                self.spot_data = [SpotData(**t) for t in data]
        except FileNotFoundError:
            pass

    def save_to_json(self):
        with open(self.file_path, 'w') as file:
            json.dump([t._asdict() for t in self.spot_data], file, indent=4, sort_keys=True)

    def add_trade(self):
        currency = input("Enter currency: ")
        open_date = input("Enter open date (YYYY-MM-DD): ")
        buy_price = float(input("Enter buy price: "))
        amount = float(input("Enter amount: "))
        spot_trade = SpotData(currency=currency, open_date=open_date, buy_price=buy_price, amount=amount,
                              sell_price=0, profit=0, close_date='-')
        self.spot_data.append(spot_trade)

    def close_trade(self):
        for i, trade in enumerate(self.spot_data):
            if trade.close_date == '-':
                print(f"{i}. {trade.currency} - {trade.amount} {trade.currency} @ {trade.buy_price}")
        index = int(input("Select trade to close: "))
        trade = self.spot_data[index]
        sell_price = float(input("Enter sell price: "))
        profit = (sell_price - trade.buy_price) * trade.amount
        trade = trade._replace(sell_price=sell_price, profit=profit, close_date=input("Enter close date (YYYY-MM-DD): "))
        self.spot_data[index] = trade

    def print_all(self):
        for i, trade in enumerate(self.spot_data):
            buy_sell_diff = trade.sell_price - trade.buy_price
            pnl_colored = colored(f"{trade.profit:+.2f}", 'green' if trade.profit >= 0 else 'red')
            if buy_sell_diff < 0:
                bs_diff_colored = colored(f"{buy_sell_diff:+.2f}", 'red')
            else:
                bs_diff_colored = f"{buy_sell_diff:.2f}"
            print(f"{i}. {trade.currency}\t{trade.open_date}\t{trade.buy_price:.2f}\t{trade.amount}\t{trade.sell_price:.2f}\t{bs_diff_colored}\t{pnl_colored}\t{trade.close_date}")

    def print_sorted_by_pnl(self):
        sorted_spots = sorted(self.spots, key=lambda spot: spot.profit or 0, reverse=True)
        table_data = [[i+1, spot.currency, spot.open_date.strftime('%d.%m.%Y'), spot.buy_price, spot.amount,
                       spot.sell_price or "-", spot.close_date.strftime('%d.%m.%Y') if spot.close_date else "-",
                       spot.profit or "-"] for i, spot in enumerate(sorted_spots)]

        headers = ["#", "Currency", "Open Date", "Buy Price", "Amount", "Sell Price", "Close Date", "Profit"]
        print(tabulate(table_data, headers=headers))

    def print_sorted_by_pnl_low_to_high(self):
        sorted_spots = sorted(self.spots, key=lambda spot: spot.profit or 0)
        table_data = [[i+1, spot.currency, spot.open_date.strftime('%d.%m.%Y'), spot.buy_price, spot.amount,
                       spot.sell_price or "-", spot.close_date.strftime('%d.%m.%Y') if spot.close_date else "-",
                       spot.profit or "-"] for i, spot in enumerate(sorted_spots)]

        headers = ["#", "Currency", "Open Date", "Buy Price", "Amount", "Sell Price", "Close Date", "Profit"]
        print(tabulate(table_data, headers=headers))

    def print_open_positions(self):
        table_data = [[i+1, spot.currency, spot.open_date.strftime('%d.%m.%Y'), spot.buy_price, spot.amount]
                      for i, spot in enumerate(self.spots) if spot.close_date is None]

        headers = ["#", "Currency", "Open Date", "Buy Price", "Amount"]
        print(tabulate(table_data, headers=headers))
    
    def print_closed_positions(self):
        table_data = [[i+1, spot.currency, spot.open_date.strftime('%d.%m.%Y'), spot.buy_price, spot.amount,
                       spot.sell_price, spot.close_date.strftime('%d.%m.%Y'), spot.profit] for i, spot in enumerate(self.spots) if spot.close_date]
        headers = ["#", "Currency", "Open Date", "Buy Price", "Amount", "Sell Price", "Close Date", "Profit"]
        print(tabulate(table_data, headers=headers))