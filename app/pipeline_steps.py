from app.services.insertservice import InsertService
from app.services.truncateservice import TrucateService
from app.services.mergeservice import MergeService
from app.services.processor_excel import process_excel_file_STG_Sap_ME5A, process_excel_file_STG_Sap_MB51, process_excel_file_STG_Sap_ZMM001, process_excel_file_STG_Sap_ZMM018


# Function to insert data into the temporary table
def run_insert_data_ME5A(excel_path):
    repository_sql = InsertService()
    requisicoes = process_excel_file_STG_Sap_ME5A(excel_path)
    repository_sql.insert_requests_ME5A(requisicoes)
    
def run_insert_data_MB51(excel_path):
    repository_sql = InsertService()
    requisicoes = process_excel_file_STG_Sap_MB51(excel_path)
    repository_sql.insert_requests_MB51(requisicoes)
    
def run_insert_data_ZMM001(excel_path):
    repository_sql = InsertService()
    requisicoes = process_excel_file_STG_Sap_ZMM001(excel_path)
    repository_sql.insert_requests_ZMM001(requisicoes)
    
def run_insert_data_ZMM018(excel_path):
    repository_sql = InsertService()
    requisicoes = process_excel_file_STG_Sap_ZMM018(excel_path)
    repository_sql.insert_requests_ZMM018(requisicoes)
    
    
# Function to perform the MERGE for the final table
def run_merge_data(path: str):
    repository_sql = MergeService()
    repository_sql.merge_sql(path)
    
    
def run_truncate_table(path: str):
    trucate_sql =  TrucateService()
    trucate_sql.clear_staging_table(path)