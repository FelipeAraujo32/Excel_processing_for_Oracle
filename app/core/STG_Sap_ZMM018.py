from dataclasses import dataclass
from typing import Optional   # permite None

@dataclass
class STG_Sap_ZMM018:
    grupo_de_compradores: Optional[str] = None
    tipo_documento_compras: Optional[str] = None
    centro_custo: Optional[str] = None
    desc_centro_custo: Optional[str] = None
    material: Optional[str] = None
    num_acompanhamento: Optional[str] = None
    denominacao: Optional[str] = None
    doc_compras: Optional[str] = None
    requisicao_compra: Optional[str] = None
    material: Optional[str] = None
    item: Optional[str] = None
    texto_breve: Optional[str] = None
    qtd_pedido: Optional[str] = None
    um_pedido: Optional[str] = None
    preco_liq_pedido: Optional[str] = None
    moeda: Optional[str] = None
    valor_liquido: Optional[str] = None
    data_criacao: Optional[str] = None
    denom_grupo_mercadorias: Optional[str] = None
    fornecedor: Optional[str] = None
    nome_empresa: Optional[str] = None
