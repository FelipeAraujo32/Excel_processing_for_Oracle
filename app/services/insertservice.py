import oracledb
from app.repository.connectdatabase import connect_database
from pathlib import Path

class InsertService:
    
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

    
    def insert_data_sql(self, registros: str,  path: str):
        try:
            sql = self.load_sql(path)
            self.cursor.executemany(sql, registros)
            self.conn.commit()
            print(f"{len(registros)} Registros inseridos com sucesso.")
        except oracledb.Error as e:
            error, = e.args
            print("Erro Oracle:")
            print(f"Code: {error.code}")
            print(f"Message: {error.message}")
            self.conn.rollback()
            raise
    
    def insert_requests_ME5A(self, requisicoes: list,  path: str):
        registros = [
            (
                r.tipo_documento, r.requisicao_compra, r.pedido, r.texto_breve,
                r.material, r.item_reqc, r.qtd_solicitada, r.requisitante,
                r.grupo_compradores, r.data_liberacao, r.categoria_clc, r.codigo_eliminacao, r.data_pedido, r.item_do_pedido
            )
            for r in requisicoes     
        ] 
        insert_sql = InsertService()
        insert_sql.insert_data_sql(registros, path) 
        
        
         
    def insert_requests_MB51(self, requisicoes: list, path: str):
        registros = [
            (
                r.material, r.texto_breve, r.deposito, r.tipo_movimento,
                r.doc_material, r.data_lancamento, r.qtd_um_registro, r.um_registro,
                r.centro_custo, r.montante_em_mi
            )
            for r in requisicoes
            
        ] 
        insert_sql = InsertService()
        insert_sql.insert_data_sql(registros, path)
         
    def insert_requests_ZMM001(self, requisicoes: list, path: str):
        registros = [
            (
                r.tmat, r.material, r.n_material, r.n_material_antigo,
                r.pos_dpst, r.utiliz_livre, r.umb
            )
            for r in requisicoes
        ] 
        insert_sql = InsertService()
        insert_sql.insert_data_sql(registros, path)
    
    def insert_requests_ZMM018(self, requisicoes: list, path: str):
        registros = [
            (
                r.grupo_de_compradores, r.tipo_documento_compras, r.centro_custo, r.desc_centro_custo, r.material, r.num_acompanhamento, 
                r.denominacao, r.doc_compras, r.requisicao_compra, r.item, r.texto_breve, r.qtd_pedido, r.um_pedido, r.preco_liq_pedido,
                r.moeda, r.valor_liquido, r.data_criacao, r.denom_grupo_mercadorias, r.fornecedor, r.nome_empresa
            )
            for r in requisicoes
        ]
        insert_sql = InsertService()
        insert_sql.insert_data_sql(registros, path)
