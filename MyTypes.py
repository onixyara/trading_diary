from collections import namedtuple

TradeData = namedtuple('TradeData', ['open_date', 'open_time', 'long_short', 'currency', 'leverage', 'amount', 'pnl', 'close_date', 'close_time'])

SpotData = namedtuple('SpotData', ['currency', 'open_date', 'buy_price', 'amount', 'sell_price', 'profit', 'close_date'])

commands = ['1. Go to futures diary', '2. Go to spot diary.', '3. Analysis menu.', 'x - exit.']

spot_manager_commands = ['1. Show data options.', '2. Add new trade.', '3. Close trade.', 'x - go to previous menu']

manager_commands = ['1. Show data options.', '2. Add new trade.', '3. Close trade.', '4. Show PNL data options.','x - go to previous menu']

print_spot_commands = ['1. Print all.', '2. By profit descending','3. By profit ascending', '4. Open positions.', '5. Closed positions.', 'x - go to previous menu']

print_commands = ['1. Print all.', '2. By PNL descending.', '3. By PNL ascending.', '4. Open positions.', '5. Closed positions.', 'x - go to previous menu']

print_pnl_comands = ['1. Acumulated PNL.', '2. Trades percentage.', '3. PNL summary.', '4. PNL to balance percentage.', '5. Weighted avarage PNL.', 'x - go to previous menu']