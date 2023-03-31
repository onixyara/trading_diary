from TradingManager import *
from MyTypes import *
import json
import os

def start_mnanager():
    manager = TradingManager('/Users/vladyslavonishchuk/Study/Projects/python/TraidingDiary/Futures_March.json', '/Users/vladyslavonishchuk/Study/Projects/python/TraidingDiary/Spot_March.json')
    print('Chose option, type number.')
    while(True):
        for a in commands:
            print(a)
        com = input()
        print("\033c\033[3J")
        if com == '1':
            futures_manager_comands(manager.futures_manager)
        elif com == '2':
            spot_manager_comands(manager.spot_manager)
        elif com == '3':
            analysis_menu()
        elif com == 'x':
            break

def analysis_menu():
    print(3)

def spot_manager_comands(manager):
    while(True):
        print('Chose option, type number:')
        for a in spot_manager_commands:
            print(a)
        com = input()
        print("\033c\033[3J")
        print(com)
        if com == 'x':
            break
        if com == '1':
            print_spot_show(manager)
        elif com == '2':
            manager.add_trade()
        elif com == '3':
            manager.close_trade()
        else:
            print('Wrong input.')

def print_spot_show(manager):
    while(True):
        for b in print_spot_commands:
            print(b)
        com = input()
        print("\033c\033[3J")
        if com == '1':
            manager.print_all()
        elif com == '2':
            manager.print_sorted_by_profit_descending()
        elif com == '3':
            manager.print_sorted_by_profit_ascending()
        elif com == '4':
            manager.print_open_positions()
        elif com == '5':
            manager.print_closed_positions()
        elif com == 'x':
            break

def futures_manager_comands(manager):
    while(True):
        print('Chose option, type number:')
        for a in manager_commands:
            print(a)
        com = input()
        print("\033c\033[3J")
        print(com)
        if com == 'x':
            break
        if com == '1':
            print_options_show(manager)
        elif com == '2':
            manager.add_trade()
        elif com == '3':
            manager.close_trade()
        elif com == '4':
            show_pnl_options(manager)
        else:
            print('Wrong input.')

def show_pnl_options(manager):
    while(True):
        for b in print_pnl_comands:
            print(b)
        com = input()
        print("\033c\033[3J")

        if com == '1':
            manager.accumulate_pnl()
        elif com == '2':
            manager.calculate_positive_trades_percentage()
        elif com == '3':
            manager.print_pnl_summary()
        elif com == '4':
            manager.print_pnl_percent()
        elif com == '5':
            manager.print_pnl_weighted_average()
        elif com == 'x':
            break

def print_options_show(manager):
    while(True):
        for b in print_commands:
            print(b)
        com = input()
        print("\033c\033[3J")
        if com == '1':
            manager.print_all()
        elif com == '2':
            manager.print_sorted_by_pnl()
        elif com == '3':
            manager.print_sorted_by_pnl_low_to_high()
        elif com == '4':
            manager.print_open_positions()
        elif com == '5':
            manager.print_closed_positions()
        elif com == 'x':
            break