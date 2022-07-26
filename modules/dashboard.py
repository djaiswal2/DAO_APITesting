import json

from modules.base import Base

class Dashboard():
    base = Base()

    def get_exchange(self,data):
        path = "exchange?amount={}&currency={}".format(data.get("amount"), data.get("currency"))
        return self.base.get_req(path,data)

    def get_token_price(self):
        return self.base.get_req("token_price")

    def get_user_details(self,data):
        return self.base.post_req("user_details",data)

    def get_account_addr(self,data):
        return self.base.post_req("retrieve_algo_public_addr",data)

    def save_public_addr(self,data):
        return self.base.post_req("save_algo_public_addr_and_opt_in ",data)

    def get_account_addr_by_type(self,data):
        return self.base.post_req("retrieve_account_address",data)

    def get_user_token_balance(self,data):
        return self.base.post_req("user_token_balance",data)

    def get_opt_in_by_addr(self,data):
        return self.base.post_req("opt_in",data)

    def get_user_details_with_token_price(self,data):
        return self.base.post_req("user_details_with_token_price",data)

    def buy_token(self,data):
        return self.base.post_req("buy_token",data)

    def retrieve_proposal_type(self,data):
        return self.base.post_req("retrieve_proposal_type",data)

    def retrieve_my_proposals(self,data):
        return self.base.post_req("retrieve_my_proposals",data)








