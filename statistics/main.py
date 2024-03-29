import json
import os
import random
import sys
from matplotlib import pyplot as plt
import scenarios
import api


def draw_graph(request_name: str, times: list[float]):
    print(f'Draw {request_name}')
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.suptitle(f'{request_name} execution time')
    avg_time = sum(times) / len(times)

    ax.bar(range(1, len(times) + 1), times, color='skyblue')
    ax.set_xlabel('Request')
    ax.set_ylabel('Time (s)')
    ax.set_title(f'{request_name} (Average: {avg_time:.3f} s)')
    plt.savefig(os.path.join(images_path, f'{request_name}.png'))
    if show_figures:
        plt.show()


def create_items() -> list[float]:
    print('Creating items...')
    global item_ids
    (item_ids, times) = scenarios.create_items(num_requests)
    return times


def get_items() -> list[float]:
    print('Getting all items...')
    return [api.get_items()[1] for _ in range(num_requests)]


def get_item_by_id() -> list[float]:
    print('Getting items by id...')
    return [api.get_item_by_id(random.choice(item_ids))[1] for _ in range(num_requests)]


def delete_item() -> list[float]:
    print('Deleting items...')
    return [api.delete_item(item_ids[i])[1] for i in range(num_requests)]


def create_basket() -> list[float]:
    print('Creating baskets...')
    global basket_ids
    (basket_ids, times) = scenarios.create_baskets(num_requests)
    return times


def get_basket_by_id() -> list[float]:
    print('Getting baskets by id...')
    return [api.get_basket_by_id(basket_ids[i])[1] for i in range(num_requests)]


def basket_add_item() -> list[float]:
    print('Adding items to baskets...')
    return scenarios.fill_baskets(num_requests, basket_ids, item_ids)


def basket_remove_item() -> list[float]:
    print('Removing items from baskets...')
    times = []
    counter = 0
    for basket_id in basket_ids:
        response = api.get_basket_by_id(basket_id)[0]
        basket_item_ids = [item['itemId'] for item in response['items']]
        for basket_item_id in basket_item_ids:
            times.append(api.delete_item_from_basket(basket_id, basket_item_id)[1])
            counter += 1
            if counter > num_requests:
                return times
    return times


def create_order() -> list[float]:
    print('Creating orders...')
    global order_ids
    (order_ids, times) = scenarios.create_orders(num_requests, basket_ids)
    return times


def get_order_by_id() -> list[float]:
    print('Getting orders by id...')
    return [api.get_order_by_id(order_ids[i])[1] for i in range(num_requests)]


def delete_basket() -> list[float]:
    print('Deleting baskets...')
    return [scenarios.delete_basket_by_id(basket_ids[i])[1] for i in range(num_requests)]


if __name__ == '__main__':
    num_requests = 100
    show_figures = eval(sys.argv[1])
    images_path = os.path.join(os.getcwd(), 'graphics', sys.argv[2])
    os.makedirs(images_path, exist_ok=True)
    print(f'Saving graphics to {images_path}')

    draw_graph('create items', create_items())
    draw_graph('create baskets', create_basket())
    draw_graph('add item to basket', basket_add_item())
    draw_graph('get items', get_items())
    draw_graph('get item by id', get_item_by_id())
    draw_graph('get basket by id', get_basket_by_id())
    draw_graph('create order', create_order())
    draw_graph('get order by id', get_order_by_id())
    draw_graph('remove item from basket', basket_remove_item())
    draw_graph('delete basket', delete_basket())
    draw_graph('delete item', delete_item())

