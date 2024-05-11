FROM python:3.10.2

WORKDIR /ai-image-generator

COPY src/ src/
COPY Makefile .
COPY .env .
COPY requirements.txt .

RUN apt install make
RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT make run