from dataclasses import dataclass


@dataclass
class STG_Sap_ME5A:
    tipo_documento: str
    requisicao_compra: str
    pedido: str
    texto_breve: str
    material: str
    item_reqc: str
    qtd_solicitada: str
    requisitante: str
    grupo_compradores: str
    categoria_clc: str
    data_liberacao: str
    codigo_eliminacao: str
    data_pedido: str