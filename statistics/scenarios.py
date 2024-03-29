import matplotlib.pyplot as plt
import random
from api import *

def random_item_properties() -> tuple[str, str, float]:
    item_name = f'item_{random.randint(0, 1000)}'
    description = f'description of {item_name}'
    cost = random.randint(0, 1000) + random.random()
    return (item_name, description, cost)


def random_address() -> str:
    return f'street {random.randint(1, 10)}, house {random.randint(1, 50)}, floor {random.randint(1, 12)}'


# create num_requests items returns tuple of item ids and response times
def create_items(num_requests: int) -> tuple[list[str], list[float]]:
    return zip(*[create_item(*random_item_properties()) for _ in range(num_requests)])


# create num_requests baskets returns tuple of basket ids and response times
def create_baskets(num_requests: int) -> tuple[list[str], list[float]]:
    return zip(*[create_basket() for _ in range(num_requests)])


# fills random baskets with random items
def fill_baskets(num_requests: int, baskets_ids: list[str], item_ids: list[str]) -> list[float]:
    counter = 0
    times = []
    while counter < num_requests:
        for basket_id in baskets_ids:
            items = item_ids[random.randint(0, len(item_ids))::]
            for item in items:
                if counter >= num_requests:
                    return times
                times.append(basket_add_item(basket_id=basket_id, item_id=item)[1])
                counter += 1
    return times


# creates orders for random baskets
def create_orders(num_requests: int, baskets_ids: list[str]) -> tuple[list[str], list[float]]:
    return zip(*[create_order(random.choice(baskets_ids), random_address()) for _ in range(num_requests)])

