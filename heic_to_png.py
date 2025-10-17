from PIL import Image
import pillow_heif
from pathlib import Path

# Registra il formato HEIC con Pillow
pillow_heif.register_heif_opener()

def converti_heic_in_png(cartella):
    """
    Converte tutti i file HEIC in PNG nella cartella specificata
    """
    cartella_path = Path(cartella)
    
    # Trova tutti i file HEIC (case-insensitive)
    file_heic = list(cartella_path.glob("*.heic")) + list(cartella_path.glob("*.HEIC"))
    
    if not file_heic:
        print("Nessun file HEIC trovato nella cartella.")
        return
    
    print(f"Trovati {len(file_heic)} file HEIC da convertire...\n")
    
    convertiti = 0
    errori = 0
    
    for file_heic in file_heic:
        try:
            # Apri l'immagine HEIC
            immagine = Image.open(file_heic)
            
            # Crea il nome del file PNG
            file_png = file_heic.with_suffix('.png')
            
            # Salva come PNG
            immagine.save(file_png, 'PNG')
            
            print(f"✓ Convertito: {file_heic.name} → {file_png.name}")
            convertiti += 1
            
        except Exception as e:
            print(f"✗ Errore con {file_heic.name}: {str(e)}")
            errori += 1
    
    print(f"\n{'='*50}")
    print(f"Conversione completata!")
    print(f"File convertiti con successo: {convertiti}")
    print(f"Errori: {errori}")
    print(f"{'='*50}")

if __name__ == "__main__":
    cartella = "inserisci percorso qua"
    converti_heic_in_png(cartella)
