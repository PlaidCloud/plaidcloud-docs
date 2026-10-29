---
title: Solución de problemas
description: Problemas habituales al conectar agentes de IA con el servidor MCP de PlaidCloud y cómo resolverlos.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/troubleshooting.md
---

## Cursor (u otro cliente estricto) no se conecta en absoluto

Síntoma: el servidor nunca establece una sesión en Cursor ni en clientes estrictos similares, mientras que el mismo espacio de trabajo funciona en Claude Code.

Causa: una **barra diagonal final** en la URL del servidor. Utilice `https://<your-workspace>.plaid.cloud/mcp`, no `.../mcp/`. Los clientes estrictos rechazan una URL con barra diagonal final (o no siguen la redirección que emitía la ruta anterior), mientras que los clientes más permisivos, como Claude Code, la toleran.

Solución: elimine la barra diagonal final de `url` en su configuración y vuelva a conectarse. Todos los ejemplos de estas guías usan la forma sin barra diagonal.

## “failed to Connect” / “session Not Found”

Síntoma: la configuración del cliente parece correcta, pero el servidor aparece como fallido en el panel de estado de MCP del cliente. Los registros del servidor muestran errores 404 `Session not found`.

Causa: un error conocido en algunos clientes MCP (en particular Claude Code 2.1.111 con encabezados `Authorization` estáticos) por el cual el cliente no conserva `mcp-session-id` entre solicitudes HTTP sucesivas. El servidor MCP de PlaidCloud se ejecuta en modo HTTP sin estado para evitarlo; si lo observa en un tenant que no se ha vuelto a implementar desde la corrección, pida a su administrador que lo implemente de nuevo.

Hasta que se complete la nueva implementación, el flujo de OAuth (sin encabezados `Authorization` estáticos) sigue funcionando porque utiliza una ruta de código distinta en el cliente.

## La página “application Access Request”

Síntoma: tras iniciar sesión en PlaidCloud durante una autorización de OAuth, llega a una página titulada **Application Access Request** que nombra una aplicación y un URI de redirección, y debe hacer clic en Aprobar para que el flujo continúe.

Causa: es el comportamiento esperado. Cada autorización de OAuth a través del servidor MCP de PlaidCloud muestra esta página para que usted confirme a qué se está conectando antes de que reciba un token: indica la aplicación solicitante y el URI de redirección al que enviará las credenciales. Compruebe que ambos corresponden al cliente con el que realmente se está conectando y no apruebe una solicitud que usted no haya iniciado.

Un cliente que ya está conectado no vuelve a ver esta página al renovar el token; solo una autorización nueva (la primera conexión, o después de que el token de renovación caduque o se revoque) vuelve a mostrarla.

Solución: no hay nada que corregir; apruebe la página para continuar. Si inició la autorización en un navegador (o perfil) y la página se muestra en otro, no se completará: el consentimiento está vinculado al navegador que inició el flujo. Reinicie la autorización desde el mismo navegador en el que tiene la sesión iniciada en PlaidCloud.

## “oauth Flow is Not in Progress” durante el inicio de sesión en Claude Code

Síntoma: autoriza en el navegador, pega la URL de devolución de llamada en Claude Code y este indica que no hay ningún flujo en curso.

Causa: el estado de OAuth en memoria del puente es por puerto y puede perderse entre las llamadas a las herramientas `authenticate` y `complete_authentication`, en particular en sesiones remotas o SSH donde la devolución de llamada del navegador no puede llegar a `localhost`.

Solución: cambie al flujo de token Bearer estático. Abra `https://<your-workspace>.plaid.cloud/mcp/setup/token` en un navegador donde tenga la sesión iniciada en PlaidCloud, copie el fragmento en su `.mcp.json` y reinicie Claude Code.

## Token caducado

Síntoma: las herramientas que funcionaban ayer ahora devuelven 401 Unauthorized.

Causa: los tokens Bearer estáticos siguen la política de duración del token de acceso de su realm de Keycloak (normalmente de unas horas a un día).

Solución: vuelva a cargar `https://<your-workspace>.plaid.cloud/mcp/setup/token` para generar un token nuevo y péguelo en su configuración. Para sesiones de larga duración, prefiera OAuth: los clientes que lo admiten renuevan los tokens automáticamente.

## “no `access_token` in Session”

Síntoma: al abrir `/mcp/setup/token` aparece “Sign-in required” o “No access_token in session” aunque tenga la sesión iniciada en PlaidCloud.

Causa: su sesión se estableció mediante una ruta de inicio de sesión que no almacenó en caché el token de Keycloak (poco frecuente, pero posible).

