import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL di partenza
base_url = "pngohttps://"

# Proviamo a prendere la pagina principale del sito
main_url = "https://store.supercell.com/images/moco/"
response = requests.get(main_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Troviamo tutti i link nel sito
    links = [urljoin(main_url, a['href']) for a in soup.find_all('a', href=True)]

    # Troviamo tutte le immagini
    images = [urljoin(main_url, img['src']) for img in soup.find_all('img', src=True)]

    print("\n🔗 Link trovati:")
    for link in links:
        print(link)

    print("\n🖼️ Immagini trovate:")
    for img in images:
        print(img)
else:
    print("Errore nel caricamento della pagina principale.")
