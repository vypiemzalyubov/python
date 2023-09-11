FROM python

WORKDIR /4. Creating framework. Running in Docker

VOLUME /allure-results

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python -m pytest -s -v tests/* --alluredir=allure-results/