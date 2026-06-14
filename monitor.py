import requests
import datetime

URLS = [
    "https://google.com",
    "https://github.com",
    "https://ejemplo-caido.com"
]

LOG_FILE = "monitor.log"

def log(mensaje):
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = "[" + ahora + "] " + mensaje
    print(linea)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linea + "\n")

def verificar_url(url):
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            log("OK - " + url)
        else:
            log("ERROR " + str(respuesta.status_code) + " - " + url)
    except Exception:
        log("CAIDO - " + url)

def ejecutar_monitor():
    log("Iniciando comprobacion de servicios...")
    for url in URLS:
        verificar_url(url)
    log("Comprobacion finalizada.")

ejecutar_monitor()