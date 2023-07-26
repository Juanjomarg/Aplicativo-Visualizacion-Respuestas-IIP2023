FROM python:3.9.5
WORKDIR /app
COPY . /app/
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8050

#CMD ["python", "app.py"]
#CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app:server"]
#CMD ["gunicorn", "-D", "--bind", "0.0.0.0:8050", "app:server"]
#CMD ["gunicorn", "-D", "--bind", "0.0.0.0:8050", "--log-level", "debug", "app:server"]
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "--log-level", "debug", "app:server"]
