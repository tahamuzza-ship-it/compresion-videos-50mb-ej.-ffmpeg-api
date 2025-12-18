FROM jrottenberg/ffmpeg:6.1-alpine

RUN apk add --no-cache python3 py3-pip

WORKDIR /app
COPY app.py /app/app.py

RUN pip install flask

EXPOSE 8080
CMD ["python3", "app.py"]
