import requests

API_URL = 'http://localhost:8080'


def get_items() -> tuple[str, float]:
    request = requests.get(f'{API_URL}/items')
    return (request.json(), request.elapsed.total_seconds())


# creates order and returns order id and response time
def create_order(basket_id: str, address: str) -> tuple[str, float]:
    request = requests.put(url=f'{API_URL}/order', json={
        'address': address,
        'basketId': basket_id
    })
    return (request.json()['orderId'], request.elapsed.total_seconds())


# creates item and returns item id and response time
def create_item(item_name: str, description: str, cost: float) -> tuple[str, float]:
    request = requests.put(url=f'{API_URL}/items', json={
        'itemName': item_name,
        'description': description,
        'cost': cost
    })
    return (request.json()['itemId'], request.elapsed.total_seconds())


# deletes item and returns deleted item and response time
def delete_item(item_id: str) -> tuple[str, float]:
    request = requests.delete(f'{API_URL}/items/{item_id}')
    return (request.json(), request.elapsed.total_seconds())


# gets item and returns item json and response time
def get_item_by_id(item_id: str) -> tuple[str, float]:
    request = requests.get(f'{API_URL}/items/{item_id}')
    return (request.json(), request.elapsed.total_seconds())


# adds item and returns basket json and response time
def basket_add_item(basket_id: str, item_id: str) -> tuple[str, float]:
    request = requests.post(f'{API_URL}/basket/{basket_id}/{item_id}')
    return (request.json(), request.elapsed.total_seconds())


# creates basket and returns basket id and response time
def create_basket() -> tuple[str, float]:
    request = requests.put(f'{API_URL}/basket')
    return (request.json()['basketId'], request.elapsed.total_seconds())


# deletes basket and return basket json and response time
def delete_basket_by_id(basket_id: str) -> tuple[str, float]:
    request = requests.delete(f'{API_URL}/basket/{basket_id}')
    return (request.json(), request.elapsed.total_seconds())


# deletes item from basket and returns basket json and response time
def delete_item_from_basket(basket_id: str, item_id: str) -> tuple[str, float]:
    request = requests.delete(f'{API_URL}/basket/{basket_id}/{item_id}')
    return (request.json(), request.elapsed.total_seconds())


# gets basket by id and returns basket json and response time
def get_basket_by_id(basket_id: str) -> tuple[str, float]:
    request = requests.get(f'{API_URL}/basket/{basket_id}')
    return (request.json(), request.elapsed.total_seconds())


def get_order_by_id(order_id: str) -> tuple[str, float]:
    request = requests.get(f'{API_URL}/order/{order_id}')
    return (request.json(), request.elapsed.total_seconds())