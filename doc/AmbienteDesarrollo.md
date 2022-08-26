# Ambiente de desarrollo

[:house:](../README.md)

Para la creación de un ambiente de desarrollo, se realiza los siguiente pasos:

1. ejecute [^1]  `py -m pip install --user virtualenv`
2. ejecute [^2]  `py -m venv env`
3. active el ambiente [^3] [^4]  `.\env\Scripts\activate`
4. ejecute [^5]  `python -m pip install -r requirements.txt`
5. cree las [Variables de entorno](#variables-de-entorno)
6. para desactivar el ambiente ejecute `deactivate`


[:arrow_up_small:](#ambiente-de-desarrollo) [:house:](../README.md)


[^1]: También se puede usar [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) para crear el ambiente virtual.

[^2]: Creará una carpeta donde se instalarán nuestra dependencias.

[^3]: La ruta puede ser `.\env\bin\activate`.

[^4]: Asegurese de que esté **levantado** antes de continuar. Por lo general se verá un (env) al inicio de la linea de comandos.

[^5]: Instalará nuestra dependencias en la carpeta `env\Lib\`.