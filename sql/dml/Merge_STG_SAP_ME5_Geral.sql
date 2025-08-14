-- ==========================================================
-- Script: Merge - Update or Insert into sap_me5a
-- Description: Synchronizes purchase requisition data from staging (stg_sap_me5a) into the target table (sap_me5a).
-- Author: [Felipe Araújo GitHub: https://github.com/FelipeAraujo32]
-- Date: 2025-04-17
-- ==========================================================

MERGE INTO sap_me5a_geral d
USING (
    SELECT *
    FROM STG_SAP_ME5A
    WHERE "Código de eliminação" = 'False'
) s
ON (
    d.requisicao_compra = s."Requisição de compra"
    AND d.item_reqc = s."Item reqC"
)
WHEN MATCHED THEN
    UPDATE SET 
        d.pedido = s."Pedido",
        d.texto_breve = s."Texto breve",
        d.material = s."Material",
        d.qtd_solicitada = s."qtd.solicitada",
        d.requisitante = s."Requisitante",
        d.grupo_compradores = s."Grupo de compradores",
        d.modificado_em = s."Data da liberação",
        d.categoria_cic = s."Categoria ClC",
        d.tipo_documento = s."Tipo de documento",
        d.codigo_eliminação = s."Código de eliminação",
        d.data_pedido = s."Data do pedido",
        d.item = s."ITEM"
WHEN NOT MATCHED THEN
    INSERT (
        tipo_documento,
        requisicao_compra,
        pedido,
        texto_breve,
        material,
        item_reqc,
        qtd_solicitada,
        requisitante,
        grupo_compradores,
        modificado_em,
        categoria_cic,
        codigo_eliminação,
        data_pedido,
        item
    )
    VALUES (
        s."Tipo de documento",
        s."Requisição de compra",
        s."Pedido",
        s."Texto breve",
        s."Material",
        s."Item reqC",
        s."qtd.solicitada",
        s."Requisitante",
        s."Grupo de compradores",
        s."Data da liberação",
        s."Categoria ClC",
        s."Código de eliminação",
        s."Data do pedido",
        s."ITEM"

)






