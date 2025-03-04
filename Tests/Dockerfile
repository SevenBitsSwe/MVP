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
RUN mkdir -p app/SimulationModule
RUN mkdir -p app/FlinkProcessor
RUN mkdir -p app/Tests

# Copy each directory into a temporary location
COPY ./SimulationModule/Tests /tmp/SimulationModuleTests/
COPY ./FlinkProcessor/Tests /tmp/FlinkProcessorTests/
COPY ./IntegrationTests /tmp/IntegrationTests/
COPY ./SystemTests /tmp/SystemTests/

# Concatenate them into the final destination (/app/tests)
RUN cp -r /tmp/SimulationModuleTests/* /app/tests/ && \
    cp -r /tmp/FlinkProcessorTests/* /app/tests/ && \
    cp -r /tmp/IntegrationTests/* /app/tests/ && \
    cp -r /tmp/SystemTests/* /app/tests/

# Clean up the temporary directories
RUN rm -rf /tmp/SimulationModuleTests /tmp/FlinkProcessorTests /tmp/IntegrationTests /tmp/SystemTests

# Copia il codice sorgente e i test
COPY ./SimulationModule/ /app/SimulationModule
COPY ./FlinkProcessor /app/FlinkProcessor


RUN apt-get update -y && \
apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest pytest-cov coveralls pylint

# Crea directory per i report
COPY ./__init__.py /app/

RUN chmod -R 777 /app
# Esegue i test con coverage
CMD ["sh","-c","pylint --rcfile=pylintrc --output-format=parseable . > pylint_report.txt; pytest --cov=SimulationModule --cov=FlinkProcessor --cov-report=xml:coverage.xml tests/ --cov-config=.coveragerc "]


# # Costruisci l'immagine
# docker build -t python-test-coverage -f tests/Dockerfile .

# # Esegui i test e monta un volume per accedere ai report
# docker run --rm -v $(pwd)/reports:/app/reports python-test-coverage