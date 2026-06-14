import requests
import datetime

# Lista de URLs a monitorizar
URLS = [
    "https://google.com",
    "https://github.com",
    "https://ejemplo-caido.com"
]

def verificar_url(url):
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code == 200:
            return f"✅ OK       - {url}"
        else:
            return f"⚠️  ERROR {respuesta.status_code} - {url}"
    except Exception:
        return f"❌ CAÍDO    - {url}"

def ejecutar_monitor():
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🔍 Comprobando servicios - {ahora}\n")
    for url in URLS:
        resultado = verificar_url(url)
        print(resultado)

ejecutar_monitor()