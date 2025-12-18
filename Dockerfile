FROM jrottenberg/ffmpeg:6.1-alpine

# 🔴 IMPORTANTE: borrar entrypoint de ffmpeg
ENTRYPOINT []

RUN apk add --no-cache python3 py3-flask

WORKDIR /app
COPY app.py /app/app.py

EXPOSE 8080

CMD ["python3", "/app/app.py"]
