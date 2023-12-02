FROM python:3.9
COPY . /usr/application
WORKDIR /usr/application
#ENV APP_URL=${APP_URL}
#ENV APP_URL=http://backend:8000
EXPOSE 5000
RUN cat requirements.txt | xargs -n 1 -L 1 python -m pip install
#ENTRYPOINT ["python", "app.py"]