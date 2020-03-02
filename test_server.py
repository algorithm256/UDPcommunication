import pywaves as pw
import datetime
from time import sleep
import os
import configparser
import socket

class AndBot:
    def __init__(self):
        self.log_file = "bot.log"             
        self.node = "http://nodes.wavesnodes.com"
        self.chain = "mainnet"
        self.matcher = "https://matcher.waves.exchange"
        self.order_fee = int(0.003 * 10 ** 8)
        self.order_lifetime = 86400  # 29 days
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


    def log(self, msg):
        timestamp = datetime.datetime.utcnow().strftime("%b %d %Y %H:%M:%S UTC")
        s = "[{0}]:{1}".format(timestamp, msg)
        print(s)
        try:
            f = open(self.log_file, "a")
            f.write(s + "\n")
            f.close()
        except OSError:
            pass

    def read_config(self, cfg_file):
        if not os.path.isfile(cfg_file):
            self.log("Missing config file")
            self.log("Exiting.")
            exit(1)

        try:
            self.log("Reading config file '{0}'".format(cfg_file))
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
            self.log("Error reading config file")
            self.log("Exiting.")
            exit(1)


def main():

    bot = AndBot()
    bot.read_config("config.cfg")
    pw.setNode(node=bot.node, chain=bot.chain)
    pw.setMatcher(node=bot.matcher)
    my_address = pw.Address(privateKey=bot.private_key)
    waves_btc = pw.AssetPair(bot.amount_asset, bot.price_asset)
    eth_btc = pw.AssetPair(bot.amount_asset1, bot.price_asset1)
    waves_eth = pw.AssetPair(bot.amount_asset, bot.price_asset2)
    UDP_IP = "192.168.0.136"
    UDP_PORT1 = 5005
    UDP_PORT2 = 5006
    UDP_PORT3 = 5007
    UDP_PORT4 = 5008
    UDP_PORT5 = 5009
    UDP_PORT6 = 5010
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock1.bind((UDP_IP, UDP_PORT1))
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock2.bind((UDP_IP, UDP_PORT2))
    sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock3.bind((UDP_IP, UDP_PORT3))
    sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock4.bind((UDP_IP, UDP_PORT4))
    sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock5.bind((UDP_IP, UDP_PORT5))
    sock6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock6.bind((UDP_IP, UDP_PORT6))
    
    while True:
        ask, addr = sock1.recvfrom(1024) # buffer size is 1024 bytes
        bid1, addr = sock2.recvfrom(1024)
        ask2, addr = sock3.recvfrom(1024)
        ask_amt, addr = sock4.recvfrom(1024) # waves
        bid1_amt, addr = sock5.recvfrom(1024)   # btc
        ask2_amt, addr = sock6.recvfrom(1024)   # eth
        
        bid1_amtW = bid1_amt *
        ask2_amtW = ask2_amt *
        amt = min(ask_amt, bid1_amt, ask2_amt)

        cal = ((10000 / ask2) * bid1 / ask) - 10000
        if cal > 1
            buy
            sell
            buy


        bot.log("D1: {0}".format(float(ask)))        
        bot.log("D2: {0}".format(float(bid1)))
        bot.log("D3: {0}".format(float(ask2)))  
        bot.log("A1: {0}".format(float(ask_amt)))        
        bot.log("A2: {0}".format(float(bid1_amt)))
        bot.log("A3: {0}".format(float(ask2_amt)))  

if __name__ == "__main__":
    main()