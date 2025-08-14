MERGE INTO SAP_ZMM018_GERAL tgt
USING STG_SAP_ZMM018 src
ON (
    tgt.DOC_COMPRAS = src.DOC_COMPRAS
    AND tgt.ITEM = src.ITEM
    AND tgt.REQUISICAO_COMPRA = src.REQUISICAO_COMPRA
)
WHEN MATCHED THEN
    UPDATE SET
        tgt.GRUPO_COMPRADORES     = src.GRUPO_COMPRADORES,
        tgt.TP_DOC_COMPRAS        = src.TP_DOC_COMPRAS,
        tgt.CENTRO_CUSTO             = src.CENTRO_CUSTO,
        tgt.DESC_CENTRO_CUSTO        = src.DESC_CENTRO_CUSTO,
        tgt.MATERIAL                 = src.MATERIAL,
        tgt.NUM_ACOMPANHAMENTO       = src.NUM_ACOMPANHAMENTO,
        tgt.DENOMINACAO              = src.DENOMINACAO,
        tgt.TEXTO_BREVE              = src.TEXTO_BREVE,
        tgt.QTD_PEDIDO               = src.QTD_PEDIDO,
        tgt.UM_PEDIDO                = src.UM_PEDIDO,
        tgt.PRECO_LIQ_PEDIDO         = src.PRECO_LIQ_PEDIDO,
        tgt.MOEDA                    = src.MOEDA,
        tgt.VALOR_LIQUIDO            = src.VALOR_LIQUIDO,
        tgt.DATA_CRIACAO             = src.DATA_CRIACAO,
        tgt.DENOM_GRUPO_MERC         = src.DENOM_GRUPO_MERC,
        tgt.FORNECEDOR               = src.FORNECEDOR,
        tgt.NOME_EMPRESA             = src.NOME_EMPRESA

WHEN NOT MATCHED THEN
    INSERT (
        GRUPO_COMPRADORES,
        TP_DOC_COMPRAS,
        CENTRO_CUSTO,
        DESC_CENTRO_CUSTO,
        MATERIAL,
        NUM_ACOMPANHAMENTO,
        DENOMINACAO,
        DOC_COMPRAS,
        REQUISICAO_COMPRA,
        ITEM,
        TEXTO_BREVE,
        QTD_PEDIDO,
        UM_PEDIDO,
        PRECO_LIQ_PEDIDO,
        MOEDA,
        VALOR_LIQUIDO,
        DATA_CRIACAO,
        DENOM_GRUPO_MERC,
        FORNECEDOR,
        NOME_EMPRESA
    )
    VALUES (
        src.GRUPO_COMPRADORES,
        src.TP_DOC_COMPRAS,
        src.CENTRO_CUSTO,
        src.DESC_CENTRO_CUSTO,
        src.MATERIAL,
        src.NUM_ACOMPANHAMENTO,
        src.DENOMINACAO,
        src.DOC_COMPRAS,
        src.REQUISICAO_COMPRA,
        src.ITEM,
        src.TEXTO_BREVE,
        src.QTD_PEDIDO,
        src.UM_PEDIDO,
        src.PRECO_LIQ_PEDIDO,
        src.MOEDA,
        src.VALOR_LIQUIDO,
        src.DATA_CRIACAO,
        src.DENOM_GRUPO_MERC,
        src.FORNECEDOR,
        src.NOME_EMPRESA
    )
