import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from bs4 import BeautifulSoup
from tabulate import tabulate

# ▶️ Masquer les logs de Chrome natif
sys.stderr = open(os.devnull, 'w')

# ▶️ Demande de l'URL
url = input("👉 Entrez l'URL de la fiche entreprise : ").strip()

# 🔧 Configuration de Chrome (mode headless + suppression des logs)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument("--lang=fr-FR")
options.add_argument("--log-level=3")  # Affiche seulement les erreurs critiques
options.add_argument("--disable-logging")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 🚫 Redirection des logs ChromeDriver
service = Service(log_path='nul')  # 'nul' pour Windows, '/dev/null' pour Linux/macOS
driver = webdriver.Chrome(service=service, options=options)

# 🕵️ Activation du mode furtif
stealth(driver,
    languages=["fr-FR", "fr"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

# 🌐 Chargement de la page
print("\n[+] Chargement de la page...")
try:
    driver.get(url)
    time.sleep(3)
except Exception as e:
    print(f"[!] Erreur lors du chargement de l'URL : {e}")
    driver.quit()
    exit()

# 🔍 Extraction du contenu HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# 📦 Fonctions d'extraction
def safe_select_text(soup, selector, label):
    el = soup.select_one(selector)
    return el.get_text(strip=True) if el else f"[!] {label} introuvable"

def safe_table_value(soup, th_text):
    ths = soup.find_all("th")
    for th in ths:
        th_clean = th.get_text(strip=True).replace("\xa0", " ").strip().lower()
        if th_text.strip().lower() in th_clean:
            td = th.find_next_sibling("td")
            return td.get_text(strip=True) if td else f"[!] Cellule manquante pour {th_text}"
    return f"[!] Ligne '{th_text}' non trouvée"

# 📝 Données extraites
data = {
    "Nom": safe_select_text(soup, "#resume h1.big-text", "Nom"),
    "SIREN": safe_table_value(soup, "SIREN :"),
    "SIRET (siège)": safe_table_value(soup, "SIRET (siège) :"),
    "Forme juridique": safe_table_value(soup, "Forme juridique :"),
    "Numéro de TVA": safe_table_value(soup, "Numéro de TVA:"),
    "Inscription au RCS": safe_table_value(soup, "Inscription au RCS :"),
    "Inscription au RNE": safe_table_value(soup, "Inscription au RNE :"),
    "Numéro RCS": safe_table_value(soup, "Numéro RCS :"),
    "Capital social": safe_table_value(soup, "Capital social :"),
    "Statut": safe_select_text(soup, ".siren-statut .status span", "Statut"),
    "Adresse": safe_table_value(soup, "Adresse :"),
    "Activité": safe_table_value(soup, "Activité :"),
    "Effectif": safe_table_value(soup, "Effectif :"),
    "Création": safe_table_value(soup, "Création :"),
    "Dirigeant": safe_select_text(soup, "td.info-dirigeant a", "Dirigeant"),
    "Activité principale déclarée": safe_table_value(soup, "Activité principale déclarée :"),
    "Code NAF ou APE": safe_table_value(soup, "Code NAF ou APE :"),
    "Domaine d’activité": safe_table_value(soup, "Domaine d’activité :"),
    "Forme d'exercice": safe_table_value(soup, "Forme d'exercice :"),
    "Convention collective": safe_table_value(soup, "Convention collective :"),
    "Clôture d'exercice": safe_table_value(soup, "Date de clôture d'exercice comptable :"),
}

# 📤 Affichage des résultats en tableau
print("\n--- 📊 Données extraites ---\n")
table = [[key, value] for key, value in data.items()]
print(tabulate(table, headers=["Champ", "Valeur"], tablefmt="grid"))

driver.quit()