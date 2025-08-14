from app.services.insertservice import InsertService
from app.services.truncateservice import TrucateService
from app.services.mergeservice import MergeService
from app.services.processor_excel import process_excel_file_STG_Sap_ME5A, process_excel_file_STG_Sap_MB51, process_excel_file_STG_Sap_ZMM001, process_excel_file_STG_Sap_ZMM018
from app.services.viewserive import ViewService

class PipeLine_Steps:

    # Function to insert data into the temporary table
    def run_insert_data_ME5A(self, excel_path, sql_path):
        repository_sql = InsertService()
        requisicoes = process_excel_file_STG_Sap_ME5A(excel_path)
        repository_sql.insert_requests_ME5A(requisicoes, sql_path)
        
    def run_insert_data_MB51(self, excel_path, sql_path):
        repository_sql = InsertService()
        requisicoes = process_excel_file_STG_Sap_MB51(excel_path)
        repository_sql.insert_requests_MB51(requisicoes,sql_path)
        
    def run_insert_data_ZMM001(self, excel_path, sql_path):
        repository_sql = InsertService()
        requisicoes = process_excel_file_STG_Sap_ZMM001(excel_path)
        repository_sql.insert_requests_ZMM001(requisicoes, sql_path)
        
    def run_insert_data_ZMM018(self, excel_path, sql_path):
        repository_sql = InsertService()
        requisicoes = process_excel_file_STG_Sap_ZMM018(excel_path)
        repository_sql.insert_requests_ZMM018(requisicoes, sql_path)
        
        
    # Function to perform the MERGE for the final table
    def run_merge_data(self, path: str):
        repository_sql = MergeService()
        repository_sql.merge_sql(path)
        
        
    def run_truncate_table(self, path: str):
        trucate_sql =  TrucateService()
        trucate_sql.clear_staging_table(path)
        
    def run_view_table(self, path: str):
        viwe_sql =  ViewService()
        viwe_sql.view_update_table(path)