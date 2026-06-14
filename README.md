# Service Monitor

Script en Python que monitoriza el estado de servicios web y guarda un historial de logs.

## Que hace

- Comprueba si una lista de URLs estan online
- Detecta servicios caidos o con errores
- Guarda un historial en un fichero de log con fecha y hora

## Tecnologias

- Python 3
- requests
- Docker

## Como usarlo

### Con Python

pip install requests
python monitor.py

### Con Docker

docker build -t service-monitor .
docker run service-monitor

## Ejemplo de salida

[2026-06-14 17:30:00] Iniciando comprobacion de servicios...
[2026-06-14 17:30:01] OK - https://google.com
[2026-06-14 17:30:02] OK - https://github.com
[2026-06-14 17:30:07] CAIDO - https://ejemplo-caido.com
[2026-06-14 17:30:07] Comprobacion finalizada.

## Autor

Ayaxlc - https://github.com/Ayaxlc