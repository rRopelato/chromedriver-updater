import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

file_name = "chromedriver-win64.zip"
file_path = os.path.join(os.path.expanduser("~"), "Downloads", file_name)

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Arquivo {file_name} existente removido.")

driver = webdriver.Chrome()
driver.get("https://googlechromelabs.github.io/chrome-for-testing/#stable")

xpath = "/html/body/section[1]/div[1]/table/tbody/tr[10]/td[1]"

element_with_link = driver.find_element("xpath", xpath)

link_text = element_with_link.text

driver.execute_script("window.open('about:blank', '_blank');")

driver.switch_to.window(driver.window_handles[1])

driver.get(link_text)

timeout = 5

try:
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, f"//a[text()='{file_name}']"))
    )
    print("Download concluído.")
except TimeoutError:
    print("Tempo de espera excedido. O download pode não ter sido concluído.")


driver.close()
