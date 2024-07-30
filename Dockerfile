FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 1234
ENV NOM Cédric
CMD ["python", "app.py"]
