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
        self.price_asset_id = "" # BTC
        self.price_asset = pw.Asset(self.price_asset_id)  
        self.amount_asset1_id = ""
        self.amount_asset1 = pw.Asset(self.amount_asset1_id)  
        self.price_asset1_id = "" # BTC
        self.price_asset1 = pw.Asset(self.price_asset1_id)  
        self.price_asset2_id = "" # 
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
    waves_btc = pw.AssetPair(bot.amount_asset, bot.price_asset)
    UDP_IP = "192.168.0.115"
    UDP_PORT1 = 5005
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        order_book = waves_btc.orderbook()
        askR = (float(order_book["asks"][0]["price"]))
        ask = askR / 10 ** 8
        sock1.sendto(str(ask), (UDP_IP, UDP_PORT1))
if __name__ == "__main__":
    main()
