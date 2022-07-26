import random

from config.constants import *
from modules.login import Login

class Test_Login:

    email = str(random.randint(0,99999))+EMAIL_ID

    def test_create_login_invalid(self):
        data = {
            "name": Name,
            "country": COUNTRY,
            "email": self.email,
            "referal_code": REFERAL_CODE,
            "password": PASSWORD,
            "password": "test"
        }
        login = Login()
        res = login.create_account(data)
        print(res)
        assert res["code"] == 400
        assert  "invalid" in res["message"]

    def test_signup(self):
        data = {
            "name": Name,
            "country": COUNTRY,
            "email": self.email,
            "referal_code": REFERAL_CODE,
            "password": PASSWORD,
            "confirm_password": PASSWORD
        }
        login = Login()
        res = login.create_account(data)
        print(res)
        assert res["code"] == 201
        assert res["message"] == "Successfully created user account for {}".format(self.email)

    def test_create_login_duplicate(self):
        data = {
            "name": Name,
            "country": COUNTRY,
            "email": self.email,
            "referal_code": REFERAL_CODE,
            "password": PASSWORD,
            "confirm_password": PASSWORD
        }
        login = Login()
        res = login.create_account(data)
        print(res)
        assert res["code"] == 409
        assert  "User with email ID {} already exists".format(self.email) in res["message"]


    def test_do_login(self):
        data = {
            "email": self.email,
            "password": PASSWORD
        }
        login = Login()
        res = login.login(data)
        print(res)
        assert res["code"] == 200
        assert "User login successful" in res["message"]
        print(res)

    def test_do_login_invalid(self):
        data = {

            "email": self.email,
            "password": "abc"
        }
        login = Login()
        res = login.login(data)
        print(res)
        assert res["code"] == 401
        assert "User email and password did not match" in res["message"]
        print(res)

    def test_send_email(self):
        data = {
            "email":self.email
        }
        login= Login()
        res = login.send_email(data)
        print (res)
        assert res["status_code"] == 200
        assert "Sent verification email to {}".format(self.email) in res["message"]

    def test_send_email_non_existing(self):
        data = {
            "email":"invalid@yopmail.com"
        }
        login= Login()
        res = login.send_email(data)
        print (res)
        assert res["code"] == 404
        assert "invalid" in res["message"]


    def test_get_country_list(self):
        login =Login()
        res = login.get_country_list()
        assert res["statusCode"] == 200


    def test_forget_password(self):
        login = Login()
        data = {
            "email": self.email,
            "token": "138413",
            "password": "new_pass@123",
            "confirm_password": "new_pass@123"
        }

        login= Login()
        res = login.forget_pass(data)
        print (res)
        assert res["code"] == 200
        assert "Successfully sent forgot password link via email" in res["message"]

