FROM --platform=linux/amd64 alpine

ENV PIPENV_VENV_IN_PROJECT=1

RUN apk update
RUN apk add python3-dev
RUN apk add gcc libc-dev linux-headers libffi-dev
RUN apk add py3-pip
RUN apk add libpq-dev
RUN pip3 install pipenv --break-system-packages
WORKDIR /data

CMD sh -c "pipenv install && \
pipenv run pip3 install tzdata && \
pipenv run python3 manage.py migrate neuronaApp && \
pipenv run python3 manage.py migrate neuronaLogs --database logs \
pipenv run python3 manage.py runserver 0.0.0.0:8000"

