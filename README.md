# NearYou - Sistema di Notifiche Personalizzate basate sulla Posizione
[![Continuos Integration & Quality Checks](https://github.com/SevenBitsSwe/MVP/actions/workflows/main.yml/badge.svg)](https://github.com/SevenBitsSwe/MVP/actions/workflows/main.yml)
![pylint](https://img.shields.io/badge/PyLint-9.67-brightgreen?logo=python&logoColor=white)
![Line coverage](https://img.shields.io/badge/Line%20coverage-100.0%25-brightgreen?logo=python&logoColor=white)
![Branch coverage](https://img.shields.io/badge/Branch%20coverage-100.0%25-brightgreen?logo=python&logoColor=white)

Questo **MVP (Minimum Viable Product)** implementa una piattaforma per l'invio di notifiche pubblicitarie personalizzate basate sulla posizione dell'utente, sui suoi interessi e sui punti di interesse nelle vicinanze. Il sistema utilizza basato su tecnologie moderne come **Apache Flink**, **Grafana**, e **ClickHouse** e un **Large Language Model (LLM)** per creare un'esperienza personalizzata in tempo reale.

## Architettura del Sistema

Il sistema è composto da diversi moduli containerizzati che collaborano per fornire un'infrastruttura completa:

- **Simulatore di dati**: Genera dati simulati da sensori o altre fonti.
- **Processore Flink**: Elabora i dati in tempo reale, li arricchisce con informazioni contestuali tramite LLM e poi li valida.
- **Database ClickHouse**: Memorizza dati storici in tempo relae e dati statici per le informazioni generali.
- **Dashboard Grafana**: Visualizza i dati elaborati in tempo reale tramite dashboard personalizzate.

## Struttura del Progetto

### FlinkProcessor/
Contiene l'applicazione Apache Flink per l'elaborazione dei dati in tempo reale. Include il codice per validare, arricchire (tramite LLM) e processare i dati provenienti dai sensori.

### SimulationModule/
Serve a simulare l'invio di dati da sensori GPS.

### StorageData/
Contiene schemi e script SQL per il database ClickHouse. Questi file definiscono la struttura del database e le viste necessarie per l'analisi dei dati.

### Grafana/
Configurazione per la visualizzazione dei dati. Include dashboard preconfigurate e impostazioni per il provisioning delle fonti di dati.

## Come Avviare il Progetto

Il progetto utilizza Docker Compose per orchestrare tutti i servizi. Per avviare l'intero sistema, seleziona il profilo appropriato in base all'ambiente desiderato:

### Ambiente di Produzione

Questo ambiente è progettato per essere stabile e rappresentare una versione funzionante del sistema. È ideale per dimostrazioni e per mostrare il prodotto in azione, evidenziandone le funzionalità principali.

1. Clona il repository:
   ```bash
   git clone https://github.com/SevenBitsSwe/MVP.git
   cd MVP
   ```

2. Configura il file `.env`:
   Crea un file `.env` nella directory principale e aggiungi la seguente variabile:
   ```properties
   PYTHON_PROGRAM_KEY=CHIAVE_GROQ
   ```
   Sostituisci `CHIAVE_GROQ` con la chiave effettiva fornita.

3. Avvia i servizi con il profilo `prod`:
   ```bash
   docker-compose up --profile prod --build
   ```

4. Accedi a Grafana all'indirizzo [http://localhost:3000](http://localhost:3000) con le credenziali predefinite:
   - **Username**: `admin`
   - **Password**: `admin`

### Ambiente di Test

Questo ambiente è pensato per eseguire test approfonditi sul sistema consentendo di generare report sullo stato di salute del progetto.

1. Clona il repository (se non già fatto):
   ```bash
   git clone https://github.com/SevenBitsSwe/MVP.git
   cd MVP
   ```

2. Configura il file `.env` come descritto sopra.

3. Avvia i servizi con il profilo `test`:
   ```bash
   docker-compose up --profile test --build
   ```

### Ambiente di Sviluppo

Questo ambiente è dedicato agli sviluppatori per sperimentare e implementare nuove funzionalità. È ideale per attività di debugging e sviluppo iterativo.

1. Clona il repository (se non già fatto):
   ```bash
   git clone https://github.com/SevenBitsSwe/MVP.git
   cd MVP
   ```

2. Configura il file `.env` come descritto sopra.

3. Avvia i servizi con il profilo `develop`:
   ```bash
   docker-compose up --profile develop --build
   ```

## Requisiti

- **Docker** e **Docker Compose**
- Chiave API per il servizio Groq (da configurare in un file `.env`)