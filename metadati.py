import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from collections import defaultdict
from prettytable import PrettyTable

# Definisci la cartella di destinazione
DEST_DIR = "SCRIVI QUA"

# Funzione per estrarre i metadati EXIF da un'immagine
def extract_exif_data(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        if not exif_data:
            return None  # Nessun metadato EXIF presente
        exif = {}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "GPSInfo":
                gps_data = {}
                for gps_tag_id, gps_value in value.items():
                    gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                    gps_data[gps_tag] = gps_value
                exif[tag] = gps_data
            else:
                exif[tag] = value
        return exif
    except Exception as e:
        print(f"Errore durante l'estrazione dei metadati da {image_path}: {e}")
        return None

# Funzione per analizzare tutte le foto e riepilogare i metadati
def analyze_photos(dest_dir):
    # Dizionario per memorizzare i conteggi dei metadati
    metadata_summary = defaultdict(int)

    # Scansiona tutti i file nella cartella di destinazione
    for root, _, files in os.walk(dest_dir):
        for file in files:
            file_path = os.path.join(root, file)
            exif_data = extract_exif_data(file_path)
            if exif_data:
                # Conta i tipi di metadati trovati
                if "DateTimeOriginal" in exif_data:
                    metadata_summary["Foto con data di scatto"] += 1
                if "Make" in exif_data:
                    metadata_summary[f"Fotocamera ({exif_data['Make']})"] += 1
                if "Model" in exif_data:
                    metadata_summary[f"Modello fotocamera ({exif_data['Model']})"] += 1
                if "GPSInfo" in exif_data:
                    metadata_summary["Foto con geolocalizzazione"] += 1
            else:
                metadata_summary["Foto senza metadati EXIF"] += 1

    # Genera una tabella con i risultati
    table = PrettyTable()
    table.field_names = ["Tipo di Metadato", "Numero di Foto"]
    for key, value in metadata_summary.items():
        table.add_row([key, value])

    # Stampa la tabella
    print("Riepilogo dei metadati EXIF:")
    print(table)

# Esegui la funzione
analyze_photos(DEST_DIR)
