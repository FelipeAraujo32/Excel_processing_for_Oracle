MERGE INTO SAP_ZMM001_ALMOX dst
USING STG_SAP_ZMM001 src
ON (dst."material" = src."material") -- Condição de junção entre as duas tabelas
WHEN MATCHED THEN
    UPDATE SET
        dst."tmat" = src."tmat", 
        dst."n_material" = src."n_material",
        dst."n_material_antigo" = src."n_material_antigo",
        dst."pos_dpst" = src."pos_dpst",
        dst."utiliz_livre" = src."utiliz_livre",
        dst."umb" = src."umb"
