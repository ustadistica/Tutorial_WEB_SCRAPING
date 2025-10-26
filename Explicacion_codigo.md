# INFORME SOBRE EL SCRIPT DE WEB SCRAPING CON SELENIUM PARA LA DESCARGA DE DATOS DE LA RMCAB

## 1. Introducción

El presente informe describe el funcionamiento de un script desarrollado en Python llamado OAB_Borrador.py para realizar Web Scraping automatizado en la plataforma web de la Red de Monitoreo de Calidad del Aire de Bogotá (RMCAB).
El objetivo del script es descargar series históricas de datos del contaminante PM10 para un conjunto de estaciones, utilizando intervalos personalizados y obteniendo los resultados en formato Excel de manera automática.

Este proceso se realiza utilizando la herramienta Selenium, la cual permite simular acciones humanas dentro de un navegador web, como hacer clic, seleccionar menús, escribir texto y descargar archivos


## 2. Librerías Utilizadas


### Codigo:

    from selenium import webdriver

    from selenium.webdriver import Chrome

    from selenium.webdriver.common.by import By

    from selenium.webdriver.support.ui import Select, WebDriverWait

    from selenium.webdriver.support import expected_conditions as EC

    from webdriver_manager.chrome import ChromeDriverManager

    from selenium.webdriver.chrome.service import Service

    from selenium.webdriver.common.keys import Keys

    import time

### Explicación:

| **Librería / Módulo**                        | **Función dentro del código**                  | **Explicación en lenguaje sencillo**                                                                               |
| -------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `selenium`                                   | Control del navegador                          | Permite automatizar acciones dentro de una página web, como hacer clic, escribir, seleccionar opciones, etc.       |
| `webdriver` (de Selenium)                    | Control principal del navegador                | Permite abrir y manejar el navegador Chrome automáticamente como si fuera un usuario.                              |
| `Chrome` (de `selenium.webdriver`)           | Inicializa la ventana de Chrome                | Es el navegador que se va a controlar y manejar durante la automatización.                                         |
| `By` (de Selenium)                           | Localizar elementos                            | Se utiliza para indicar cómo encontrar elementos en la página (por ID, XPATH, nombre, etc.).                       |
| `Select` (de Selenium)                       | Manejo de menús desplegables tipo `<select>`   | Permite seleccionar opciones dentro de cajas de selección tradicionales.                                           |
| `WebDriverWait`                              | Espera inteligente                             | Sirve para esperar hasta que un elemento esté listo antes de interactuar con él, evitando errores por carga lenta. |
| `expected_conditions (EC)`                   | Condiciones de espera                          | Define qué condición se debe cumplir (por ejemplo, que un botón sea clickeable). Se usa junto con WebDriverWait.   |
| `ChromeDriverManager` (de webdriver_manager) | Administrador del controlador                  | Descarga y configura automáticamente la versión correcta del controlador de Chrome.                                |
| `Service` (de Selenium)                      | Servicio que vincula Selenium con ChromeDriver | Permite ejecutar el driver de Chrome correctamente para conectarlo al navegador.                                   |
| `Keys` (de Selenium)                         | Envío de teclas al navegador                   | Permite usar teclas como ENTER, flechas, borrar, etc., simulando el teclado.                                       |
| `time`                                       | Pausas controladas                             | Permite agregar descansos con `time.sleep()` para esperar cargas o asegurar tiempos de descarga.                   |



## 3. Definición de la Función Principal

### Codigo:

    def main():

### Explicación:

El código se organiza dentro de la función main() para mantener una estructura clara y permitir reusabilidad del script.


## 4. Configuración e Inicio del Navegador

En esta sección del código se prepara y lanza el navegador que usaremos para realizar el web scraping. Para ello, utilizamos Selenium junto con Google Chrome.

### Codigo:

    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")  #Ejecutar en modo headless
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("http://rmcab.ambientebogota.gov.co/Report/stationreport")

### Explicación:

