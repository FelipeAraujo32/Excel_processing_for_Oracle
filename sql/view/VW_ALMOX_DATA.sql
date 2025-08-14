CREATE OR REPLACE VIEW "VW_ALMOX_DATA" (
    "material", 
    "texto_breve_material", 
    "um_registro", 
    "centro_custo", 
    "montante_em_mi", 
    "data_lancamento", 
    "qtd_um_registro"
) AS 
SELECT
    e."material",
    INITCAP(UPPER(e."texto_breve_material")) AS "texto_breve_material",
    e."um_registro",
    e."centro_custo",
    e."montante_em_mi",
    e."data_lancamento",
    e."qtd_um_registro"
FROM 
    SAP_MB51_ALMOX e
INNER JOIN
    SAP_ZMM001_ALMOX m
    ON e."material" = m."material"
