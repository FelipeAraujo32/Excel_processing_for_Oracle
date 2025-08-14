CREATE OR REPLACE VIEW VW_ALMOX_MRP AS 
SELECT
    e."material",
    e."utiliz_livre",
    INITCAP(UPPER(e."n_material")) AS "n_material",
    e."umb",
    m."coordenacao",
    m."estoque_minimo",
    m."estoque_maximo",
    m."estoque_seguranca"
FROM 
    SAP_ZMM001_ALMOX e
LEFT JOIN
    CONTROLE_ESTOQUE_MRP m
    ON e."material" = m."material"




