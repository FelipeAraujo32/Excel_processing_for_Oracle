import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.pipeline import PipeLine

        
if __name__ == "__main__":
    pipe_run = PipeLine()
    start_time = time.time()
    excel_path_me5a_bi = "c:/Users/fasilva/Documents/SAP/SAP GUI/export_ME5A_BI.xlsx"
    excel_path_me5a_app = "c:/Users/fasilva/Documents/SAP/SAP GUI/export_ME5A_App_Geral.xlsx"
    excel_path_mb51_almox = "c:/Users/fasilva/Documents/SAP/SAP GUI/export_MB51_Almox.xlsx"
    excel_path_zmm001_almox = "c:/Users/fasilva/Documents/SAP/SAP GUI/export_ZMM001_Almox.xlsx" 
    excel_path_zmmm018_Geral = "c:/Users/fasilva/Documents/SAP/SAP GUI/export_ZMM018_Geral.xlsx"
    
    pipe_run.run_me5a_BI(excel_path_me5a_bi)
    pipe_run.run_me5a_App_Geral(excel_path_me5a_app)
    pipe_run.run_mb51_almox(excel_path_mb51_almox)
    pipe_run.run_zmm001_almox(excel_path_zmm001_almox)
    pipe_run.run_zmm018_Geral(excel_path_zmmm018_Geral)
    pipe_run.run_update_view()
    
    elapsed = time.time() - start_time
    print(f"Processado em {elapsed:.2f} segundos.")
    