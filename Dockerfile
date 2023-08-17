FROM python:3.11-slim

RUN apt-get update

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV MONGO_STRING = 'mongodb+srv://python:python07@cluster0.sxx9jqd.mongodb.net/?retryWrites=true&w=majority'


WORKDIR /app

COPY requirements.txt .
RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

