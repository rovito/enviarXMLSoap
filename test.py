import requests

# URL del servicio SOAP
url = "https://test.timbra.mx/WCFTimbrador/DetecnoPac.svc"

# Leer el contenido del archivo XML
xml_file_path = r'C:\Users\jramon\Documents\pythonWorkspace\envioXMLSoap\archivo_cfdi.xml'

# Leer el contenido del archivo XML
with open(xml_file_path, 'r') as file:
    xml_content = file.read()

# Crear el cuerpo de la solicitud SOAP
soap_request = f"""
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/">
   <soap:Header/>
   <soap:Body>
      <tem:TimbrarCfdi>
         <tem:usuario>AAAAAA\\wsTIMBRADOR</tem:usuario>
         <tem:password>GlMkm9F=b+</tem:password>
         <tem:cfdi><![CDATA[{xml_content}]]></tem:cfdi>
         <tem:origen>1</tem:origen>
      </tem:TimbrarCfdi>
   </soap:Body>
</soap:Envelope>
"""

# Encabezados de la solicitud
headers = {
    'Content-Type': 'application/soap+xml; charset=utf-8',
    'SOAPAction': 'http://tempuri.org/TimbrarCfdi'
}

# Enviar la solicitud
response = requests.post(url, data=soap_request, headers=headers)

# Verificar el estado de la respuesta
if response.status_code == 200:
    print("Respuesta exitosa:", response.content.decode())
else:
    print("Error:", response.status_code, response.content.decode())
