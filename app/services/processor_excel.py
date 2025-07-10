import pandas as pd
import locale
from app.core.STG_Sap_ME5A import STG_Sap_ME5A
from app.core.STG_Sap_MB51 import STG_Sap_MB51
from app.core.STG_Sap_ZMM001 import STG_Sap_ZMM001

def process_excel_file_STG_Sap_ME5A(caminho: str) -> list[STG_Sap_ME5A]:
    df = pd.read_excel(caminho)

    print("Columns found:", df.columns.tolist())
    
    requisicoes = []

    for _, row in df.iterrows():
        requisicao = STG_Sap_ME5A(
            tipo_documento=row['Tipo de documento'] if pd.notna(row['Tipo de documento']) else None,
            requisicao_compra=row['Requisição de compra'] if pd.notna(row['Requisição de compra']) else None,
            pedido=row['Pedido'] if pd.notna(row['Pedido']) else None,
            texto_breve=row['Texto breve'].upper() if pd.notna(row['Texto breve']) else None,
            material=row['Material'] if pd.notna(row['Material']) else None,
            item_reqc=row['Item ReqC'] if pd.notna(row['Item ReqC']) else None,
            qtd_solicitada=row['Qtd.solicitada'] if pd.notna(row['Qtd.solicitada']) else None,
            requisitante=row['Requisitante'].capitalize() if pd.notna(row['Requisitante']) else None,
            grupo_compradores=row['Grupo de compradores'] if pd.notna(row['Grupo de compradores']) else None,
            data_liberacao = row['Data da liberação'].strftime('%d/%m/%Y') if pd.notna(row['Data da liberação']) else None,
            codigo_eliminacao=str(row['Código de eliminação']) if pd.notna(row['Código de eliminação']) else None,
            data_pedido = row['Data do pedido'].strftime('%d/%m/%Y') if pd.notna(row['Data do pedido']) else None,
            categoria_clc=row['Categoria ClC'] if pd.notna(row['Categoria ClC']) else None
        )
        requisicoes.append(requisicao)

    return requisicoes

locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

def process_excel_file_STG_Sap_MB51(caminho: str) -> list[STG_Sap_MB51]:
    df = pd.read_excel(caminho)

    print("Columns found:", df.columns.tolist())
    
    requisicoes = []

    for _, row in df.iterrows():
        requisicao = STG_Sap_MB51(
            material=row['Material'] if pd.notna(row['Material']) else None,
            texto_breve=row['Texto breve de material'].strip('*').upper() if pd.notna(row['Texto breve de material']) else None,
            deposito=row['Depósito'] if pd.notna(row['Depósito']) else None,
            tipo_movimento=row['Tipo de movimento'] if pd.notna(row['Tipo de movimento']) else None,
            doc_material=row['Doc.material'] if pd.notna(row['Doc.material']) else None,
            data_lancamento=row['Data de lançamento'].strftime('%d/%m/%Y') if pd.notna(row['Data de lançamento']) else None,
            qtd_um_registro = row['Qtd.  UM registro'] if pd.notna(row['Qtd.  UM registro']) else None,
            um_registro=row['UM registro'] if pd.notna(row['UM registro']) else None,
            centro_custo = row['Centro custo'] if pd.notna(row['Centro custo']) else None,
            montante_em_mi = locale.format_string('%.2f', row['Montante em MI'], grouping=True) if pd.notna(row['Montante em MI']) else None
        )
        requisicoes.append(requisicao)

    return requisicoes

def process_excel_file_STG_Sap_ZMM001(caminho: str) -> list[STG_Sap_ZMM001]:
    df = pd.read_excel(caminho)

    print("Columns found:", df.columns.tolist())
    
    requisicoes = []

    for _, row in df.iterrows():
        requisicao = STG_Sap_ZMM001(
            material=row['Material'] if pd.notna(row['Material']) else None,
            tmat=row['TMat'].upper() if pd.notna(row['TMat']) else None,
            n_material = row['Nº do material'].strip('*').capitalize() if pd.notna(row['Nº do material']) else None,
            n_material_antigo=row['Nº material antigo'] if pd.notna(row['Nº material antigo']) else None,
            pos_dpst=row['Pos.dpst.'].upper() if pd.notna(row['Pos.dpst.']) else None,
            utiliz_livre=row['Utiliz.livre'] if pd.notna(row['Utiliz.livre']) else None,
            umb=row['UMB'].upper() if pd.notna(row['UMB']) else None,
        )
        requisicoes.append(requisicao)

    return requisicoes

