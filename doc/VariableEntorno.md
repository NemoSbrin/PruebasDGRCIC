# Variable de entorno 

[:house:](../README.md)

Se puede realizar una de las acciones:

## Temporal

    Escribir en la terminal `$env:VARIABLE = 'valor'` .
    Tendrá que escribirlo cada vez que levante el ambiente de desarrollo.

## Cuando se active el ambiente

    * Escribir en el archivo `env/Scripts/Activate.ps1`,
      entre `$Env:PATH = "$VenvExecDir$...code...` y `# SIG # Begin signature block`,
      lo siguiente:

        ```
        # Add variables
        # The syntax is $env:VARIABLE="value"
        $env:VARIABLE="value"
        ```

    * Escribir en el archivo `env/Scripts/activate.bat`,
      entre `set PATH=...code...` y `:END`,
      lo siguiente:

        ```
        rem Add variables
        rem The syntax is $env:VARIABLE='value'
        set VARIABLE = 'value'
        ```

## Variables a usar

Las variable que necesitará son:

`TEST_RG_LINK = 'http://link-sevice.com/wsdl'`

    * Link del servicio proporcionado por la Dirección General de Registro Civil, Identificación y Cedulación del Ecuador.

`TEST_RG_USER = 'user'` :

    * Usuario proporcionado por la Dirección General de Registro Civil, Identificación y Cedulación del Ecuador.

`TEST_RG_PASS = 'pass'` :

    * Contraseña proporcionada por la Dirección General de Registro Civil, Identificación y Cedulación del Ecuador.

`TEST_RG_CODEINS = 0123456789`

    * Código de institucion porporcionado por la Dirección General de Registro Civil, Identificación y Cedulación del Ecuador.

`TEST_RG_CODEAGN = 0123456789`

    * Código de agencia porporcionado por la Dirección General de Registro Civil, Identificación y Cedulación del Ecuador.

`TEST_RG_DATATST = 'C:/path-to/file.csv'`

    * Código de agencia porporcionado por la Dirección General de Registro Civil, Identificación y Cedulación del Ecuador.

`TEST_RG_CAMPOS = '['campo1', 'campo2']'`

    * Lista de campos a buscar en el resultado del Client SOAP, esto dependerá de las necesidades de cada uno.

[:arrow_up_small:](#variable-de-entorno) [:house:](../README.md)
