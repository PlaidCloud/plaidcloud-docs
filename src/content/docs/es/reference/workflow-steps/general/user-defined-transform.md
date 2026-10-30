---
title: User Defined Transform
description: Cree transformaciones de datos personalizadas con código Python en un paso de flujo de trabajo de PlaidCloud para disponer de una lógica de procesamiento de datos flexible y potente.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## Descripción

Las **transformaciones estándar de flujo de trabajo** que incluye PlaidCloud suelen poder realizar casi todas las operaciones que necesitará. Además, estas transformaciones estándar se optimizan continuamente para mejorar el rendimiento y ofrecen los datos más sólidos. Sin embargo, cuando las opciones estándar, usadas por separado o en grupo, no permiten alcanzar sus objetivos, puede crear **transformaciones definidas por el usuario** para satisfacer sus necesidades. PlaidCloud permite usar código estándar de Python, incluidos muchos paquetes avanzados.

Para crear una transformación definida por el usuario se requiere programar en Python, y se ejecuta en Python 3.14. Para obtener más información, visite el [sitio web de Python.](https://www.python.org/)



## Transformaciones definidas por el usuario

Hay dos maneras de crear funciones definidas por el usuario (UDF):
 - Escribir y mantener la lógica directamente en PlaidCloud
 - Conectarse a un repositorio de Git y apuntar a un archivo

Además de usar Python estándar, todas las funciones de la API de PlaidCloud están disponibles para interactuar de forma nativa con PlaidCloud.  Los paquetes de análisis avanzado como SciPy, PySpark, Pandas y muchos más están listos para importarse.

### Escribir y mantener una UDF almacenada en PlaidCloud
Para crear una nueva función definida por el usuario (UDF), abra el flujo de trabajo que necesita la transformación personalizada, seleccione la pestaña **Definido por el usuario** y haga clic en el botón **Add User Defined Function**. Especifique un ID para la UDF. Una vez creada, seleccione el icono Edit function logic (el primero a la izquierda) para abrir la ventana “Edit User Defined Function”.

Como alternativa, se puede importar una función definida por el usuario creada anteriormente con el botón **Importar** de la pestaña **Definido por el usuario**. Simplemente pulse ese botón y seleccione el flujo de trabajo correspondiente en el menú desplegable (este menú contiene todos los flujos de trabajo del espacio de trabajo actual). A continuación, seleccione las funciones que se importarán y pulse el botón **Import Selected Functions**.

Una vez creada o importada la función, vaya a la pestaña **Analyze Steps** del flujo de trabajo y agregue un paso **User Defined Transform** en la posición adecuada, igual que agregaría una **transformación estándar**. En la ventana de configuración, seleccione Analizar UDF como tipo y, después, seleccione la **Función definida por el usuario** correspondiente en el menú desplegable.

### Hacer referencia a una UDF en un repositorio de Git

Primero deberá crear una conexión con el repositorio de Git (por ejemplo, GitHub, GitLab, etc.) en el área **Conexiones de datos externas**.

Cuando la conexión con el repositorio de Git esté disponible, vaya a la pestaña **Analyze Steps** del flujo de trabajo y agregue un paso **User Defined Transform** en la posición adecuada, igual que agregaría una **transformación estándar**. En la ventana de configuración, seleccione Repositorio de código fuente externo como tipo y, después, seleccione la conexión, la rama y la ruta del archivo de la UDF.  La selección de la rama también admite elegir etiquetas para habilitar procesos de publicación estándar.

Los cambios en los archivos de Git se reflejarán automáticamente la próxima vez que se ejecute la UDF.

## Configuración de las tablas de origen y de destino
Aunque es posible acceder directamente a las tablas en una UDF sin definirlas en la configuración de la transformación UDF, las dependencias de las tablas no estarán disponibles.  Por eso se recomienda definir en la configuración todos los orígenes y destinos de tabla que se usan en la UDF.  Definir las tablas en la configuración también hace que estén disponibles para usarlas dentro de la UDF de una manera más directa (vea más abajo).

## Especificación de variables adicionales
Las variables de nivel de proyecto y de flujo de trabajo están disponibles dentro de la UDF mediante los métodos estándar de la API; sin embargo, a menudo hay variables adicionales, específicas del paso, que resultan útiles.  Se pueden definir en la sección **Otras variables** de la configuración.

Los valores de las variables se pueden establecer manualmente o definirse de forma dinámica mediante combinaciones de variables de proyecto y de flujo de trabajo.

## Ejemplos de UDF de Python

### Importaciones comunes con la configuración de la conexión de la API de PlaidCloud

```python
### COMMON PYTHON IMPORTS
# import os
# import pandas as pd
# import numpy as np

### COMMON PLAIDCLOUD IMPORTS
from plaidcloud.utilities.connect import PlaidConnection
from plaidcloud.utilities import frame_manager as fm
# from plaidcloud.utilities import data_helpers as dh

conn = PlaidConnection()
```

### Establecer mensajes de registro en el registro de la aplicación
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### Acceso a las variables de proyecto y de flujo de trabajo
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### Guardar datos en una tabla
Este ejemplo supone que los datos existen en un dataframe de Pandas.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### Leer datos de una tabla

Para usar una tabla, primero debe obtener el objeto de la tabla.  Una vez que tenga el objeto, puede consultarlo con el método `get_data()`.  El método `get_data()` también admite la sintaxis de SQLAlchemy para habilitar capacidades avanzadas de creación de consultas.  El resultado de la consulta es un objeto dataframe de Pandas.

```python
tbl_object = conn.get_table('INBOUND_TABLE_NAME')
dfImport = conn.get_data(tbl_object)
dfImportQuery = conn.get_data(
    tblImport.select().with_only_columns(
        [tblImport.c.Col1, tblImport.c.Col2]
    ).where(
        tblImport.c.Col1 == 'FilterValue'
    )
)
```

### Acceso a los datos de las tablas de origen y de destino definidas
Cuando se usan tablas de origen y de destino definidas que se configuraron en la configuración del paso, la obtención inicial del objeto (es decir, `get_table()`) se realiza automáticamente.  Para utilizar las tablas preconfiguradas se sigue este proceso:

```python
# Source Tables as a dict
my_source = conn.udf.source_by_name('my_table')

# All sources as a list
my_sources = conn.udf.sources()

# Target Tables as a dict
my_target = conn.udf.target_by_name('my_table')

# All targets as a list
my_targets = conn.udf.targets()
```

### Acceso a las variables del paso
El acceso a las variables definidas en la configuración del paso se realiza con el siguiente proceso:

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Lectura de archivos desde Document
Acceder a los archivos de Document también es sencillo con la conexión de PlaidCloud.  Este es un ejemplo de una función que obtiene el contenido del archivo y lo guarda en una ruta local del contenedor en tiempo de ejecución.

```python
def get_from_document(conn, document_account, remote_path, local_file_path):
    # accounts = conn.document.view.shared_accounts()
    remote_file = base64.b64decode(
        conn.document.view.download(
            account_id=document_account,
            path=remote_path,
        )
    )
    with open(local_file_path, 'wb') as output_file:
        output_file.write(remote_file)

    return local_file_path
```
