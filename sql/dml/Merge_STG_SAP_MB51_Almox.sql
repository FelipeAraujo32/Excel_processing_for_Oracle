MERGE INTO SAP_MB51_ALMOX dst
USING STG_SAP_MB51 src
ON (
    dst."material" = src."material" AND
    dst."tipo_movimento" = src."tipo_movimento" AND
    dst."doc_material" = src."doc_material" AND
    dst."data_lancamento" = src."data_lancamento" AND
    dst."qtd_um_registro" = src."qtd_um_registro" AND
    dst."montante_em_mi" = src."montante_em_mi"
)
WHEN MATCHED THEN
    UPDATE SET
        dst."texto_breve_material" = src."texto_breve_material",
        dst."deposito" = src."deposito",
        dst."um_registro" = src."um_registro",
        dst."centro_custo" = src."centro_custo"
WHEN NOT MATCHED THEN
    INSERT (
        "material",
        "texto_breve_material",
        "deposito",
        "tipo_movimento",
        "doc_material",
        "data_lancamento",
        "qtd_um_registro",
        "um_registro",
        "centro_custo",
        "montante_em_mi"
    )
    VALUES (
        src."material",
        src."texto_breve_material",
        src."deposito",
        src."tipo_movimento",
        src."doc_material",
        src."data_lancamento",
        src."qtd_um_registro",
        src."um_registro",
        src."centro_custo",
        src."montante_em_mi"
    )