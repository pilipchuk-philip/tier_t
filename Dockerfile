FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python3", "-m" , "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]