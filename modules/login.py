from modules.base import Base

class Login(object):
    base = Base()

    def create_account(self,data):
        headers={
            'Content-type':'application/json',
            'Accept':'application/json'
        }
        return self.base.post_req(end_point="create_account",data=data,headers=headers)

    def login(self, data):
        return self.base.post_req("do_login",data )

    def send_email(self,data):
        return self.base.post_req("send_email",data)

    def get_country_list(self):
        return self.base.get_req(end_point="countries")

    def forget_pass(self, data):
        return self.base.post_req("forgot_password",data)





