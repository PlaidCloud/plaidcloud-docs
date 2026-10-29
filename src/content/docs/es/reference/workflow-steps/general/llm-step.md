---
title: Paso LLM
description: Ejecute un prompt contra un LLM con acceso limitado de lectura o escritura a los datos del proyecto, de modo que el modelo escriba sus resultados directamente a través del servidor MCP.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/llm-step.md
---

## Descripción

El **Paso LLM** envía un prompt a un modelo de lenguaje de gran tamaño. Con una conexión de LLM de Anthropic, el modelo obtiene acceso limitado a las tablas, dimensiones y documentos del proyecto que usted vincule (**Leer**, **Escribir** o ambos por objeto) y escribe sus resultados directamente en las vinculaciones con escritura habilitada. Una vinculación de escritura es la salida del paso; no existe un formato de salida independiente.

Para ver un recorrido completo, consulte la [guía del Paso LLM](/es/guides/workflows/llm-step/).

## Configuración

* **Conexión de LLM** *(obligatorio)*: una conexión de tipo LLM (por ejemplo, Anthropic). Su **Acceso del agente** debe ser **Lectura y escritura** para cualquier vinculación de escritura. **Completo** también permite escribir hasta que se elimine el 15 de enero de 2027, y un paso que lo usa registra una advertencia al finalizar. Con **Lectura y escritura**, un paso solo escribe en las vinculaciones con Escribir marcado y no puede ejecutar SQL que escriba ni crear tablas.
* **Modelo** *(opcional)*: de forma predeterminada, el modelo predeterminado de la conexión. Con una conexión de Anthropic funciona cualquier modelo Claude, incluidos modelos anteriores como Claude Sonnet 4.5.
* **Prompt** *(obligatorio)*: admite referencias `{{tables.NAME}}`, `{{dimensions.NAME}}` y `{{documents.NAME}}` a los objetos vinculados.
* **Esquema de resultado** *(opcional para Anthropic; obligatorio para otros proveedores)*: un esquema JSON (raíz `"type": "object"`) para un resumen estructurado capturado; con Anthropic, déjelo en blanco cuando el trabajo del modelo sean sus escrituras por MCP. Los proveedores distintos de Anthropic no tienen acceso a MCP, por lo que se requiere un esquema.
* **Vinculaciones**: las tablas, dimensiones y documentos a los que puede acceder el modelo, cada uno elegido con un selector y con permiso de **Leer** o **Escribir**, o ambos. Las tablas de escritura reciben filas insertadas, las dimensiones de escritura reciben nodos y los documentos de escritura reciben archivos cargados.
* **Límites**: Máximo de tokens de salida (de 1024 a 128 000) y TTL de credencial (de 60 a 3600 segundos).

## Comportamiento

* La llamada al modelo se ejecuta en su propio trabajo. Se genera una credencial limitada y de corta duración para la ejecución, y se revoca cuando esta termina.
* El acceso se controla por objeto y por casilla: el modelo solo lee los objetos vinculados con Leer y solo escribe en los vinculados con Escribir, nunca en un objeto que usted no haya vinculado. Para escribir se requiere un objeto de destino existente; el paso no crea ninguno.
* Cada ejecución realiza una llamada facturable al proveedor y escribe en los objetos que usted vinculó.

## Qué se comprueba al guardar

* **Esquema de resultado**: cuando indica uno, debe ser JSON válido, un objeto JSON y declarar `"type": "object"` en su raíz. De lo contrario, se rechaza el guardado, por ejemplo con *The result schema must declare "type": "object" at its root.*
* **Vinculaciones y la conexión**: solo una conexión de Anthropic da al modelo acceso a las vinculaciones. Se rechaza guardar un paso con vinculaciones en la conexión de otro proveedor, con un mensaje que nombra al proveedor y le pide *Remove the bindings or choose an Anthropic connection.* Una vinculación con **Escribir** marcado necesita una conexión cuyo **Acceso del agente** permita escribir. En una conexión de solo lectura, se rechaza el guardado con *The selected LLM connection has Read-only Agent Access, so a binding with Write checked could not write. Set the connection to 'Read & write' or uncheck Write on the bindings.* Un paso guardado mediante la API sin conexión se comprueba con la conexión de LLM predeterminada del espacio de trabajo, en la que también se ejecuta: la que un administrador marcó como predeterminada o, si no, la actualizada más recientemente. Sin una conexión predeterminada marcada por un administrador, editar otra conexión de LLM hace que esa pase a ser la predeterminada y puede provocar que se rechace el siguiente guardado del paso.
