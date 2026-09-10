import time
import memory_profiler


# 1. Варіант зі списком (Eager / No Generator)
def check_even_list(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num * num)
    return even


# 2. Варіант із генератором (Lazy / With Generator)
def check_even_generator(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


def run_benchmark(func_name, target_func, data_range):
    m_start = memory_profiler.memory_usage()[0]
    t_start = time.perf_counter()

    # Виконання функції
    result = target_func(data_range)

    # Якщо це генератор — обходимо його, щоб форсувати обчислення
    if hasattr(result, "__next__"):
        for _ in result:
            pass

    t_end = time.perf_counter()
    m_end = memory_profiler.memory_usage()[0]

    elapsed_time = t_end - t_start
    memory_used = max(0.0, m_end - m_start)

    print(f"| {func_name:<20} | {elapsed_time:>10.4f} с | {memory_used:>10.2f} МБ |")


if __name__ == "__main__":
    limit = 90_000_000
    print(f"Тестування на діапазоні: range({limit:,})\n")
    print("| Підхід               |        Час |     Пам'ять |")
    print("|" + "-" * 22 + "|" + "-" * 13 + "|" + "-" * 13 + "|")

    # # Запуск 1: Без генератора
    # run_benchmark("Список (No Gen)", check_even_list, range(limit))

    # Запуск 2: З генератором
    run_benchmark("Генератор (With Gen)", check_even_generator, range(limit))