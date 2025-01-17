import cbpro
import pandas as pd
from datetime import datetime

class CoinbaseAdvanced:
    def __init__(self, api_setup):
        self.api_key = api_setup['api_key']
        self.api_secret = api_setup['api_secret']
        self.client = cbpro.AuthenticatedClient(
            self.api_key, self.api_secret
        )

    def fetch_recent_ohlcv(self, symbol, timeframe, limit):
        granularity = self._timeframe_to_granularity(timeframe)
        data = self.client.get_product_historic_rates(
            symbol, granularity=granularity, limit=limit
        )
        df = pd.DataFrame(data, columns=['time', 'low', 'high', 'open', 'close', 'volume'])
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df = df.set_index('time')
        df = df.sort_index()
        return df

    def _timeframe_to_granularity(self, timeframe):
        if timeframe == '1m':
            return 60
        elif timeframe == '5m':
            return 300
        elif timeframe == '15m':
            return 900
        elif timeframe == '1h':
            return 3600
        elif timeframe == '4h':
            return 14400
        elif timeframe == '1d':
            return 86400
        else:
            raise ValueError(f"Timeframe {timeframe} not supported")

    def fetch_open_orders(self, symbol):
        orders = self.client.get_orders(product_id=symbol, status='open')
        return orders

    def cancel_order(self, order_id, symbol):
        self.client.cancel_order(order_id)

    def fetch_open_trigger_orders(self, symbol):
        # Coinbase does not have trigger orders in the same way as Bitget
        # You will need to implement this logic using limit orders with stop prices
        # This is a placeholder
        return []

    def cancel_trigger_order(self, order_id, symbol):
        # Coinbase does not have trigger orders in the same way as Bitget
        # You will need to implement this logic using limit orders with stop prices
        # This is a placeholder
        pass

    def fetch_closed_trigger_orders(self, symbol):
        # Coinbase does not have trigger orders in the same way as Bitget
        # You will need to implement this logic using limit orders with stop prices
        # This is a placeholder
        return []

    def flash_close_position(self, symbol, side):
        # Coinbase does not have flash close position
        # You will need to implement this logic using market orders
        # This is a placeholder
        pass

    def place_trigger_market_order(self, symbol, side, amount, trigger_price, reduce, print_error):
        # Coinbase does not have trigger market orders
        # You will need to implement this logic using limit orders with stop prices
        # This is a placeholder
        pass

    def place_trigger_limit_order(self, symbol, side, amount, trigger_price, price, print_error):
        # Coinbase does not have trigger limit orders
        # You will need to implement this logic using limit orders with stop prices
        # This is a placeholder
        pass

    def fetch_open_positions(self, symbol):
        # Coinbase does not have positions in the same way as Bitget
        # You will need to implement this logic using the account information
        # This is a placeholder
        return []

    def fetch_balance(self):
        accounts = self.client.get_accounts()
        balance = {}
        for account in accounts:
            if account['currency'] == 'USDT':
                balance['USDT'] = {'total': float(account['available'])}
        return balance

    def fetch_min_amount_tradable(self, symbol):
        product = self.client.get_product(symbol)
        return float(product['base_min_size'])