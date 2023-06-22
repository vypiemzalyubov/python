FROM python

WORKDIR /4. Creating framework. Running in Docker

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV ENV=dev

CMD python -m pytest -s tests/* --alluredir=test_results/