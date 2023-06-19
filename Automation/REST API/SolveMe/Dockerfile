FROM python3.11-alpine

ARG run_env
ENV env $run_env

LABEL "myproject" = "api_testing"
LABEL "creator" = "vypiemzalyubov"

WORKDIR /API Testing

VOLUME /allure-result

COPY requirements.txt .

RUN pip install -r requirements.txt

# RUN apk update && apk upgrade && apk add bash

COPY . .

CMD pytest -m "$env" -s -v tests/test_api.py --alluredir=allure-result

# docker build -t api-testing .
# docker build --build-arg run_env=dev -t api-testing .
# docker run api-testing
# docker cp ${docker ps -a -q | head -1}:/API Testing/allure-result .