| **Línea de código**                                  | **Explicación detallada**                                                                                                                                                     |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `option = webdriver.ChromeOptions()`                 | Crea un objeto de configuración para el navegador. Aquí definimos cómo queremos que se abra Chrome (por ejemplo, tamaño, modo sin ventana, permisos, etc.).                                      |
| `# option.add_argument("--headless")`                | Esta línea está comentada. Si se activara, abriría el navegador en **modo invisible** (sin mostrar ventana). Se usa cuando no necesitamos ver lo que ocurre, útil para automatizar sin interfaz. |
| `option.add_argument("--window-size=1920,1080")`     | Indica el **tamaño de la ventana del navegador**. Se usa un tamaño grande para que todos los menús y botones estén visibles y así Selenium pueda detectarlos correctamente.                      |
| `service = Service(ChromeDriverManager().install())` | Descarga y configura automáticamente el **ChromeDriver**, que es el puente que permite a Selenium controlar el navegador Chrome. Sin esto, no podríamos automatizar el navegador.                |
| `driver = Chrome(service=service, options=option)`   | **Inicia el navegador Chrome** con las configuraciones definidas. `driver` será la variable con la que controlaremos el navegador (hacer clic, escribir, navegar, etc.).                         |
| `driver.get("http://rmcab.ambientebogota.gov.co/Report/stationreport")` | Abre la URL(pagina web) donde se encuentra el reporte de estaciones de calidad del aire. |



## 5. Selección del Formato de Descarga y Tipo de Reporte

### Codigo:

    #Exel

    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[1]/ul[1]/li[3]").click()
    

    #Perzonalizado
    
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[1]/ul[2]/li[6]").click()


### Explicación:

Aquí se indica:

Que los resultados serán descargados en formato Excel.

Que se trabajará con un periodo personalizado, permitiendo definir rangos de fechas.

Esto utilizando el "By.XPATH", nos indica que por el XPATH dado en las comillas del codigo, la pagina se ubicara y hara click a el boton, asi presiona el boton seleccionado, con el .click() del codigo.


## 6. Selección del Tipo de Información: Calidad del Aire

En esta sección del código, lo que se está haciendo es indicarle a la página qué tipo de información queremos consultar, específicamente que queremos trabajar con Calidad del Aire, y no con otros reportes que también ofrece la plataforma.

La página contiene un menú desplegable (dropdown) donde el usuario puede elegir qué tipo de reporte quiere visualizar.
Pero como estamos automatizando el proceso, el programa debe:

Localizar ese menú

Abrirlo

Seleccionar la opción correcta (Calidad del Aire)

### Codigo:


    #Air Quality

    wait = WebDriverWait(driver, 20)

    #1. localizar y hacer clic en el dropdown para abrirlo

    dropdown = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//span[contains(@class, 'k-widget') and contains(@class, 'k-dropdown') and @aria-labelledby='Purpose_label']")))

    dropdown.click()

    #2. mover dos veces hacia abajo y luego Enter

    dropdown.send_keys(Keys.ARROW_DOWN)

    dropdown.send_keys(Keys.ARROW_DOWN)

    dropdown.send_keys(Keys.ENTER)


### Explicación:


| Línea de Código                               | ¿Qué Hace?                   | Explicación en Palabras Simples                                                                                                                  |
| --------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `wait = WebDriverWait(driver, 20)`            | Crea un "esperador"          | La página puede tardar en cargar. Esta línea asegura que el programa **espere hasta 20 segundos** a que aparezcan los elementos antes de fallar. |
| `wait.until(EC.element_to_be_clickable(...))` | Busca el menú desplegable    | Le dice al programa: “**Espera hasta que el menú esté listo para hacer clic**”.                                                                  |
| `dropdown.click()`                            | Abre el menú desplegable     | Es como cuando tú haces clic para desplegar una lista de opciones.                                                                               |
| `dropdown.send_keys(Keys.ARROW_DOWN)`         | Baja una posición en el menú | Equivale a presionar la flecha ↓ del teclado.                                                                                                    |
| `dropdown.send_keys(Keys.ENTER)`              | Selecciona la opción         | Confirma la elección, igual que cuando presionas **Enter**.                                                                                      |


## 7. Selección de Estaciones y Contaminante PM10

En esta parte del programa, se recorre estación por estación, se despliega su lista de contaminantes y se marca el contaminante PM10 para incluirlo en el reporte.

### Código:

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

   



### Explicación:


