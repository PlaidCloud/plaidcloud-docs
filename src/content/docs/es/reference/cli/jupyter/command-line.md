---
title: Línea de comandos
description: Use la interfaz de línea de comandos de PlaidCloud para automatizar tareas, ejecutar scripts e interactuar con los recursos de PlaidCloud desde la terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud usa solicitudes JSON-RPC estándar y se puede utilizar con cualquier aplicación capaz de realizar esas solicitudes.


Para facilitar las cosas, hay disponible un paquete de Python que simplifica el proceso de conexión y de ejecución de la API.


## Instalación requerida

Desde una terminal, ejecute el siguiente comando:

```bash
pip install plaidcloud-rpc
```


## Uso del objeto Simplerpc para realizar una solicitud

Para realizar una solicitud con el paquete `plaidcloud-rpc`, use el objeto `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Una vez que haya instanciado el objeto `SimpleRPC`, puede enviar solicitudes RPC a PlaidCloud. Este ejemplo solicita los metadatos de una tabla.

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## ¿Qué API están disponibles?

Hay muchas API disponibles que controlan casi todos los aspectos de PlaidCloud. La referencia interactiva de la API se ofrece por inquilino dentro de cada espacio de trabajo de PlaidCloud: abra su espacio de trabajo y vaya al menú de documentación de la API para ver el catálogo de endpoints en vivo.


## Obtención de un token OAuth

Consulte la [configuración de OAuth](/es/reference/cli/jupyter/oauth-setup/) para obtener más información sobre cómo obtener un token OAuth y cómo configurar el sistema para la autenticación automatizada.
