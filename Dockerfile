FROM python3
WORKDIR /app
COPY ./src /app
RUN cp /data /app
RUN chmod +x TextCounter

