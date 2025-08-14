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

    
    def insert_requests_ME5A(self, requisicoes: list):
        registros = [
            (
                r.tipo_documento, r.requisicao_compra, r.pedido, r.texto_breve,
                r.material, r.item_reqc, r.qtd_solicitada, r.requisitante,
                r.grupo_compradores, r.data_liberacao, r.categoria_clc, r.codigo_eliminacao, r.data_pedido, r.item_do_pedido
            )
            for r in requisicoes
            
        ] 
        sql_insert ="""
            INSERT INTO STG_SAP_ME5A ("Tipo de documento", "Requisição de compra", "Pedido", "Texto breve", "Material", "Item reqC", "qtd.solicitada", "Requisitante", "Grupo de compradores", "Data da liberação", "Categoria ClC",  "Código de eliminação", "Data do pedido", "ITEM") 
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)
            """
        try:
            self.cursor.executemany(sql_insert, registros)
            self.conn.commit()
            print(f"{len(registros)} registros inseridos com sucesso na STG_SAP_ME5A.")
        except oracledb.Error as e:
            error, = e.args
            print("Erro Oracle:")
            print(f"Code: {error.code}")
            print(f"Message: {error.message}")
            self.conn.rollback()
            raise
         
    def insert_requests_MB51(self, requisicoes: list):
        registros = [
            (
                r.material, r.texto_breve, r.deposito, r.tipo_movimento,
                r.doc_material, r.data_lancamento, r.qtd_um_registro, r.um_registro,
                r.centro_custo, r.montante_em_mi
            )
            for r in requisicoes
            
        ] 
        sql_insert ="""
            INSERT INTO STG_SAP_MB51 ("material", "texto_breve_material", "deposito", "tipo_movimento", "doc_material", "data_lancamento", "qtd_um_registro", "um_registro", "centro_custo", "montante_em_mi") 
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)
            """
        try:
            self.cursor.executemany(sql_insert, registros)
            self.conn.commit()
            print(f"{len(registros)} registros inseridos com sucesso na STG_SAP_MB51.")
        except oracledb.Error as e:
            error, = e.args
            print("Erro Oracle:")
            print(f"Code: {error.code}")
            print(f"Message: {error.message}")
            self.conn.rollback()
            raise
         
    def insert_requests_ZMM001(self, requisicoes: list):
        registros = [
            (
                r.tmat, r.material, r.n_material, r.n_material_antigo,
                r.pos_dpst, r.utiliz_livre, r.umb
            )
            for r in requisicoes
            
        ] 
        sql_insert ="""
            INSERT INTO STG_SAP_ZMM001 ("tmat", "material", "n_material", "n_material_antigo", "pos_dpst", "utiliz_livre", "umb") 
            VALUES (:1, :2, :3, :4, :5, :6, :7)
            """
        try:
            self.cursor.executemany(sql_insert, registros)
            self.conn.commit()
            print(f"{len(registros)} registros inseridos com sucesso na STG_SAP_ZM001.")
        except oracledb.Error as e:
            error, = e.args
            print("Erro Oracle:")
            print(f"Code: {error.code}")
            print(f"Message: {error.message}")
            self.conn.rollback()
            raise
    
    def insert_requests_ZMM018(self, requisicoes: list):
        registros = [
            (
                r.grupo_de_compradores, r.tipo_documento_compras, r.centro_custo, r.desc_centro_custo, r.material, r.num_acompanhamento, 
                r.denominacao, r.doc_compras, r.requisicao_compra, r.item, r.texto_breve, r.qtd_pedido, r.um_pedido, r.preco_liq_pedido,
                r.moeda, r.valor_liquido, r.data_criacao, r.denom_grupo_mercadorias, r.fornecedor, r.nome_empresa
            )
            for r in requisicoes
    ]

        sql_insert = """
            INSERT INTO STG_SAP_ZMM018 (
                GRUPO_COMPRADORES, TP_DOC_COMPRAS, CENTRO_CUSTO, DESC_CENTRO_CUSTO,
                MATERIAL, NUM_ACOMPANHAMENTO, DENOMINACAO, DOC_COMPRAS, REQUISICAO_COMPRA,
                ITEM, TEXTO_BREVE, QTD_PEDIDO, UM_PEDIDO, PRECO_LIQ_PEDIDO, MOEDA,
                VALOR_LIQUIDO, DATA_CRIACAO, DENOM_GRUPO_MERC, FORNECEDOR, NOME_EMPRESA
            ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9, :10,
                :11, :12, :13, :14, :15, :16, :17, :18, :19, :20
            )
        """

        try:
            self.cursor.executemany(sql_insert, registros)
            self.conn.commit()
            print(f"{len(registros)} registros inseridos com sucesso na STG_SAP_ZMM018.")
        except oracledb.Error as e:
            error, = e.args
            print("Erro Oracle:")
            print(f"Code: {error.code}")
            print(f"Message: {error.message}")
            self.conn.rollback()
            raise
