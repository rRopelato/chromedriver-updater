import os
import zipfile
import time
import shutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

current_datetime = datetime.now()

datetime_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

log_file_path = os.path.join(os.path.expanduser("~"), "Downloads", f"script_log_{datetime_str}.txt")

def log_and_print(message):
    print(message)
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")

file_to_delete = os.path.join(os.path.expanduser("~"), "Downloads", "chromedriver-win64.zip")

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    log_and_print(f"Arquivo {file_to_delete} excluído.")
else:
    log_and_print("O arquivo não existe. Nenhuma exclusão necessária.")

driver = webdriver.Chrome()
driver.get("https://googlechromelabs.github.io/chrome-for-testing/#stable")

xpath = "/html/body/section[1]/div[1]/table/tbody/tr[10]/td[1]"

element_with_link = driver.find_element("xpath", xpath)

link_text = element_with_link.text

driver.execute_script("window.open('about:blank', '_blank');")

driver.switch_to.window(driver.window_handles[1])

driver.get(link_text)

max_wait_time = 300

start_time = time.time()

while time.time() - start_time < max_wait_time:
    file_path = os.path.join(os.path.expanduser("~"), "Downloads", "chromedriver-win64.zip")
    
    if os.path.exists(file_path):
        log_and_print("O download foi concluído.")
        break
    else:
        log_and_print("Aguardando o download...")
        time.sleep(1)

else:
    log_and_print("O download não foi concluído dentro do tempo máximo.")

zip_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "chromedriver-win64.zip")

extracted_folder_path = os.path.join(os.path.expanduser("~"), "Downloads", "chromedriver-win64")

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

log_and_print(f"Arquivo {zip_file_path} extraído para {extracted_folder_path}.")

selenium_basic_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "SeleniumBasic")
files_to_delete = ["chromedriver.exe", "LICENSE.chromedriver"]

for file_name in files_to_delete:
    file_path = os.path.join(selenium_basic_path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        log_and_print(f"Arquivo {file_name} excluído em {selenium_basic_path}.")
    else:
        log_and_print(f"O arquivo {file_name} não existe em {selenium_basic_path}. Nenhuma exclusão necessária.")

extracted_folder_path = os.path.join(os.path.expanduser("~"), "Downloads", "chromedriver-win64", "chromedriver-win64")

destination_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "SeleniumBasic")

shutil.copytree(extracted_folder_path, destination_path, dirs_exist_ok=True)
log_and_print(f"Arquivos copiados de {extracted_folder_path} para {destination_path}.")

folder_to_delete = os.path.join(os.path.expanduser("~"), "Downloads", "chromedriver-win64")

zip_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "chromedriver-win64.zip")

if os.path.exists(folder_to_delete):
    shutil.rmtree(folder_to_delete)
    log_and_print(f"Pasta {folder_to_delete} excluída.")
else:
    log_and_print(f"A pasta {folder_to_delete} não existe. Nenhuma exclusão necessária.")

if os.path.exists(zip_file_path):
    os.remove(zip_file_path)
    log_and_print(f"Arquivo {zip_file_path} excluído.")
else:
    log_and_print(f"O arquivo {zip_file_path} não existe. Nenhuma exclusão necessária.")

with open(log_file_path, "a") as log_file:
    log_file.write("Script concluído.")

log_and_print(f"Processo totalmente encerrado.")

driver.quit()