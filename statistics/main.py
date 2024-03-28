import requests
import time
from api import *
import matplotlib.pyplot as plt

API_URL = "http://localhost:8080"

# Функция для отправки запроса к API
def make_request(resource):
    start_time = time.time()
    response = requests.get(f"{API_URL}/{resource}")
    end_time = time.time()
    return end_time - start_time

# Функция для тестирования смены бэкэнда
def test_backend_rotation(resource, num_requests):
    times = []
    for _ in range(num_requests):
        time_taken = make_request(resource)
        times.append(time_taken)
    return sum(times) / len(times)

# Функция для тестирования влияния количества экземпляров компонентов
def test_component_performance(resource, num_components, num_requests):
    times = []
    for _ in range(num_requests):
        for _ in range(num_components):
            time_taken = make_request(resource)
            times.append(time_taken)
    return sum(times) / len(times)

# Ресурсы для тестирования
resources = ["items", "basket", "orders"]

# Конфигурации для тестирования
backend_configurations = ["nginx1"]  # Пример смены бэкэнда
component_configurations = [1, 2, 3]  # Пример количества экземпляров компонентов

# Замеры для различных конфигураций
results_backend = {}
results_components = {}

# Тестирование смены бэкэнда
for resource in resources:
    results_backend[resource] = {}
    for backend in backend_configurations:
        results_backend[resource][backend] = test_backend_rotation(resource, 100)

# Тестирование влияния количества экземпляров компонентов
for resource in resources:
    results_components[resource] = {}
    for num_components in component_configurations:
        results_components[resource][num_components] = test_component_performance(resource, num_components, 100)

# Построение графиков
plt.figure(figsize=(15, 5 * len(resources)))

for idx, resource in enumerate(resources, start=1):
    plt.subplot(len(resources), 1, idx)
    plt.title(f"{resource.capitalize()} Производительность")
    #plt.xlabel(f'Конфигурация ')
    plt.ylabel('Среднее время выполнения запроса (s)')

    backend_data = results_backend[resource][backend_configurations[0]]
    component_data = results_components[resource]

    # График для среднего времени выполнения запроса при различных конфигурациях бэкэнда
    plt.bar([f"{backend}\n(GET)" for backend in backend_configurations], [backend_data] * len(backend_configurations), color='skyblue')
    #plt.xticks(rotation=45)

    # График для среднего времени выполнения запроса при различном количестве экземпляров компонентов
    plt.bar([f"(POST) с кол-вом компонентов = {n} " for n in component_data.keys()], component_data.values(), color='lightgreen')
    plt.bar()
    plt.bar()
    plt.bar()
    plt.bar()
plt.tight_layout()
plt.show()
