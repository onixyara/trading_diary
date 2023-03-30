from  FuturesManager import *
from SpotManager import *

class TradingManager:
    def __init__(self, futures_file_path, spot_file_path):
        self.futures_manager = FuturesManager(futures_file_path)
        self.spot_manager = SpotManager(spot_file_path)

# FUTURES BLOCK
    def __del__(self):
        del self.futures_manager
        del self.spot_manager

    def open_futures_position(self):
        self.futures_manager.open_position()

    def close_futures_position(self):
        self.futures_manager.close_position()

    def show_futures_positions(self):
        self.futures_manager.show_all()



# SPOT BLOCK
    def open_spot_position(self):
        self.spot_manager.open_position()

    def close_spot_position(self):
        self.spot_manager.close_position()

    def show_spot_positions(self):
        self.spot_manager.show_all()