# Timbrado de CFDI mediante SOAP

Este proyecto es un script en Python que permite timbrar un CFDI (Comprobante Fiscal Digital por Internet) utilizando un servicio SOAP. El script interactúa con un servicio web para enviar el CFDI y procesar la respuesta, guardando los resultados en archivos para su posterior revisión.

---

## Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Configuración](#configuración)
3. [Ejecución](#ejecución)
4. [Estructura del Código](#estructura-del-código)
5. [Manejo de Respuestas](#manejo-de-respuestas)
6. [Registro de Tiempos](#registro-de-tiempos)
7. [Instalación y Configuración](#Instalación-y-Configuracion)
8. [Ejemplo de Uso](#ejemplo-de-uso)
9. [Notas Adicionales](#notas-adicionales)
10. [Solución de Problemas](#solución-de-problemas)

---

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalados los siguientes componentes:

- **Python 3.x**: El script está escrito en Python 3. Puedes descargarlo desde [python.org](https://www.python.org/).
- **Biblioteca `zeep`**: Es una biblioteca para interactuar con servicios web SOAP. Instálala usando pip:
  ```bash
  pip install zeep
 **Biblioteca `request`**: Se usa para verificar la disponibilidad de la URL antes de hacer la solicitud SOAP. Instálala usando pip:
  ```bash
  pip install request
  
Archivo XML (CFDI): Un archivo XML válido que represente el CFDI que deseas timbrar.

Configuración
1. Archivo XML (CFDI)
Coloca el archivo XML del CFDI en la ruta especificada en la variable xml_file_path dentro del script. Por ejemplo:
    xml_file_path = r'C:\Users\jramon\Documents\pythonWorkspace\envioXMLSoap\archivo_cfdi.xml'
2. URL del WSDL
Asegúrate de que la URL del WSDL (wsdl_url) sea correcta y esté accesible. Por ejemplo:
    wsdl_url = "https://test.timbra.mx/WCFTimbrador/DetecnoPac.svc?wsdl"
3. Credenciales de Acceso
Proporciona las credenciales de usuario y contraseña en la llamada al método TimbrarCfdi:
    response = client.service.TimbrarCfdi(
        usuario="AAAAAA\\wsTIMBRADOR",
        password="GlMkm9F=b+",
        cfdi=cfdi_content,
        origen=1
    )

Ejecución
Para ejecutar el script, sigue estos pasos:
1. Abre una terminal o línea de comandos.
2. Navega al directorio donde se encuentra el script.
3. Ejecuta el siguiente comando:
    python timbrar_cfdi.py

Estructura del Código
El script está estructurado en las siguientes secciones:

1. Importaciones
    zeep: Para interactuar con el servicio SOAP.
    datetime: Para manejar fechas y horas.
    Fault: Para manejar errores específicos de SOAP.

2. Lectura del Archivo XML
    Lee el contenido del archivo XML especificado en xml_file_path.
    Si el archivo no existe o está vacío, el script termina con un mensaje de error.

3. Creación del Cliente SOAP
    Inicializa el cliente SOAP utilizando la URL del WSDL.
    Configura el cliente para manejar WSDL menos estrictos.

4. Llamada al Servicio SOAP
    Envía el CFDI al servicio SOAP utilizando el método TimbrarCfdi.
    Procesa la respuesta del servicio.

5. Manejo de Respuestas
    Si la respuesta es exitosa (Success = True), guarda el XML timbrado en un archivo.
    Si hay errores, guarda el mensaje de error en un archivo de texto.

6. Registro de Tiempos
    Registra el tiempo de inicio, fin y duración del proceso.
-----------------------------------------------------------    
Manejo de Respuestas
El script genera dos tipos de archivos de salida:

1. Respuesta Exitosa
    Si el timbrado es exitoso, se guarda un archivo XML con el contenido de la respuesta.
    El nombre del archivo sigue el formato respuesta_YYYYMMDD_HHMMSS.xml.

2. Respuesta con Errores
    Si hay errores, se guarda un archivo de texto con el mensaje de error.
    El nombre del archivo sigue el formato error_YYYYMMDD_HHMMSS.txt.

------------------------------------------
Registro de Tiempos
El script registra el tiempo de inicio, fin y duración del proceso. Esto es útil para medir el rendimiento y depurar posibles problemas.

Ejemplo de salida:

>>> Inicio del proceso: 2023-10-15 14:30:00
>>> Fin del proceso: 2023-10-15 14:30:05
>>> Duración total del proceso: 0:00:05

-------------------------------------------------

Instalación y Configuración

Clonar el repositorio desde GitHub:

    git clone https://github.com/tuusuario/envio-xml-soap.git
    cd envio-xml-soap

Instalar dependencias:

    pip install zeep
    pip install request

Configurar el entorno:

    Modifica wsdl_url con la URL del servicio SOAP.
    Define la ruta del archivo XML en xml_file_path.
    Ajusta las credenciales (usuario y password).

--------------------------------------------------------------

Ejemplo de Uso
1. Coloca tu CFDI en la ruta especificada (archivo_cfdi.xml).

2. Ejecuta el script:
    python timbrar_cfdi.py

3. Revisa los archivos generados:
    Si el timbrado fue exitoso, busca un archivo respuesta_*.xml.
    Si hubo errores, busca un archivo error_*.txt.

-------------------------------------------------
Notas Adicionales

Acceso a Internet: Asegúrate de tener conexión a Internet para interactuar con el servicio SOAP.
Credenciales: Verifica que las credenciales de usuario y contraseña sean correctas.
Validación del CFDI: Asegúrate de que el archivo XML sea válido y esté correctamente formateado.

----------------------------------------------

Solución de Problemas
1. Error: FileNotFoundError
    Verifica que la ruta del archivo XML sea correcta.
    Asegúrate de que el archivo exista y tenga permisos de lectura.

2. Error: zeep.exceptions.Fault
    Revisa el mensaje de error devuelto por el servicio SOAP.
    Verifica que las credenciales y el contenido del CFDI sean correctos.

3. Error: AttributeError
    Asegúrate de que la respuesta del servicio contenga los campos esperados (Success, XmlTfd, etc.).

4. Error: Conexión al Servicio SOAP
    Verifica que la URL del WSDL sea correcta y esté accesible.
    Asegúrate de que no haya problemas de red o firewalls bloqueando la conexión.

-------------------------------------------------
Contribuciones

Si deseas contribuir a este proyecto, ¡eres bienvenido! Puedes:

    Reportar problemas o sugerir mejoras.
    Enviar pull requests con correcciones o nuevas funcionalidades.

    Realiza un fork del repositorio.
        Crea una nueva rama (git checkout -b feature-nueva-funcionalidad).
        Realiza tus cambios y confirma los commits (git commit -m 'Agrega nueva funcionalidad').
        Envía los cambios a tu fork (git push origin feature-nueva-funcionalidad).
        Abre un Pull Request en el repositorio original.

Autor
Jonathan Ramón
Programa v1 para consumo de servicios SOAP para Facturacio¿ón Electrónica