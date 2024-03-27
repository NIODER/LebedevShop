import requests

API_URL = 'http://localhost:8080'


def get_items():
    return requests.get(f'{API_URL}/items')


def create_order(basket_id):
    return requests.put(url=f'{API_URL}/order', json={
        'address': 'some address',
        'basketId': basket_id
    })


def create_item():
    return requests.put(url=f'{API_URL}/items', json={
        'itemName': 'item1',
        'description': 'cool item!',
        'cost': 123.123
    })


def delete_item(item_id):
    return requests.delete(f'{API_URL}/items/{item_id}')


def get_item_by_id(item_id):
    return requests.get(f'{API_URL}/items/{item_id}')


def basket_add_item(basket_id, item_id):
    return requests.post(f'{API_URL}/basket/{basket_id}/{item_id}')


def create_basket():
    return requests.put(f'{API_URL}/basket')


def delete_basket_by_id(basket_id):
    return requests.delete(f'{API_URL}/basket/{basket_id}')


def delete_item_from_basket(basket_id, item_id):
    return requests.delete(f'{API_URL}/basket/{basket_id}/{item_id}')


def get_basket_by_id(basket_id):
    return requests.get(f'{API_URL}/basket/{basket_id}')
