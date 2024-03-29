import os
import pickle
import sys
from matplotlib import pyplot as plt
from main import methods


def get_data(method_name: str, conf: str) -> float:
    data_path = os.path.join(os.getcwd(), 'graphics', conf, 'data')
    times = pickle.load(open(os.path.join(data_path, f'{method_name}.pickle'), 'rb'))
    return sum(times) / len(times)


def draw(method_name: str, data: dict[str, float]):
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.suptitle(f'{method_name} execution time')

    ax.bar(list(data.keys()), list(data.values()), color='skyblue')
    ax.set_xlabel('Request')
    ax.set_ylabel('Average time (s)')
    ax.set_title(f'{method_name}')

    plt.savefig(os.path.join(os.getcwd(), 'graphics', 'summary', f'{method_name}.png'))
    if need_show:
        plt.show()


configs = [
    'full',
    'one_pg',
    'onepgpool',
    'oneweb'
]

if __name__=='__main__':
    need_show = eval(sys.argv[1])
    os.makedirs(os.path.join(os.getcwd(), 'graphics', 'summary'), exist_ok=True)
    data = {}
    for method in methods:
        floats = {}
        for conf in configs:
            floats[conf] = get_data(method, conf)
        data[method] = floats
    for method in data.keys():
        draw(method, data[method])