Solución: cierre la sesión de PlaidCloud y vuelva a iniciarla desde la página de inicio de sesión estándar. La nueva sesión incluirá el token de acceso.

## Herramientas ausentes o catálogo incompleto

Síntoma: `mcp_introspect` devuelve menos herramientas de las esperadas, o faltan herramientas concretas que necesita.

Causa 1 (ámbitos): las herramientas requieren ámbitos específicos de PlaidCloud (por ejemplo, `analyze.workflow.write`). Si su cuenta no tiene el ámbito, la herramienta se negará a ejecutarse. Ejecute `mcp_introspect(name='<tool>')` para ver `required_scopes`. Pida al administrador de su espacio de trabajo que conceda el ámbito o ejecute la operación con una cuenta que lo tenga.

Causa 2 (versiones no coincidentes): es posible que una implementación anterior no tenga todas las herramientas descritas en la documentación más reciente. Compare el número de herramientas de `mcp_introspect()` con las notas de versión de su versión actual y solicite una nueva implementación si es necesario.

## Varios tenants: ¿a qué tenant acaba de acceder el agente?

Síntoma: tiene configurados varios tenants de PlaidCloud y la respuesta del agente podría provenir de cualquiera de ellos.

Solución: indique el tenant de forma explícita en su instrucción (“en el tenant **dev**, enumere los flujos de trabajo…”). Los nombres de servidor MCP que eligió en su configuración (por ejemplo, `plaidcloud-prod`, `plaidcloud-dev`) sirven también como identificadores con los que el modelo puede distinguirlos. Para operaciones de alto riesgo, mantenga producción desactivada en el selector de conectores hasta que realmente la necesite.

## Límites de frecuencia y cuota

La superficie REST de PlaidCloud tiene un límite de solicitudes por minuto aplicado por el mismo middleware que da servicio a la interfaz de usuario. Las llamadas MCP comparten ese límite. Si un agente lanza una ráfaga larga de llamadas `find` (por ejemplo, al intentar enumerar todos los proyectos, flujos de trabajo y pasos), es posible que alcance el límite. Utilice la paginación (`cursor`, `limit`) y `count_only=True` para comprobar tamaños en lugar de obtener el conjunto de resultados completo.

Tenga en cuenta que una búsqueda devuelve 25 filas por página de forma predeterminada (`step_find` devuelve 50), por lo que enumerar un conjunto grande requiere más llamadas que antes: aumente `limit` en un barrido deliberado en lugar de paginar con el valor predeterminado. Por el contrario, si sigue alcanzando el límite, `count_only=True` y una proyección `fields=[...]` más ajustada suelen indicar que no necesitaba el barrido.

## Una lista parece corta o un agente dice “eso es todo”

Síntoma: una búsqueda devolvió menos filas de las esperadas, o el agente concluyó que un proyecto tiene 25 tablas cuando tiene 300.

Solución: revise el sobre de la respuesta. Una página limitada establece `next_cursor`, y una herramienta de búsqueda también nombra la lista recortada en `truncated`; cualquiera de los dos indica que hay más por obtener. `total` informa del recuento completo en cualquier caso, así que compárelo con las filas recibidas. Pida al agente que pagine con el cursor o que vuelva a ejecutar la búsqueda con un `limit` mayor.

## Un resultado tiene el aspecto `{"_fmt": "cols", ...}`

Síntoma: una herramienta devolvió `{"_fmt": "cols", "cols": [...], "rows": [[...]]}` en lugar de la lista de objetos que esperaba.

Es la forma prevista para un resultado grande cuyas filas tienen todas los mismos campos: los nombres de los campos se envían una sola vez en lugar de repetirse en cada fila. La fila *i* es `dict(zip(cols, rows[i]))`. Se informa de esto a los agentes cuando se conectan y lo gestionan sin necesidad de indicaciones; si lee estas respuestas desde su propio código, decodifique ambas formas, porque los resultados pequeños e irregulares siguen llegando como matrices de objetos normales. Nada más del sobre cambia y no se altera ningún valor. Consulte [Introducción a los agentes de programación con IA](/es/integrations/ai-coding-agents/getting-started/#resultados-orientados-a-columnas).

## Obtener ayuda

Para problemas del lado del servidor (fallos de autenticación, herramientas que devuelven errores sin una causa evidente, herramientas ausentes), revise primero el sobre `error` de la respuesta. Cada fallo incluye `code`, `retryable`, `message` y, con frecuencia, un `hint`. Si la sugerencia no es suficiente, comuníquese con su administrador de PlaidCloud o abra un ticket de soporte con el ID de la solicitud (devuelto en el encabezado de respuesta `X-Request-Id`).
