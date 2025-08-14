from .pipeline_steps import PipeLine_Steps

class PipeLine:

    def run_me5a_BI(self, excel_path_bi):
        step = PipeLine_Steps()
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A_Compradores_BI.sql")
        step.run_insert_data_ME5A(excel_path_bi, "sql/dml/insert/Insert_SAP_ME5A.sql")
        step.run_merge_data("sql/dml/merge/Merge_STG_SAP_ME5_Comprador_BI.sql")
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")
        
    def run_me5a_App_Geral(self, excel_path_app):
        step = PipeLine_Steps()
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")
        step.run_insert_data_ME5A(excel_path_app, "sql/dml/insert/Insert_SAP_ME5A.sql")
        step.run_merge_data("sql/dml/merge/Merge_STG_SAP_ME5_Comprador_App.sql")
        step.run_merge_data("sql/dml/merge/Merge_STG_SAP_ME5_Geral.sql")
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ME5A.sql")
    
    def run_mb51_almox(self, excel_path_mb51_almox):
        step = PipeLine_Steps()
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_MB51_Almox.sql")
        step.run_insert_data_MB51(excel_path_mb51_almox, "sql/dml/insert/Insert_SAP_MB51.sql")
        step.run_merge_data("sql/dml/merge/Merge_STG_SAP_MB51_Almox.sql")
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_MB51_Almox.sql")
    
    def run_zmm001_almox(self, excel_path_zmm001_almox):
        step = PipeLine_Steps()
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM001_Almox.sql")
        step.run_insert_data_ZMM001(excel_path_zmm001_almox, "sql/dml/insert/Insert_SAP_ZMM001.sql")
        step.run_merge_data("sql/dml/merge/Merge_STG_SAP_ZMM001_Almox.sql")
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM001_Almox.sql")
        
    def run_zmm018_Geral(self, excel_path_zmmm023_Geral):
        step = PipeLine_Steps()
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM018.sql")
        step.run_insert_data_ZMM018(excel_path_zmmm023_Geral, "sql/dml/insert/Insert_SAP_ZMM018.sql")
        step.run_merge_data("sql/dml/merge/Merge_STG_SAP_ZMM018.sql")
        step.run_truncate_table("sql/util/Stg_Truncate_Sap_ZMM018.sql")
        
    def run_update_view(self):
        step = PipeLine_Steps()
        step.run_view_table("sql/view/VW_ALMOX_DATA.sql")
        step.run_view_table("sql/view/VW_ALMOX_MRP.sql")
        step.run_view_table("sql/view/VW_ME5A_ALMOX_APP.sql")
        step.run_view_table("sql/view/VW_ME5A_Compradores_APP.sql")
        step.run_view_table("sql/view/VW_ME5A_Compradores_BI.sql")