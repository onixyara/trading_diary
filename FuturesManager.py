import json
from tabulate import tabulate
from termcolor import colored
from MyTypes import *

class FuturesManager:
    def __init__(self, filename):
        self.filename = filename
        self.trades = []
        self.read_from_json()
        self.my_balance = 3870

    def add_trade(self):
        # Collect input from the user
        open_date = input("Enter the open date: ")
        open_time = input("Enter the open time: ")
        long_short = input("Enter long or short: ")
        currency = input("Enter the currency: ")
        leverage = input("Enter the leverage: ")
        amount = input("Enter the amount: ")
        pnl = -1
        close_date = '-'
        close_time = '-'
    
        # Create a new TradeData object
        trade = TradeData(open_date, open_time, long_short, currency, leverage, amount, pnl, close_date, close_time)
    
        # Add the TradeData object to the list
        self.trades.append(trade)

    def read_from_json(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.trades = [TradeData(**trade_data) for trade_data in data]
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
    
    def save_to_json(self):
        with open(self.filename, 'w') as f:
            data = [trade._asdict() for trade in self.trades]
            json.dump(data, f, indent=4)

    def print_available_trades(self):
        available_trades = [trade for trade in self.trades if trade.close_date == '-']
        table_data = []
        for i, trade in enumerate(available_trades):
            table_data.append([i+1, trade.currency, trade.open_date, trade.open_time, trade.long_short, trade.pnl, trade.close_date, trade.close_time])
        print(tabulate(table_data, headers=[ "Number", "Currency", "Open Date", "Open Time", "Long/Short", "PNL", "Close Date", "Close Time"], tablefmt="fancy_grid", numalign="right", stralign="right", floatfmt=".2f"))
 
    def close_trade(self):
        self.print_available_trades()
        trade_index = int(input("Enter the number of the trade to close: ")) - 1
        trade = [t for t in self.trades if t.close_date == '-'][trade_index]
        pnl = input("Enter the P&L: ")
        close_date = input("Enter the close date: ")
        close_time = input("Enter the close time: ")
        self.trades[self.trades.index(trade)] = trade._replace(pnl=pnl, close_date=close_date, close_time=close_time)
    
    def print_open_positions(self):
        open_trades = [t for t in self.trades if t.close_date == '-']
        headers = ['Open Date', 'Open Time', 'Currency', 'Long/Short', 'Leverage', 'Amount', 'P&L']
        rows = []
        for trade in open_trades:
            long_short_colored = colored(trade.long_short, 'green') if trade.long_short == 'long' else colored(trade.long_short, 'red')
            pnl_colored = colored(trade.pnl, 'green') if float(trade.pnl) >= 0 else colored(trade.pnl, 'red')
            row = [trade.open_date, trade.open_time, trade.currency, long_short_colored, trade.leverage, trade.amount, pnl_colored]
            rows.append([r if r != '-' else '' for r in row])
        print(tabulate(rows, headers=headers, tablefmt='grid'))

    def print_closed_positions(self):
        closed_trades = [t for t in self.trades if t.close_date != '-']
        headers = ['Open Date', 'Open Time', 'Currency', 'Long/Short', 'Leverage', 'Amount', 'P&L', 'Close Date', 'Close Time']
        rows = []
        for trade in closed_trades:
            long_short_colored = colored(trade.long_short, 'green') if trade.long_short == 'long' else colored(trade.long_short, 'red')
            pnl_colored = colored(trade.pnl, 'green') if float(trade.pnl) >= 0 else colored(trade.pnl, 'red')
            row = [trade.open_date, trade.open_time, trade.currency, long_short_colored, trade.leverage, trade.amount, pnl_colored, trade.close_date, trade.close_time]
            rows.append([r if r != '-' else '' for r in row])
        print(tabulate(rows, headers=headers, tablefmt='grid'))

    def print_all(self):
        headers = ['Open Date', 'Open Time', 'Currency', 'Long/Short', 'Leverage', 'Amount', 'P&L', 'Close Date', 'Close Time']
        rows = []
        for trade in self.trades:
            long_short_colored = colored(trade.long_short, 'green') if trade.long_short == 'long' else colored(trade.long_short, 'red')
            pnl_colored = colored(trade.pnl, 'green') if float(trade.pnl) >= 0 else colored(trade.pnl, 'red')
            row = [trade.open_date, trade.open_time, trade.currency, long_short_colored, trade.leverage, trade.amount, pnl_colored, trade.close_date, trade.close_time]
            rows.append([r if r != '-' else '' for r in row])
        print(tabulate(rows, headers=headers, tablefmt='grid'))

    def print_sorted_by_pnl(self):
        sorted_trades = sorted(self.trades, key=lambda x: float(x.pnl), reverse=True)
        headers = ['Open Date', 'Open Time', 'Currency', 'Long/Short', 'Leverage', 'Amount', 'P&L', 'Close Date', 'Close Time']
        rows = []
        for trade in sorted_trades:
            long_short_colored = colored(trade.long_short, 'green') if trade.long_short == 'long' else colored(trade.long_short, 'red')
            pnl_colored = colored(trade.pnl, 'green') if float(trade.pnl) >= 0 else colored(trade.pnl, 'red')
            row = [trade.open_date, trade.open_time, trade.currency, long_short_colored, trade.leverage, trade.amount, pnl_colored, trade.close_date, trade.close_time]
            rows.append([r if r != '-' else '' for r in row])
        print(tabulate(rows, headers=headers, tablefmt='grid'))

    def print_sorted_by_pnl_low_to_high(self):
        sorted_trades = sorted(self.trades, key=lambda x: float(x.pnl))
        headers = ['Open Date', 'Open Time', 'Currency', 'Long/Short', 'Leverage', 'Amount', 'P&L', 'Close Date', 'Close Time']
        rows = []
        for trade in sorted_trades:
            long_short_colored = colored(trade.long_short, 'green') if trade.long_short == 'long' else colored(trade.long_short, 'red')
            pnl_colored = colored(trade.pnl, 'green') if float(trade.pnl) >= 0 else colored(trade.pnl, 'red')
            row = [trade.open_date, trade.open_time, trade.currency, long_short_colored, trade.leverage, trade.amount, pnl_colored, trade.close_date, trade.close_time]
            rows.append([r if r != '-' else '' for r in row])
        print(tabulate(rows, headers=headers, tablefmt='grid'))
    
    def accumulate_pnl(self):
        total_pnl = sum([float(t.pnl) for t in self.trades])
        pnl_colored = colored(f"{total_pnl:.2f}", 'green') if total_pnl >= 0 else colored(f"{total_pnl:.2f}", 'red')
        print('\n\n----------------------------------------')
        print(f"Total P&L: {pnl_colored}")
        print('---------------------------------------- \n\n')
    
    def calculate_positive_trades_percentage(self):
        closed_trades = [t for t in self.trades if t.close_date != '-']
        positive_trades = [t for t in closed_trades if float(t.pnl) > 0]
        if len(closed_trades) == 0:
            print("There are no closed trades to calculate.")
            return
        positive_percentage = len(positive_trades) / len(closed_trades) * 100
        if positive_percentage >= 55:
            positive_colored = colored(f"{positive_percentage:.2f}%", 'green')
        else:
            positive_colored = colored(f"{positive_percentage:.2f}%", 'red')
        print('\n\n----------------------------------------')
        print(f"Percentage of trades: {positive_colored}")
        print('----------------------------------------\n\n')
    
    def print_pnl_summary(self):
        closed_trades = [t for t in self.trades if t.close_date != '-']
        negative_trades = [t for t in closed_trades if float(t.pnl) < 0]
        positive_trades = [t for t in closed_trades if float(t.pnl) > 0]
        if len(closed_trades) == 0:
            print("There are no closed trades to summarize.")
            return
        negative_total = sum([float(t.pnl) for t in negative_trades])
        positive_total = sum([float(t.pnl) for t in positive_trades])
        pnl_sum = negative_total + positive_total
        negative_colored = colored(f"Loses: {negative_total:.2f}", 'red')
        positive_colored = colored(f"Gains: {positive_total:.2f}", 'green')
        pnl_sum_colored = colored(f"Total P&L: {pnl_sum:.2f}", 'green' if pnl_sum >= 0 else 'red')
        print('\n\n----------------------------------------')
        print(negative_colored)
        print(positive_colored)
        print(pnl_sum_colored)
        print('----------------------------------------\n\n')

    def print_pnl_percent(self):
        closed_trades = [t for t in self.trades if t.close_date != '-']
        pnl_sum = sum([float(t.pnl) for t in closed_trades])
        pnl_percent = pnl_sum / self.my_balance * 100
        pnl_percent_colored = colored(f"Total pnl to main acc: {pnl_percent:.2f}%", 'green' if pnl_sum >= 0 else 'red')
        print('\n\n----------------------------------------')
        print(pnl_percent_colored)
        print('----------------------------------------\n\n')

    def print_pnl_weighted_average(self):
        closed_trades = [trade for trade in self.trades if trade.close_date != '-']
        total_pnl = sum(float(trade.pnl) for trade in closed_trades)
        total_amount = sum(float(trade.amount) for trade in closed_trades)
        if total_amount != 0:
            pnl_weighted_avg = total_pnl / total_amount
            if pnl_weighted_avg > 0:
                color = '\033[92m'  # green color
            else:
                color = '\033[91m'  # red color
            percentage = pnl_weighted_avg * 100
            if percentage > 0:
                percentage_color = '\033[92m'  # green color
            else:
                percentage_color = '\033[91m'  # red color
            print('\n\n----------------------------------------')
            print(f"PNL Weighted Average: {color}{pnl_weighted_avg:.2f} ({percentage_color}{percentage:.2f}%\033[0m)")
            print('----------------------------------------\n\n')
        else:
            print('\n\n----------------------------------------')
            print("No closed trades found.")
            print('----------------------------------------\n\n')

    def __del__(self):
        self.save_to_json()