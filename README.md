
Questa repository raccoglie una serie di script Python utili per la gestione, organizzazione e analisi di file multimediali, immagini e scraping web.

---

## 📦 Requisiti generali

Tutti gli script richiedono Python 3.9+ e alcuni pacchetti Python. Puoi installarli con:

```bash
pip install Pillow pillow-heif prettytable requests beautifulsoup4
````

> Alcuni script utilizzano solo un sottoinsieme di questi pacchetti.

---

## 📑 Tabella dei contenuti

1. [Unione di file da più cartelle](#1-unione-di-file-da-più-cartelle-unione_fotopy)
2. [Divisione dei file in sottocartelle](#2-divisione-dei-file-in-sottocartelle-divisionepy)
3. [Analisi dei metadati EXIF](#3-analisi-dei-metadati-exif-analisi_exifpy)
4. [Web scraping di link e immagini](#4-web-scraping-di-link-e-immagini-scraping_webpy)
5. [Conversione da HEIC a PNG](#5-conversione-da-heic-a-png-converti_heicpy)

---

## 1. Unione di file da più cartelle (`unione_foto.py`)

* **Descrizione:**
  Scansiona una cartella sorgente e tutte le sue sottocartelle, copiando tutti i file in una cartella di destinazione. Rinomina automaticamente eventuali duplicati.
* **Pacchetti richiesti:** `os`, `shutil`
* **Funzionalità principali:**

  * Raccoglie tutti i file da una directory e le sue sottocartelle.
  * Mostra un riepilogo delle estensioni dei file trovati.
  * Copia i file nella cartella di destinazione rinominando i duplicati.

---

## 2. Divisione dei file in sottocartelle (`divisione.py`)

* **Descrizione:**
  Divide i file presenti in una cartella in più sottocartelle in modo uniforme.
* **Pacchetti richiesti:** `os`, `shutil`
* **Funzionalità principali:**

  * Suddivide grandi collezioni di file in più sottocartelle.
  * Utile per organizzare raccolte di foto, video o altri file in parti gestibili.

---

## 3. Analisi dei metadati EXIF (`analisi_exif.py`)

* **Descrizione:**
  Analizza tutte le immagini in una cartella e genera un riepilogo dei metadati EXIF (data di scatto, modello fotocamera, geolocalizzazione, ecc.).
* **Pacchetti richiesti:** `Pillow`, `collections`, `prettytable`, `os`
* **Funzionalità principali:**

  * Estrae metadati EXIF dalle immagini.
  * Riepiloga i dati in una tabella leggibile.
  * Conta le foto senza metadati EXIF.

---

## 4. Web scraping di link e immagini (`scraping_web.py`)

* **Descrizione:**
  Effettua una richiesta HTTP a un sito web, analizza il contenuto HTML e mostra tutti i link e le immagini presenti nella pagina.
* **Pacchetti richiesti:** `requests`, `beautifulsoup4`, `urllib.parse`
* **Funzionalità principali:**

  * Estrae tutti i link (`<a href>`) e le immagini (`<img src>`) da una pagina web.
  * Visualizza i risultati nel terminale.

---

## 5. Conversione da HEIC a PNG (`converti_heic.py`)

* **Descrizione:**
  Converte tutti i file HEIC presenti in una cartella in formato PNG, mantenendo il nome originale e mostrando il numero di file convertiti e eventuali errori.
* **Pacchetti richiesti:** `Pillow`, `pillow-heif`, `pathlib`
* **Funzionalità principali:**

  * Supporta file HEIC sia in maiuscolo che minuscolo.
  * Converte in PNG preservando il contenuto dell’immagine.
  * Mostra un riepilogo dei file convertiti e degli errori.

---

## ⚡ Uso rapido

1. Clona la repository:

```bash
git clone https://github.com/tuo-username/multimedia-utility-scripts.git
cd multimedia-utility-scripts
```

2. Modifica le variabili di percorso (`SOURCE_DIR`, `DEST_DIR`, `cartella`) negli script secondo le tue cartelle.

3. Esegui gli script con Python:

```bash
python unione_foto.py
python divisione.py
python analisi_exif.py
python scraping_web.py
python converti_heic.py
```

---

Questa raccolta di script è pensata per **semplificare la gestione di file multimediali**, organizzare foto, estrarre metadati, convertire immagini e automatizzare operazioni ripetitive.

```

---

Se vuoi, posso anche fare una **versione con colori e badge aggiuntivi**, tipo “Build Passing”, “License MIT”, e un box con tutti i requisiti Python separati per ogni script, così il README sembrerà **professionale come una repo pubblica su GitHub**.  

Vuoi che faccia anche quella versione avanzata?
```
