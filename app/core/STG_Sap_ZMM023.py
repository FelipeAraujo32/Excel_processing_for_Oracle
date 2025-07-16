from dataclasses import dataclass
from typing import Optional   # permite None

@dataclass
class STG_Sap_ZMM023:
    nome_da_firma: Optional[str] = None
    grupo_de_compradores: Optional[str] = None
    tipo_documento_compras: Optional[str] = None
    documento_compras: Optional[str] = None
    item: Optional[str] = None
    material: Optional[str] = None
    texto_breve: Optional[str] = None
    grupo_mercadorias: Optional[str] = None
    denom_grupo_mercadorias: Optional[str] = None
    qtd_pedido: Optional[str] = None
    um_pedido: Optional[str] = None
    requisicao_compra: Optional[str] = None
    item_requisicao: Optional[str] = None
    num_acompanhamento: Optional[str] = None
    preco_liq_pedido: Optional[str] = None
    moeda: Optional[str] = None
    valor_liquido_pedido: Optional[str] = None
    cambio_pedido_reais: Optional[str] = None
    fornecedor: Optional[str] = None
    nome_fornecedor: Optional[str] = None
    data_criacao: Optional[str] = None
    data_solicitacao: Optional[str] = None
    data_lancamento: Optional[str] = None
    tipo_fornecedor: Optional[str] = None
    orcamento: Optional[str] = None
    centro_custo: Optional[str] = None
    aplicacao: Optional[str] = None     
