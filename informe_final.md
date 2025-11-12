# Informe Final del Tutorial de Web Scraping en Python: Caso Práctico de la Red de Monitoreo de Calidad del Aire de Bogotá (RMCAB)

## 1. Introducción

El Web Scraping es una herramienta fundamental en el ámbito del análisis y la ciencia de datos, ya que permite extraer información de manera automatizada desde páginas web. Su utilidad radica en la posibilidad de recopilar grandes volúmenes de información estructurada, reduciendo el tiempo y el esfuerzo que implicaría hacerlo manualmente.

En este informe final, se presenta un tutorial completo de Web Scraping en Python, empleando la librería Selenium. Como ejemplo práctico, se utiliza el sitio web oficial de la Red de Monitoreo de Calidad del Aire de Bogotá (RMCAB), con el objetivo de automatizar la descarga de datos del contaminante PM10.
Este informe recopila los pasos, metodología, resultados y análisis del proceso de automatización, con el fin de servir como guía técnica y didáctica para futuros proyectos similares.


## 2. Justificación y Antecedentes

El acceso a datos ambientales en Bogotá, especialmente los relacionados con la calidad del aire, es vital para la investigación, la formulación de políticas públicas y la evaluación de impactos ambientales.
La RMCAB proporciona información pública sobre diferentes contaminantes, pero su descarga manual puede resultar lenta y repetitiva, especialmente al requerir datos de múltiples estaciones y periodos de tiempo.

La creación de un script automatizado mediante Selenium permite:

Simplificar la obtención masiva de información.

Minimizar errores humanos durante la descarga.

Garantizar una estructura de datos coherente y lista para análisis.

Facilitar la actualización periódica de los registros ambientales.

Este proyecto surge en respuesta a la necesidad de optimizar la recolección de información ambiental y fomentar la reproducibilidad científica, en un contexto donde la automatización es clave para el análisis de grandes volúmenes de datos.

## 3. Objetivos

### Objetivo General

Desarrollar un tutorial completo de Web Scraping utilizando Python y Selenium, que permita automatizar la descarga de datos del contaminante PM10 desde la Red de Monitoreo de Calidad del Aire de Bogotá (RMCAB).

### Objetivos Específicos

Explicar paso a paso la estructura y funcionamiento del código implementado.

Interactuar de forma automatizada con los elementos del portal web RMCAB.

Configurar dinámicamente los periodos de descarga de datos por año.

Documentar el proceso para su comprensión y replicabilidad.


## 4. Metodología

### 4.1 Herramientas y Entorno de Trabajo


| Herramienta            | Descripción                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| **Python 3.11**        | Lenguaje de programación utilizado para desarrollar el script.     |
| **Selenium**           | Librería principal que automatiza la interacción con el navegador. |
| **webdriver_manager**  | Instala y gestiona automáticamente el controlador de Chrome.       |
| **Google Chrome**      | Navegador utilizado para realizar las automatizaciones.            |
| **Visual Studio Code** | Entorno de desarrollo empleado para escribir y ejecutar el código. |


### 4.2 Proceso de Desarrollo del Script

El código fue estructurado en diferentes secciones, cada una con un propósito específico:

| Paso                                               | Descripción                                                                                           |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **1. Librerías utilizadas**                        | Importación de las dependencias necesarias (Selenium, time, Keys, etc.).                              |
| **2. Configuración del navegador**                 | Inicialización de `webdriver` con opciones de descarga y manejo de permisos.                          |
| **3. Acceso a la página RMCAB**                    | Apertura automática del sitio web de la red de monitoreo.                                             |
| **4. Selección del formato de salida (Excel)**     | Interacción con el elemento de descarga.                                                              |
| **5. Selección del tipo de información**           | Elección del módulo “Calidad del aire”.                                                               |
| **6. Selección de estaciones y contaminante PM10** | Uso de comandos de Selenium para hacer clic en los selectores y elegir las opciones correspondientes. |
| **7. Selección del promedio temporal**             | Configuración del tipo de promedio (diario, horario, etc.).                                           |
| **8. Bucle de descarga por años**                  | Iteración entre los años 2014 y 2024, definiendo fechas de inicio y fin.                              |
| **9. Ejecución de descarga**                       | Simulación del clic en el botón “Mostrar en Excel” y espera de la descarga.                           |
| **10. Finalización del script**                    | Cierre controlado del navegador y verificación de los archivos descargados.                           |



