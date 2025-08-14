CREATE OR REPLACE VIEW "VW_ME5A_ALMOX_APP" (
    "CHAVE_PRIMARIA", 
    "TIPO_DOCUMENTO", 
    "REQUISICAO_COMPRA", 
    "PEDIDO", 
    "ITEM", 
    "TEXTO_BREVE", 
    "MATERIAL", 
    "ITEM_REQC", 
    "QTD_SOLICITADA", 
    "REQUISITANTE", 
    "GRUPO_COMPRADORES", 
    "MODIFICADO_EM", 
    "CATEGORIA_CIC") AS
  SELECT
	chave_primaria,
    tipo_documento,
    requisicao_compra,
    pedido,
    item,
    INITCAP(UPPER(texto_breve)) AS texto_breve,
    material,
    item_reqc,
    qtd_solicitada,
    INITCAP(LOWER(REQUISITANTE)) AS REQUISITANTE,
    grupo_compradores,
    modificado_em,
    categoria_cic
    
FROM 
    sap_me5a_comprador_APP
WHERE
    MATERIAL IS NOT NULL
    AND PEDIDO IS NOT NULL
    AND grupo_compradores IN ('1CL','1CS','1FN','1ML','1CO','1IL', '1FA', '1GA', '100')