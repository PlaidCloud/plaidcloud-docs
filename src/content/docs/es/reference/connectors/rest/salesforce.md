---
title: Conector REST de Salesforce
description: Configure una conexión a la API REST de Salesforce en PlaidCloud con el flujo de credenciales de cliente de OAuth 2.0, pruébela y extraiga objetos de CRM a tablas del proyecto con el paso Salesforce Query Object.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## Documentación de la API

La [referencia de la API REST de Salesforce](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html) documenta los puntos de conexión de registros y metadatos, y la [guía para desarrolladores de Bulk API 2.0](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm) documenta los trabajos de consulta en los que se ejecuta el paso [Salesforce: consultar objeto](/es/reference/workflow-steps/salesforce/query-salesforce-object/).

Para un recorrido completo de principio a fin (la aplicación del lado de Salesforce, el usuario Run As, la creación de la conexión y su prueba), siga la guía [Conectarse a Salesforce](/es/guides/connections/salesforce/). Esta página es la referencia de campos en la que se apoya.

## Cómo funciona la autenticación

El conector inicia sesión con **credenciales de cliente de OAuth 2.0**: PlaidCloud intercambia la clave y el secreto de consumidor de la aplicación por un token de acceso en el punto de conexión de token propio de la organización, y llama a la API como el usuario que la aplicación indica en su configuración **Run As**. No hay inicio de sesión interactivo, ni token de actualización, ni certificado que administrar.

Dos propiedades de ese intercambio importan en la práctica:

- **Un solo token cubre toda una extracción.** PlaidCloud almacena en caché el token de acceso por conexión y entorno hasta poco antes de que caduque, de modo que una lectura paginada grande no vuelve a autenticarse en cada página. Un token que Salesforce deja de aceptar antes de tiempo (revocado, por una restricción de IP o por un cambio en la política de sesión) se descarta y se reemplaza una vez, de forma automática.
- **Las solicitudes van adonde indica Salesforce.** La respuesta del token indica la instancia de la organización, y cada llamada posterior se realiza contra esa instancia y no contra el host que usted escribió, de modo que una conexión sigue funcionando después de un cambio de My Domain o de instancia.

La versión de la API REST se fija por conexión en lugar de ser variable, para que una actualización de la organización no pueda cambiar en silencio la forma de las respuestas bajo un paso guardado. Las conexiones nuevas usan una versión compatible vigente; una conexión se puede fijar a otra mediante la API de configuración de conexiones, y si una versión fijada llega al final de su vida útil, Salesforce responde con HTTP 410 y PlaidCloud informa qué versión se retiró.

## Configuración

Estos campos aparecen al crear o editar una conexión de Salesforce en **Herramientas > Conexiones**.

### Descripción de la cuenta

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre de la cuenta | Texto | Nombre para mostrar de esta conexión. |
| Memo | Texto (varias líneas) | Notas opcionales sobre la conexión. |

### Conexión

| Campo | Tipo | Descripción |
|---|---|---|
| Host o dirección IP | Texto | El host My Domain de la organización: `mycompany.my.salesforce.com` para producción y Developer Edition, `mycompany--uat.sandbox.my.salesforce.com` para un sandbox. PlaidCloud agrega `https://` si usted lo omite. |

### Credenciales de autenticación

| Campo | Tipo | Descripción |
|---|---|---|
| ID de cliente | Texto | La clave de consumidor de la aplicación. |
| Secreto de cliente | Contraseña | El secreto de consumidor de la aplicación. Se guarda cifrado; escriba un valor nuevo para cambiarlo o déjelo en blanco para conservar el almacenado. |

### Uso y seguridad

| Campo | Tipo | Descripción |
|---|---|---|
| Activa (permitir acceso) | Interruptor | Indica si la conexión se puede usar. Desmárquelo para suspender el acceso sin eliminar la conexión. |
| Modelo de seguridad | Selección | Quién puede usar la conexión: solo sus propietarios, miembros específicos, grupos de seguridad específicos o todos los miembros del espacio de trabajo. |

Cada conexión contiene un conjunto de estos valores por entorno, de modo que una misma conexión puede apuntar a un sandbox en su entorno de desarrollo y a producción en su entorno de producción. Pruebe y establezca las credenciales por entorno.

## Probar conexión

**Probar conexión** realiza el intercambio de token real e informa de con qué identidad se autentican las credenciales:

| Informado | Por qué importa |
|---|---|
| ID de la organización | Confirma a qué organización llegan las credenciales: la forma más rápida de detectar una credencial de sandbox guardada en un entorno de producción. |
| Versión de la API | La versión más alta que admite esta organización. Las lecturas se ejecutan en la versión fijada a la conexión (`v61.0` salvo que se establezca `salesforce_api_version`), no en esta. |
| Usuario Run As | El usuario al que se limitan todas las filas y campos que devuelva esta conexión. Compruébelo antes de fiarse del recuento de filas de una extracción. |

Una prueba fallida indica la causa. Los errores de autenticación informan del estado HTTP y le piden que vuelva a introducir el ID de cliente y el secreto, porque un secreto de cliente no se puede volver a leer una vez guardado.

## Limitaciones conocidas

- **El usuario Run As limita todas las lecturas, de dos maneras distintas.** Las filas que ese usuario no puede ver simplemente no aparecen, sin error ni recuento. Un campo que ese usuario no puede leer hace fallar la consulta completa. Ambos casos se describen en [El usuario Run As limita todo](/es/guides/connections/salesforce/#el-usuario-de-run-as-limita-todo).
- **Solo lecturas.** Este conector extrae datos; no escribe registros de vuelta en Salesforce.
- **Algunos tipos de campo no se pueden extraer**: los campos compuestos de dirección y geolocalización, los blobs `base64`, `encryptedstring` y `anyType`. El selector de campos del paso marca cada uno e indica el motivo. Consulte [Campos que el paso rechaza](/es/reference/workflow-steps/salesforce/query-salesforce-object/#campos-que-rechaza-el-paso).
- **Una extracción no es una sincronización.** Un registro eliminado en Salesforce permanece en la tabla de destino.

## Temas relacionados

- [Conectarse a Salesforce](/es/guides/connections/salesforce/) — tutorial paso a paso
- [Salesforce: consultar objeto](/es/reference/workflow-steps/salesforce/query-salesforce-object/)
- [Crear y administrar una conexión](/es/guides/connections/create-connection/)
