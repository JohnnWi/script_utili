import os
import shutil
from math import ceil

# Percorso della cartella sorgente
source_folder = 'SCRIVI QUA'

# Percorso di destinazione principale
destination_root = 'SCRIVI QUA'

# Numero di parti in cui suddividere i file
num_parts = 4

# Ottieni tutti i file (escludendo cartelle)
all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

# Calcola il numero di file per parte
files_per_part = ceil(len(all_files) / num_parts)

# Crea le sottocartelle e sposta i file
for i in range(num_parts):
    part_folder = os.path.join(destination_root, f'Parte_{i+1}')
    os.makedirs(part_folder, exist_ok=True)
    
    start = i * files_per_part
    end = start + files_per_part
    for file_name in all_files[start:end]:
        src_path = os.path.join(source_folder, file_name)
        dst_path = os.path.join(part_folder, file_name)
        shutil.move(src_path, dst_path)

print("Divisione completata in 4 parti.")
