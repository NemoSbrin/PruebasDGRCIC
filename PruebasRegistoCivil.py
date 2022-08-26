import os

from zeep import Client

""" 1. Importamos las variables de entorno a utilizar
"""
URL = os.environ.get('TEST_RG_LINK')
Usuario = os.environ.get('TEST_RG_USER')
Contrasenia = os.environ.get('TEST_RG_PASS')
CodigoInstitucion = os.environ.get('TEST_RG_CODEINS')
CodigoAgencia = os.environ.get('TEST_RG_CODEAGN')
setDePruebas = os.environ.get('TEST_RG_DATATST')

msg = f"""\nSe utiliza el usuario {Usuario} con la contraseña {Contrasenia} .
El código de Institución es {CodigoInstitucion} .
El código de Agencia es {CodigoAgencia} .
El link del web service es {URL} .
El set de pruebas es {setDePruebas} .
"""
print(msg)

""" 2. Se crea el cliente para el servicio
"""
Cliente = Client(URL)

""" 3. Se lee los NUI del set de pruebas
"""
with open(file=setDePruebas, mode='r', encoding='utf-8') as file:
    NUIs = file.readlines()

""" 4. Se consulta cada NUI en el método BusquedaPorNui y el resultado es guardado en Info para crear
       un archivo de respuesta. Se usa los valores de CodigoError y Error.
"""
Info = []
for nui in NUIs:
    serviceBusquedaPorNui = Cliente.service.BusquedaPorNui(CodigoInstitucion, CodigoAgencia, Usuario, Contrasenia, nui[:-1])
    Info.append([nui, serviceBusquedaPorNui.CodigoError, serviceBusquedaPorNui.Error])

""" 5. Creación del archivo results.csv.
"""
with open(file='results.csv', mode='w+', encoding='utf-8') as file:
    file.writelines('NUI; CodigoError; Error\n')
    for i in Info:
        file.writelines(f"{i[0][:-1]}; {i[1]}; {i[2]}\n")

