FROM python:3-alpine3.16

WORKDIR /app_files

EXPOSE 5000
ENV FLASK_APP=run.py

COPY . /app_files
RUN pip install -r requirements.txt

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]
