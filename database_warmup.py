import os
import sys
import getopt

from binance_trade_bot.database_warmup import warmup_database

if __name__ == "__main__":
    db_path = "data/crypto_trading.db"
    coin_list = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:c:", [
                                   "dbpath=", "coinlist="])
    except getopt.GetoptError:
        pass
    for opt, arg in opts:
        if opt == '-h':
            print('database_warmup.py - Script to farm up a db with some coins')
            print('parameters:')
            print(
                '-d, --dbpath <optional, path to db, if not given the default db path will be used>')
            print('-c, --coinlist <optional, list of coins, e.g \'ADA BTC ETH ...\', if not given all coins available for bridge will be used>')
            os._exit(os.EX_OK)
        elif opt in ("-d", "--dbpath"):
            db_path = arg
        elif opt in ("-c", "--coinlist"):
            coin_list = arg.split()

    warmup_database(coin_list, db_path)
    os._exit(os.EX_OK)
