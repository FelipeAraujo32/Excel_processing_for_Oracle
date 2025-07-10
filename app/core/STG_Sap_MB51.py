from dataclasses import dataclass


@dataclass
class STG_Sap_MB51:
    material: str
    texto_breve: str
    deposito: str
    tipo_movimento: str
    doc_material: str
    data_lancamento: str
    qtd_um_registro: str
    um_registro: str
    centro_custo: str
    montante_em_mi: str
    