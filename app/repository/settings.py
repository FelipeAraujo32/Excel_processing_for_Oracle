import os
from dotenv import load_dotenv


load_dotenv() # Carrega as variáveis do arquivo .env

# Dados mockados
DB_CONFIG = {
    "user": os.getenv("ORACLE_USER"),
    "password": os.getenv("ORACLE_PASSWORD"),
    "dsn": os.getenv("ORACLE_DNS"),
}