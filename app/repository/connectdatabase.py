import oracledb
from app.repository.settings import DB_CONFIG

def connect_database():
    return oracledb.connect(
        user=DB_CONFIG["user"], 
        password=DB_CONFIG["password"], 
        dsn=DB_CONFIG["dsn"]
    )