import pywaves as pw
import datetime
from time import sleep
import os
import configparser
import socket

class AndBot:
    def __init__(self):

        self.node = "http://nodes.wavesnodes.com"
        self.chain = "mainnet"
        self.matcher = "https://matcher.waves.exchange"
        self.private_key = ""
        self.amount_asset_id = pw.WAVES
        self.amount_asset = pw.Asset(pw.WAVES)
        self.price_asset_id = "8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS" # BTC
        self.price_asset = pw.Asset(self.price_asset_id)  
        self.amount_asset1_id = "474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu"
        self.amount_asset1 = pw.Asset(self.amount_asset1_id)  
        self.price_asset1_id = "8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS" # BTC
        self.price_asset1 = pw.Asset(self.price_asset1_id)  
        self.price_asset2_id = "474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu" # 
        self.price_asset2 = pw.Asset(self.price_asset2_id)  

    def read_config(self, cfg_file):
        if not os.path.isfile(cfg_file):
            exit(1)

        try:
            config = configparser.RawConfigParser()
            config.read(cfg_file)
            self.node = config.get('main', 'node')
            self.chain = config.get('main', 'network')
            self.matcher = config.get('main', 'matcher')
            self.order_fee = config.getint('main', 'order_fee')
            self.order_lifetime = config.getint('main', 'order_lifetime')

            self.private_key = config.get('account', 'private_key')
            self.amount_asset_id = config.get('market', 'amount_asset')
            self.amount_asset = pw.Asset(self.amount_asset_id)
            self.price_asset_id = config.get('market', 'price_asset')
            self.price_asset = pw.Asset(self.price_asset_id)
        except OSError:
            exit(1)


def main():

    bot = AndBot()
    bot.read_config("config.cfg")
    pw.setNode(node=bot.node, chain=bot.chain)
    pw.setMatcher(node=bot.matcher)
    my_address = pw.Address(privateKey=bot.private_key)
    eth_btc = pw.AssetPair(bot.amount_asset1, bot.price_asset1)
    UDP_IP = "192.168.0.115"
    UDP_PORT2 = 5006
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        order_book1 = eth_btc.orderbook()
        bid1R = (float(order_book1["bids"][0]["price"]))
        bid1 = bid1R / 10 ** 8
        sock2.sendto(str(bid1), (UDP_IP, UDP_PORT2))
if __name__ == "__main__":
    main()
