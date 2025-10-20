from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys   
import time


def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    # option.add_argument("--headless")  # Ejecutar en modo headless
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("http://rmcab.ambientebogota.gov.co/Report/stationreport")
    #Exel
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[1]/ul[1]/li[3]").click()
    
    ## Anual
    #driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[1]/ul[2]/li[5]").click()
    ## Perzonalizado
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[1]/ul[2]/li[6]").click()

    # Air Quality
    wait = WebDriverWait(driver, 20)

    #1 localizar y hacer clic en el dropdown para abrirlo
    dropdown = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//span[contains(@class, 'k-widget') and contains(@class, 'k-dropdown') and @aria-labelledby='Purpose_label']")))

    dropdown.click()

    #time.sleep(3) 

    #2 mover dos veces hacia abajo y luego Enter
    dropdown.send_keys(Keys.ARROW_DOWN)
    dropdown.send_keys(Keys.ARROW_DOWN)
    dropdown.send_keys(Keys.ENTER)

    time.sleep(3) 


    ## Estaciones con PM10
    n=15
   

    for i in range(1, n+1):  # del 1 al n
     # Click en la estación
     xpath_estacion = f"/html/body/div[2]/div[1]/div[2]/section[1]/div[1]/div[2]/div/div/ul/li[{i}]/div/span[1]"
    
     estacion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_estacion))
     )
     estacion.click()

     time.sleep(1)
     # Click en checkbox PM10
     xpath_checkbox = f"/html/body/div[2]/div[1]/div[2]/section[1]/div[1]/div[2]/div/div/ul/li[{i}]/ul/li[1]/div/span[1]/span"
     
     pm10_checkbox = driver.find_element(By.XPATH, xpath_checkbox)
     
     driver.execute_script("arguments[0].click();", pm10_checkbox)
     
     time.sleep(1)
      
     estacion.click()
     time.sleep(1)


    time.sleep(2)

    # A base de tiempo, 12
    wait = WebDriverWait(driver, 20)

    #1 localizar y hacer clic en el dropdown para abrirlo
    dropdown = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[2]/div[2]/div[3]/span")))

    dropdown.click()
    
    time.sleep(3) 

    #2 mover dos veces hacia abajo y luego Enter
    dropdown.send_keys(Keys.ARROW_DOWN)
    dropdown.send_keys(Keys.ARROW_DOWN)
    dropdown.send_keys(Keys.ARROW_DOWN)
    dropdown.send_keys(Keys.ENTER)
    
    time.sleep(3)


    ##Fechas y importancion
    for i in range (14,25):
     
     ## Fecha de inicio
     start_date_input = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.ID, "startDate"))
     )

      # Seleccionar todo y borrar 


     start_date_input.send_keys(Keys.COMMAND, "a")  # Command + A = seleccionar todo
     start_date_input.send_keys(Keys.DELETE)

     time.sleep(2)
     
     texto_inicial= f"01-01-20{i}"
     driver.find_element(By.ID,"startDate").send_keys(texto_inicial)
     time.sleep(2)

     ## Fecha final

     end_date_input=WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.ID, "endDate"))
     )


     end_date_input.send_keys(Keys.COMMAND, "a")
     end_date_input.send_keys(Keys.DELETE)
     texto_final= f"31-12-20{i}"
     driver.find_element(By.ID,"endDate").send_keys(texto_final)

     time.sleep(2)

     ## Mostrar en Exel
     driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[2]/div[3]/input[2]").click()
     time.sleep(30)

    
    time.sleep(60)




if __name__ == "__main__":
    main()

