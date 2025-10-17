import os
import shutil

# Definisci la cartella di origine e quella di destinazione
SOURCE_DIR = "SCRIVI QUA"
DEST_DIR = "SCRIVI QUA"

# Crea la cartella di destinazione se non esiste
os.makedirs(DEST_DIR, exist_ok=True)

# Funzione per raccogliere tutti i file con le loro estensioni
def analyze_and_copy(source_dir, dest_dir):
    # Lista per memorizzare i file trovati
    found_files = []

    # Scansiona ricorsivamente la directory di origine
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            found_files.append(source_path)

    # Stampa un riepilogo delle estensioni trovate
    extensions = set()
    for file in found_files:
        _, ext = os.path.splitext(file)
        if ext:
            extensions.add(ext.lower())

    print("Estensioni trovate:")
    for ext in sorted(extensions):
        print(f"  - {ext}")

    # Copia tutti i file nella cartella di destinazione
    for source_path in found_files:
        file_name = os.path.basename(source_path)
        dest_path = os.path.join(dest_dir, file_name)

        # Se il file esiste già nella cartella di destinazione, aggiungi un suffisso numerico
        counter = 1
        while os.path.exists(dest_path):
            name, ext = os.path.splitext(file_name)
            dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
            counter += 1

        # Copia il file
        shutil.copy2(source_path, dest_path)
        print(f"Copiato: {source_path} -> {dest_path}")

    print("\nOperazione completata. Tutti i file sono stati copiati nella cartella di destinazione.")

# Esegui la funzione
analyze_and_copy(SOURCE_DIR, DEST_DIR)
