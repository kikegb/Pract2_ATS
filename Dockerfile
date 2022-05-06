FROM python:3
WORKDIR /app
COPY ./src /app
RUN chmod +x TextCounter.py
CMD ["/bin/bash", "-c", "cp -rf /data/* /app/"]