import time
from .pipeline_steps import run_truncate_table, run_insert_data_ME5A, run_merge_data, run_insert_data_MB51, run_insert_data_ZMM001, run_insert_data_ZMM023


def run_me5a_BI(excel_path_bi):
    start_time = time.time()

    run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")
    run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A_Compradores_BI.sql")
    run_insert_data_ME5A(excel_path_bi)
    run_merge_data("sql/dml/Merge_STG_SAP_ME5_Comprador_BI.sql")
    run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")

    elapsed = time.time() - start_time
    print(f"Concluído em {elapsed:.2f} segundos.")
    
def run_me5a_App_Geral(excel_path_app):
    start_time = time.time()

    run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")
    run_insert_data_ME5A(excel_path_app)
    run_merge_data("sql/dml/Merge_STG_SAP_ME5_Comprador_App.sql")
    run_merge_data("sql/dml/Merge_STG_SAP_ME5_Geral.sql")
    run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")

    elapsed = time.time() - start_time
    print(f"Concluído em {elapsed:.2f} segundos.")
    
def run_mb51_almox(excel_path_mb51_almox):
    run_truncate_table("sql/util/Stg_Truncate_Sap_MB51_Almox.sql")
    run_insert_data_MB51(excel_path_mb51_almox)
    run_merge_data("sql/dml/Merge_STG_SAP_MB51_Almox.sql")
    run_truncate_table("sql/util/Stg_Truncate_Sap_MB51_Almox.sql")
    
def run_zmm001_almox(excel_path_zmm001_almox):
    run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM001_Almox.sql")
    run_insert_data_ZMM001(excel_path_zmm001_almox)
    run_merge_data("sql/dml/Merge_STG_SAP_ZMM001_Almox.sql")
    run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM001_Almox.sql")
    
def run_zmm023_Geral(excel_path_zmmm023_Geral):
    run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM023.sql")
    run_insert_data_ZMM023(excel_path_zmmm023_Geral)
    run_merge_data("sql/dml/Merge_STG_SAP_ZMM023.sql")
    run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM023.sql")