import oracledb
from app.repository.connectdatabase import connect_database
from pathlib import Path

class MergeService:
    
     #Function to connect to the bank
    def __init__(self):
        try:
            self.conn = connect_database()
            self.cursor = self.conn.cursor()
        except oracledb.Error as e:
            print("Erro ao conectar ao banco de dados.")
            raise e
        
    #Loading sql code   
    def load_sql(self, path: str) -> str:
        try:
            return Path(path).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {path}")
            raise
        
    def merge_sql(self, path: str):
        try:
            sql = self.load_sql(path)
            self.cursor.execute(sql)
            self.conn.commit()
            print(f"Script merge executado com sucesso.")
        except oracledb.Error as e:
            error, = e.args
            print("Erro Oracle:")
            print(f"Code: {error.code}")
            print(f"Message: {error.message}")
            self.conn.rollback()
            raise