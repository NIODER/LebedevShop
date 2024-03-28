import matplotlib.pyplot as plt
import random
from api import *

# Функция для замера времени выполнения запросов и построения графиков
def measure_and_plot_requests(request_functions, num_requests):
    for request_name, request_function in request_functions.items():
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.suptitle(f'{request_name} Execution Time')

        times = [request_function().elapsed.total_seconds() for _ in range(num_requests)]
        avg_time = sum(times) / len(times)

        ax.bar(range(1, len(times) + 1), times, color='skyblue')
        ax.set_xlabel('Request')
        ax.set_ylabel('Time (s)')
        ax.set_title(f'{request_name} (Average: {avg_time:.3f} s)')

        plt.show()


# Список функций запросов
request_functions = {
    "get_items": get_items,
    "create_order": lambda: create_order(random.randint(1, 10)),
    "create_item": create_item,
    "delete_item": lambda: delete_item(random.randint(1, 10)),
    "get_item_by_id": lambda: get_item_by_id(random.randint(1, 10)),
    "basket_add_item": lambda: basket_add_item(random.randint(1, 10), random.randint(1, 10)),
    "create_basket": create_basket,
    "delete_basket_by_id": lambda: delete_basket_by_id(random.randint(1, 10)),
    "delete_item_from_basket": lambda: delete_item_from_basket(random.randint(1, 10), random.randint(1, 10)),
    "get_basket_by_id": lambda: get_basket_by_id(random.randint(1, 10)),
}

# Замер времени выполнения запросов и построение графиков
measure_and_plot_requests(request_functions, 100)
