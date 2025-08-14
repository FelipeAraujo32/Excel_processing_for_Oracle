 INSERT INTO STG_SAP_ZMM018 (
                GRUPO_COMPRADORES, 
                TP_DOC_COMPRAS, CENTRO_CUSTO, 
                DESC_CENTRO_CUSTO,
                MATERIAL, NUM_ACOMPANHAMENTO, 
                DENOMINACAO, DOC_COMPRAS, 
                REQUISICAO_COMPRA,
                ITEM, TEXTO_BREVE, 
                QTD_PEDIDO, UM_PEDIDO, 
                PRECO_LIQ_PEDIDO, MOEDA,
                VALOR_LIQUIDO, 
                DATA_CRIACAO, 
                DENOM_GRUPO_MERC, 
                FORNECEDOR, 
                NOME_EMPRESA
            ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9, :10,
                :11, :12, :13, :14, :15, :16, :17, :18, :19, :20
            )