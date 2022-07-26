import json
import random

from config.constants import *
from modules.dashboard import Dashboard

class Test_Dashboard():

    dashboard = Dashboard()

    def test_get_exchange_ETH(self):
        data= {
            "amount" : 10,
            "currency" : "ETH"
        }
        res = self.dashboard.get_exchange(data)
        assert res["statusCode"] == 200
        message = res["body"]
        assert message.get("USD") >0
        assert message.get("DAO") >0
        assert message.get("Transaction_Fees") >0

        print(res)

    def test_get_exchange_USD(self):
        data= {
            "amount" : 10,
            "currency" : "USD"
        }
        res = self.dashboard.get_exchange(data)
        print(res)
        assert res["statusCode"] == 200
        assert message.get("USD") >0
        assert message.get("DAO") >0
        assert message.get("Transaction_Fees") >0


    def test_get_exchange_USDT(self):
        data= {
            "amount" : 10,
            "currency" : "USDT"
        }
        res = self.dashboard.get_exchange(data)
        assert res["statusCode"] == 200
        message = res["body"]
        assert message.get("USD") >0
        assert message.get("DAO") >0
        assert message.get("Transaction_Fees") >0

    def test_get_exchange_BNB(self):
        data= {
            "amount" : 1,
            "currency" : "BNB"
        }
        res = self.dashboard.get_exchange(data)
        assert res["statusCode"] == 200
        message = res["body"]
        assert message.get("USD") >0
        assert message.get("DAO") >0
        assert message.get("Transaction_Fees") >0

    def test_get_exchange_ALGO(self):
        data= {
            "amount" : 1,
            "currency" : "ALGO"
        }
        res = self.dashboard.get_exchange(data)
        assert res["statusCode"] == 200
        message = res["body"]
        assert message.get("USD") >0
        assert message.get("DAO") >0
        assert message.get("Transaction_Fees") >0

    def test_get_token_price(self):
        res = self.dashboard.get_token_price()
        assert res["statusCode"] == 200
        message = res["body"]
        assert message.get("price") >0

    def test_get_user_details(self):
        data= {
            "email" : EMAIL_ID
        }
        res = self.dashboard.get_user_details(data)
        print(res)
        assert res["statusCode"] == 200

    def test_save_public_add(self):
        data= {
            "email" : EMAIL_ID,
            "algo_public_address" : "19212455"
        }
        res = self.dashboard.save_public_addr(data)
        print(res)
        assert res["statusCode"] == 200

    def test_get_account_addr(self):
        data= {
            "email" : EMAIL_ID
        }
        res = self.dashboard.get_account_addr(data)
        assert res["statusCode"] == 200
        print(res)







