FROM alpine

ENV PIPENV_VENV_IN_PROJECT=1

RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install pipenv --break-system-packages
WORKDIR /data

CMD sh -c "pipenv install && \
pipenv run pip3 install tzdata && \
pipenv run python3 manage.py migrate && \
pipenv run python3 manage.py runserver 0.0.0.0:8000"

