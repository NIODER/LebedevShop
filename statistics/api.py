import requests

API_URL = "http://localhost:8080"


def get_items():
    return requests.get(API_URL + '/items', ).json()

def create_order():
    return requests.put(url=API_URL + '/order', json=
    {
        'address': 'some address',
        'basketId': ''
    }).json()

def create_item():
    return requests.put(url=API_URL + '/items', json=
    {
        'itemName': 'item1',
        'description': 'cool item!',
        'cost': 123.123
    }).json()

def delete_item(item_id):
    return requests.delete(API_URL + f'/items/{item_id}').json()

def get_item_by_id(item_id):
    return requests.get(API_URL + f'/items/{item_id}').json()

def basket_add_item(basket_id, item_id):
    return requests.post(API_URL + f'/basket/{basket_id}/{item_id}').json()

def create_basket():
    return requests.put(API_URL + '/basket').json()

def delete_basket_by_id(basket_id):
    return requests.delete(API_URL + f'/basket/{basket_id}').json()

def delete_item_from_basket(basket_id, item_id):
    return requests.delete(API_URL + f'/basket/{basket_id}/{item_id}').json()

def get_basket_by_id(basket_id):
    return requests.get(API_URL + f'/basket/{basket_id}').json()