import requests
import datetime
import os

# Lista de URLs a monitorizar
URLS = [
    "https://google.com",
    "https://github.com",
    "https://ejemplo-caido.com"
]

LOG_FILE = "monitor.log"

def log(mensaje):
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{ahora}] {mensaje}"
    print(linea)
    with open(LOG_FILE, "a") as f:
        f.write(linea + "\n")

def verificar_url(url):
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            log(f"✅ OK       - {url}")
        else:
            log(f"⚠️  ERROR {respuesta.status_code} - {url}")
    except Exception:
        log(f"❌ CAÍDO    - {url}")

def ejecutar_monitor():
    log("🔍 Iniciando comprobación de servicios...")
    for url in URLS:
        verificar_url(url)
    log("✅ Comprobación finalizada.\n")

ejecutar_monitor()
