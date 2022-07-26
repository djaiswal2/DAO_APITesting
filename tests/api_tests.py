import requests
import json

from requests.models import Response
def create_account():
    url =  "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/create_account"
    data = {
        "name": "ayush",
        "country": "india",
        "email": "test@yopmail.com",
        "referal_code": "dfzafda",
        "password": "1234",
        "confirm_password": "1234"
    }
    headers={
        'Content-type':'application/json',
        'Accept':'application/json'
    }
    r = requests.post(url = url , json=  data, headers=headers)
    print(r)
    data = json.loads(r.text)
    print(data)

def login():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/do_login"
    data = {

        "email": "ayush.srivastava@dataneers.in",
        "password": "12345"

    }
    r = requests.post(url = url , json = data)
    data = json.loads(r.text)
    print(data)

def send_email():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/send_email"
    data = {
        "email":"abhay.chaurasia@dataneers.in"
    }
    r = requests.post(url = url , json = data)
    data = json.loads(r.text)
    print(data)

def reset_password():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/reset_password"
    data = { "email":"ayush.srivastava@dataneers.in",
             "old_password":"12345",
             "new_password":"123456",
             "confirm_password":"123456"
             }

    r = requests.post(url = url , json = data)
    data = json.loads(r.text)
    print(data)

def forgot_password():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/forgot_password"
    data = {
        "email":"ayush.srivastava@dataneers.in"
    }
    r = requests.get(url = url , params = data)
    data = json.loads(r.text)
    print(data)

def exchange():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/exchange"
    data = {"amount":1,
            "currency":"USD"}
    r = requests.get(url = url , params = data)
    data = json.loads(r.text)
    print(data)

def navigation():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/token_price"
    r = requests.get(url = url)
    data = json.loads(r.text)
    print(data)

def user_detail():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/user_details"
    data = {
        "email":"ayush.srivastava@dataneers.in"
    }
    r = requests.post(url = url, json = data)
    data = json.loads(r.text)
    print(data)

def retrieve_algo():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/retrieve_algo_public_addr"
    data = {
        "email": "kishor1@yopmail.com"
    }
    r = requests.put(url = url, json = data)
    data = json.loads(r.text)
    print(data)

def save_algo():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/save_algo_public_addr"
    data = {
        "email": "kishor2@yopmail.com",
        "algo_public_address": "111222333"
    }
    r = requests.put(url = url, json = data)
    data = json.loads(r.text)
    print(data)

def retrieve_account_address():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/retrieve_account_address"
    data = {
        "address_type": "ALGO"
    }
    r = requests.post(url = url, json = data)
    data = json.loads(r.text)
    print(data)



def user_token_balance():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/user_token_balance"
    data = {
        "email": "kishor1@yopmail.com"
    }
    r = requests.put(url = url, json = data)
    data = json.loads(r.text)
    print(data)

def user_detail_with_balanc():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/user_details_with_token_price"
    data = {
        "email": "kishor1@yopmail.com"
    }
    r = requests.post(url = url, json = data)
    data = json.loads(r.text)
    print(data)

def buy_token():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/buy_token"
    data = {
        "user_id": "1324",
        "email": "kish@In",
        "payment_date": "20220620152100",
        "payment_account": "11111",
        "transaction_hash": "117788",
        "algo_public_address": "abcdefghijklmnopqrstuvwxyz",
        "no_of_dao": "2",
        "buy_amount": "34",
        "buy_currency": "Eth",
        "usd_price": "5",
        "transaction_fee": ".2"
    }
    r = requests.post(url = url, json =data)
    data = json.loads(r.text)
    print(data)
def reset_password():
    url = "https://nkux7fssxf.execute-api.us-east-1.amazonaws.com/v1/reset_password"
    data = { "email":"ayush.srivastava@dataneers.in",
             "old_password":"123456",
             "new_password":"12345",
             }

    r = requests.post(url = url , json = data)
    data = json.loads(r.text)
    print(data)


create_account()
login()
send_email()
reset_password()
exchange()
navigation()
user_detail()
save_algo()
retrieve_algo()
retrieve_account_address()
user_token_balance()
user_detail_with_balanc()