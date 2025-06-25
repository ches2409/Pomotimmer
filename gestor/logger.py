import logging
from logging.handlers import RotatingFileHandler
import os

# Crear carpeta de logs si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configurar el logger
log_file = "logs/app.log"

# Crear el handler con rotación (máx 1MB por archivo, 5 copias)
file_handler = RotatingFileHandler(
    log_file, maxBytes=1_000_000, backupCount=5, encoding="utf-8"
)

# Formato del log
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Obtener el logger raíz
logger = logging.getLogger("gestor_app")
logger.setLevel(logging.DEBUG)  # Puedes usar INFO en producción
logger.addHandler(file_handler)

# Evitar duplicados si ya existen handlers
logger.propagate = False