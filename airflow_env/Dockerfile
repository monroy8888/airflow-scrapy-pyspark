FROM apache/airflow:2.0.1
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
RUN pip install --no-cache-dir --user apache-airflow-providers-papermill==1.0.1