
def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    # Спроба виклику функції, яку декоруємо
                    return func(*args, **kwargs)
                except Exception as e:
                    # Обробка помилки та вивід повідомлення про спробу
                    print(f"Помилка: {e}. Повторна спроба {retries + 1}/{max_retries}")
                    retries += 1
            # Викидаємо виняток, якщо досягнуто максимальну кількість спроб
            raise Exception("Досягнуто максимальну кількість спроб")
        return wrapper
    return decorator

# Параметризоване застосування декоратора
@retry(max_retries=5)
def connect_to_server():
    # Спроба з'єднатися з сервером
    raise ConnectionError("Не вдалося підключитися до сервера")

# Виклик функції
connect_to_server()