from zeep import Client, Settings
from zeep.exceptions import Fault
from datetime import datetime

# Configuración de la URL del servicio SOAP
wsdl_url = "https://test.timbra.mx/WCFTimbrador/DetecnoPac.svc?wsdl"

# Ruta del archivo XML (CFDI)
xml_file_path = r'C:\Users\jramon\Documents\pythonWorkspace\envioXMLSoap\archivo_cfdi.xml'

# Leer el archivo XML (CFDI)
try:
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        cfdi_content = file.read()
except FileNotFoundError:
    print(f"Error: El archivo {xml_file_path} no se encontró.")
    cfdi_content = ""

# Verificar si el CFDI tiene contenido
if not cfdi_content:
    print("Error: El contenido del CFDI está vacío. Verifica el archivo.")
    exit(1)

# Crear el cliente SOAP
try:
    settings = Settings(strict=False)  # Configuración para manejar WSDL menos estrictos
    client = Client(wsdl=wsdl_url, settings=settings)
except Exception as e:
    print(f"Error al inicializar el cliente SOAP: {e}")
    exit(1)

# Función para guardar la respuesta en un archivo XML
def guardar_respuesta_en_xml(respuesta, prefix="salidaXml/respuesta"):
    # Crear un nombre único basado en la fecha y hora actual
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{prefix}_{timestamp}.xml"

    # Guardar la respuesta en el archivo
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(respuesta)
    print(f"Respuesta guardada en el archivo: {nombre_archivo}")

def guardar_salida_en_archivo(contenido, prefix="errores/error"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"{prefix}_{timestamp}.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)
    print(f"Error guardado en el archivo: {nombre_archivo}")

# Registro de tiempo de inicio
inicio = datetime.now()
print(f">>> Inicio del proceso: {inicio.strftime('%Y-%m-%d %H:%M:%S')}")

# Llamar al método del servicio SOAP
try:
    print(">>> Enviando solicitud SOAP...")
    response = client.service.TimbrarCfdi(
        usuario="AAAAAA\\wsTIMBRADOR",
        password="GlMkm9F=b+",
        cfdi=cfdi_content,
        origen=1
    )
    print(">>> Respuesta del servicio SOAP recibida.")
    print(response)
    
    # Validar el campo Success en la respuesta
    if hasattr(response, 'Success') and response.Success:
        print(">>> El atributo 'Success' es True. Guardando respuesta...")
        # Guardar el XML si Success es True y el campo XmlTfd no es None
        if hasattr(response, 'XmlTfd') and response.XmlTfd:
            guardar_respuesta_en_xml(response.XmlTfd)
        else:
            print(">>> No se encontró el XML en la respuesta exitosa.")
    else:
        print(">>> El atributo 'Success' es False.")
     #   print(f"Error: {response.ErrCode} - {response.ErrDesc}")
        print(f"Mensaje del servidor: {response.Msg}")
        guardar_salida_en_archivo(response.ErrDesc)

except Fault as fault:
    print(">>> Error al procesar la solicitud SOAP:")
    print(fault)
except Exception as e:
    print(f"Error inesperado: {e}")
    
    

# Registro de tiempo de fin
fin = datetime.now()
print(f">>> Fin del proceso: {fin.strftime('%Y-%m-%d %H:%M:%S')}")

# Calcular y mostrar la duración total
duracion = fin - inicio
print(f">>> Duración total del proceso: {duracion}")