| **Línea de Código**                                                                                  | **Explicación Detallada**                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `n = 15`                                                                                             | Define que hay **15 estaciones** que se van a recorrer. Este número puede cambiar si hay más o menos estaciones.                                                                |
| `for i in range(1, n+1):`                                                                            | Se crea un ciclo que irá desde 1 hasta 15, procesando una estación por cada iteración.                                                                                          |
| `xpath_estacion = f"...li[{i}]/div/span[1]"`                                                         | Se construye dinámicamente la ruta XPATH que identifica el **nombre de la estación** correspondiente a cada valor de `i`.                                                       |
| `estacion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_estacion)))` | Espera hasta que la estación sea clickeable. Esto evita errores si la página está aún cargando.                                                                                 |
| `estacion.click()`                                                                                   | Hace clic sobre la estación para desplegar la lista de contaminantes disponibles.                                                                                               |
| `time.sleep(1)`                                                                                      | Espera 1 segundo para asegurar que la lista desplegada aparezca correctamente.                                                                                                  |
| `xpath_checkbox = f"...li[{i}]/ul/li[1]/div/span[1]/span"`                                           | Construye la ruta XPATH que apunta específicamente al **checkbox de PM10** dentro de la estación seleccionada.                                                                  |
| `pm10_checkbox = driver.find_element(By.XPATH, xpath_checkbox)`                                      | Busca el checkbox de PM10 dentro de la estación.                                                                                                                                |
| `driver.execute_script("arguments[0].click();", pm10_checkbox)`                                      | Hace clic en el checkbox **mediante JavaScript**, lo cual es más seguro cuando Selenium no puede hacer clic directo (muy útil cuando los elementos están ocultos o bloqueados). |
| `time.sleep(1)`                                                                                      | Espera a que el sistema registre la selección.                                                                                                                                  |
| `estacion.click()`                                                                                   | Vuelve a hacer clic en la estación **para cerrar su lista**, manteniendo orden visual.                                                                                          |
| `time.sleep(1)`                                                                                      | Pausa final para evitar que las acciones se solapen y cause errores en la siguiente iteración del ciclo.                                                                        |



### Resumen Conceptual

Se recorren todas las estaciones visibles en la lista.

Se entra a cada estación.

Se selecciona el contaminante PM10.

Se cierra la estación.

Se repite el proceso automáticamente para todas las estaciones.


## 8. Selección del Promedio Temporal

En esta parte del código se selecciona el tipo de base temporal.
La página ofrece un menú desplegable y el script navega dentro de ese menú usando teclas del teclado.


### Código

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

### Explicación

