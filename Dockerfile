FROM python:3.9.4
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=1
ENTRYPOINT [ "python", "main.py" ]
