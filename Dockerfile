FROM mcr.microsoft.com/playwright/python:v1.61.0-noble

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

COPY . /app

CMD ["pytest", "-m", "smoke", "--alluredir=allure-results"]
#pytest -m smoke