| **Línea de Código**                                                         | **Explicación Detallada y Clara**                                                                                                                                                                          |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wait = WebDriverWait(driver, 20)`                                          | Se define una **espera inteligente** de hasta 20 segundos. Esto permite que el script espere a que aparezca el menú, sin fallar si la página carga lentamente.                                             |
| `dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, ".../span")))` | Busca el elemento correspondiente al **menú desplegable de la base temporal** y espera hasta que sea clickeable. Esto garantiza que Selenium no intente interactuar con un elemento que aún no está listo. |
| `dropdown.click()`                                                          | Abre el menú desplegable para mostrar las opciones disponibles.                                                                                   |
| `time.sleep(3)`                                                             | Pausa breve para asegurarse de que las opciones del menú carguen completamente. Sin esta pausa, podría fallar el envío de flechas.                                                                         |
| `dropdown.send_keys(Keys.ARROW_DOWN)`                                       | Envía una pulsación de la tecla **flecha hacia abajo**, moviendo la selección del menú a la siguiente opción.                                                                                              |
| `dropdown.send_keys(Keys.ARROW_DOWN)`                                       | Baja una vez más a la siguiente opción disponible.                                                                                                                                                         |
| `dropdown.send_keys(Keys.ARROW_DOWN)`                                       | Continúa bajando, dependiendo de qué opción queremos seleccionar. En este caso se baja tres posiciones.                                                                                                    |
| `dropdown.send_keys(Keys.ENTER)`                                            | Confirma la selección actual presionando **Enter**, seleccionando así la base temporal deseada.                                                                                                            |
| `time.sleep(3)`                                                             | Espera a que la página **actualice los datos** según la nueva selección antes de continuar con el proceso.                                                                                                 |


### Resumen Conceptual del Paso

Se abre el menú del promedio temporal.

Se navega dentro del menú usando teclas del teclado.

Se selecciona la opción deseada (después de moverse varias veces con flecha abajo).

Se espera a que la página actualice la configuración.


## 9. Bucle de Descarga por Años


Este bloque del código es el encargado de recorrer año por año, modificar la página para seleccionar el año correspondiente y descargar los datos generados para cada uno.

### Código

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


### Explicación

| **Línea / Bloque**                                                                                                 | **Explicación**                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `for i in range (14,25):`                                                                                          | Crea un ciclo que va desde el **2014 hasta 2024** (porque `20{i}` formará años como 2014, 2015 … 2024). Esto permite **automatizar la descarga por año**. |
| `start_date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "startDate")))`             | Espera hasta que el campo de **Fecha de Inicio** esté disponible para escribir. Si la página demora, no genera error.                                     |
| `start_date_input.send_keys(Keys.COMMAND, "a")`                                                                    | Selecciona todo el texto que haya en el campo (equivalente a *Ctrl + A* en Windows / *Command + A* en Mac).                                               |
| `start_date_input.send_keys(Keys.DELETE)`                                                                          | Borra el contenido seleccionado del campo, dejándolo vacío.                                                                                               |
| `time.sleep(2)`                                                                                                    | Espera 2 segundos para garantizar que el cambio se registre y la interfaz no falle.                                                                       |
| `texto_inicial = f"01-01-20{i}"`                                                                                   | Crea dinámicamente la fecha de inicio del año (ej: si `i = 18`, la fecha será `01-01-2018`).                                                              |
| `driver.find_element(By.ID,"startDate").send_keys(texto_inicial)`                                                  | Inserta la **nueva fecha de inicio** en el campo.                                                                                                         |
| `end_date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "endDate")))`                 | Repite el proceso, pero ahora para el campo **Fecha Final**.                                                                                              |
| `end_date_input.send_keys(Keys.COMMAND, "a")` + `end_date_input.send_keys(Keys.DELETE)`                            | Selecciona y borra el contenido existente en la fecha final.                                                                                              |
| `texto_final = f"31-12-20{i}"`                                                                                     | Crea la fecha de finalización del año (ej: `31-12-2018`).                                                                                                 |
| `driver.find_element(By.ID,"endDate").send_keys(texto_final)`                                                      | Escribe la **nueva fecha de fin** correspondiente al año del ciclo.                                                                                       |
| `driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/section[1]/div[2]/div[2]/div[3]/input[2]").click()` | Encuentra y hace **clic en el botón de Descargar/Mostrar en Excel** utilizando una ruta XPath. Este clic inicia la descarga del archivo.                  |
| `time.sleep(30)`                                                                                                   | Espera **30 segundos** para permitir que el archivo se descargue completo antes de pasar al siguiente año. Esto evita errores de descarga incompleta.     |

### Resumen Conceptual del Paso


Cambia automáticamente el rango de fechas año por año.

Limpia los campos de fecha, escribe nuevas fechas para cada año.

Presiona el botón de descarga.

Espera a que la descarga termine.

Repite el proceso para todos los años entre 2014 y 2024.


## 10. Ejecución del Script

### Código

    if __name__ == "__main__":
        main()

### Explicación

| **Línea / Bloque**           | **Explicación**                                                                                                                                                                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `if __name__ == "__main__":` | Esta línea verifica si el archivo se está ejecutando **directamente** y no siendo importado como parte de otro código. Es decir, asegura que el script **solo se ejecute automáticamente cuando lo abrimos o ejecutamos**, y no si otro programa lo importa. |
| `main()`                     | Llama a la función `main()` para **iniciar todo el proceso de Web Scraping**. Esto hace que el navegador se abra, se seleccione la información, y se descarguen los archivos.                                                                                |


## 11. Conclusiones

El script permite automatizar completamente el proceso de descarga de los datos de PM10 desde la plataforma RMCAB.

Esto evita realizar el procedimiento manualmente para cada estación y cada año.

Selenium permite simular clics y navegación, haciendo el proceso más eficiente y reproducible.

El código está diseñado para procesar múltiples estaciones y años sin intervención del usuario, reduciendo tiempo y error humano.
