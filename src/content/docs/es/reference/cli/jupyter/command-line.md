---
title: Línea de comandos
description: Use la interfaz de línea de comandos de PlaidCloud para automatizar tareas, ejecutar scripts e interactuar con los recursos de PlaidCloud desde la terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud tiene una API REST que puede usar cualquier aplicación capaz de enviar solicitudes HTTP. Para facilitar las cosas, el paquete de Python `plaidcloud-rpc` se encarga por usted de los detalles de la conexión y las solicitudes.

:::caution[JSON-RPC está obsoleto]
JSON-RPC está obsoleto y se eliminará en una versión posterior. Use `plaidcloud-rpc` 1.25.0 o posterior, que envía sus llamadas a la API REST, y escriba las nuevas integraciones contra la API REST. Consulte [JSON-RPC está obsoleto](#json-rpc-está-obsoleto).
:::


## Instalación requerida

Desde una terminal, ejecute el siguiente comando:

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## Uso del objeto SimpleRPC para hacer una solicitud

Para realizar una solicitud con el paquete `plaidcloud-rpc`, use el objeto `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Una vez que haya creado una instancia del objeto `SimpleRPC`, puede enviar solicitudes a PlaidCloud. Este ejemplo solicita los metadatos de una tabla.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC` envía cada llamada a la API REST en `/rest/v1/` del host de su espacio de trabajo, con el mismo token. Una llamada que la API REST aún no cubre, o una llamada a un espacio de trabajo que sigue en una versión anterior, usa JSON-RPC en su lugar, de modo que el mismo código funciona en ambos casos. Una llamada fallida genera `RPCError` en ambos casos.


## Llamar directamente a la API REST

`call_rest` envía una solicitud a cualquier endpoint de la API REST con el mismo token, la misma configuración TLS y los mismos reintentos que `SimpleRPC`. Indique el método HTTP, la ruta bajo `/rest/v1/` y, opcionalmente, `params` para la cadena de consulta y `body` para un cuerpo de solicitud JSON.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

Devuelve la respuesta JSON decodificada, o `None` cuando la respuesta no tiene cuerpo. Cualquier respuesta que no sea correcta genera `RPCError`, con el estado HTTP como su `code`.


## JSON-RPC está obsoleto

JSON-RPC está obsoleto y se eliminará en una versión posterior. Las versiones de `plaidcloud-rpc` anteriores a la 1.25.0 envían todas las llamadas por JSON-RPC, por lo que dejarán de funcionar cuando se elimine. Actualice a la 1.25.0 o posterior; no necesita cambiar su código de `SimpleRPC`. Escriba las nuevas integraciones contra la API REST.


## ¿Qué API están disponibles?

Hay muchas API disponibles que controlan casi todos los aspectos de PlaidCloud. La referencia interactiva de la API se ofrece por inquilino dentro de cada espacio de trabajo de PlaidCloud: abra su espacio de trabajo y vaya al menú de documentación de la API para ver el catálogo de endpoints en vivo.


## Obtención de un token OAuth

Consulte la [configuración de OAuth](/es/reference/cli/jupyter/oauth-setup/) para obtener más información sobre cómo obtener un token OAuth y cómo configurar el sistema para la autenticación automatizada.
