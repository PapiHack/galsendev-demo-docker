FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt ./
# or COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .
# or COPY . /code/