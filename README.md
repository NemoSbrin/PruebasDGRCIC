# Pruebas Registro Civil

El siguiente repositorio indica como realizar las pruebas del ambiente de test proporcionados por la Dirección General de Registro Civil, Identificación y Cedulación del Ecuador para el consumo de WebService. Mismo que es proporcionado una vez sea aprobada la documentación requerida.

Las pruebas se desarrolló en python 3.X.

## Creación del ambiente de desarrollo

Por buenas practicas se creará un ambiente de desarrollo para pruebas.

> Si no sabe como crearlo, puede revisar el documento [Ambiente de desarrollo](doc/AmbienteDesarrollo.md)

## Creación de variables de entorno

Por buenas practicas se creará variables de entorno, evitando quemar código o información delicada.

> Si no sabe como crearlo, puede revisar el documento [Variables de entorno](doc/VariableEntorno.md)

## Consumo del servicio SOAP

Se manda a llamar las variables creadas:
```
URL = os.environ.get('TEST_RG_LINK')
Usuario = os.environ.get('TEST_RG_USER')
Contrasenia = os.environ.get('TEST_RG_PASS')
CodigoInstitucion = os.environ.get('TEST_RG_CODEINS')
CodigoAgencia = os.environ.get('TEST_RG_CODEAGN')
setDePruebas = os.environ.get('TEST_RG_DATATST')
```

Utilizamos la libreria zeep para consultar el wsld. *Más información revisar el siguiente [video](https://www.youtube.com/watch?v=jReyPAxCJr0&ab_channel=PavelNicolaMoralesBustamante)*

Se ingresa los parámetros en el método BusquedaPorNui del service al que estamos consultando.
```
Cliente.service.BusquedaPorNui(CodigoInstitucion, CodigoAgencia, Usuario, Contrasenia, nui)
```

El resultado es guardado en el archivo `results.csv`
