FROM apache/flink:1.18.1-scala_2.12-java11


# install python e pip


# install required requirements anche se li ho chiamati con un altro file


# SCarica connettore kafka flink
RUN mkdir -p /opt/flink/usrlib
RUN wget -P /opt/flink/usrlib https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/3.2.0-1.18/flink-sql-connector-kafka-3.2.0-1.18.jar
RUN wget -P /opt/flink/usrlib https://repo1.maven.org/maven2/com/clickhouse/clickhouse-jdbc/0.7.0/clickhouse-jdbc-0.7.0.jar 

RUN wget -P /opt/flink/usrlib https://repo1.maven.org/maven2/org/apache/flink/flink-connector-jdbc/3.1.2-1.18/flink-connector-jdbc-3.1.2-1.18.jar

WORKDIR /app

# Copia i file necessari
COPY Tests/requirements.txt .
COPY Tests/.coveragerc .
COPY Tests/pylintrc .
COPY Tests/pytest.ini .
COPY Tests/getReports.py .
RUN chmod 777 getReports.py
RUN mkdir -p app/SimulationModule
RUN mkdir -p app/FlinkProcessor
RUN mkdir -p app/IntegrationTests
RUN mkdir -p app/SystemTests


# Copia il codice sorgente e i test
COPY ./SimulationModule /app/SimulationModule
COPY ./FlinkProcessor /app/FlinkProcessor
COPY ./Tests/IntegrationTests /app/IntegrationTests
COPY ./Tests/SystemTests /app/SystemTests

RUN apt-get update -y && \
apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-cov coveralls pylint

# Crea directory per i report
COPY ./__init__.py /app/
COPY ./__init__.py /app/SimulationModule/
COPY ./__init__.py /app/FlinkProcessor/

# Crea directory /app/test-results per i report
RUN mkdir -p /app/reports && \
    chmod -R 777 /app/reports

RUN chmod -R 777 /app

RUN ls -la /app
# Esegue i test con coverage
CMD ["sh","-c","pylint --rcfile=pylintrc --output-format=parseable . > /app/reports/pylint_report.txt; \
    pytest -c=pytest.ini \
    --cov=./ \
    --cov-report=xml:/app/reports/coverage.xml \
    SimulationModule/Tests/ \
    FlinkProcessor/Tests/ \
    IntegrationTests/ \
    --cov-branch \
    --cov-config=.coveragerc; \
    python getReports.py"]


# # Costruisci l'immagine
# docker build -t python-test-coverage -f tests/Dockerfile .  

# # Esegui i test e monta un volume per accedere ai report
# docker run --rm -v $(pwd)/reports:/app/reports python-test-coverage