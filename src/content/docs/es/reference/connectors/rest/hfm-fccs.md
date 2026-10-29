---
title: Conector HFM / FCCS
description: Configure una conexión a Oracle FCCS (Financial Consolidation and Close, EPM Cloud) en PlaidCloud para obtener por cuenta propia un segmento de datos ad hoc con un selector de punto de vista, con almacenamiento en caché opcional y una carga recurrente programada.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

Conecte PlaidCloud a Oracle **FCCS** (Financial Consolidation and Close, parte de Oracle EPM Cloud) para que un usuario de finanzas pueda obtener por cuenta propia un segmento de datos sin abrir una solicitud con el equipo de HFM. El paso [HFM/FCCS: leer datos (ad hoc)](/es/reference/workflow-steps/oracle-epm/hfm-fccs-read/) parece una consulta en vivo, pero internamente es una secuencia asíncrona de solicitud, sondeo y obtención contra la API de trabajos de exportación de datos de FCCS.

El tipo de conexión aparece en el selector de conexiones como **REST - HFM/FCCS**.

:::note[Delimite la dimensión de entidad]
Mantenga acotado cada punto de vista: una extracción sin delimitar puede bloquear la aplicación de FCCS durante mucho tiempo mientras se ejecuta el trabajo de exportación.
:::

## Documentación de la API

El conector utiliza la [API REST](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html) de Oracle EPM Cloud: los puntos de conexión de metadatos de la aplicación (para descubrir dimensiones y miembros) y los puntos de conexión de trabajos de exportación de datos (para solicitar, sondear y obtener una cuadrícula).

## Cómo funciona la autenticación

La conexión usa **autenticación básica HTTP con una cuenta de servicio** en un pod clásico de EPM Cloud; no hay flujo de OAuth ni de token (los pods de OCI / Gen 2 con token de portador quedan fuera del alcance). Cuando se establece un **Dominio de identidad**, PlaidCloud compone el inicio de sesión como `identitydomain.username` (el dominio, un punto y luego el nombre de usuario); si deja en blanco el dominio de identidad, o si su nombre de usuario ya contiene un punto, el nombre de usuario se envía tal cual. Dirija la conexión a una cuenta de servicio de integración dedicada con acceso de lectura a las aplicaciones y los segmentos de punto de vista que extraerán sus usuarios de autoservicio.

## Configuración

| Campo | Obligatorio | Descripción |
|---|---|---|
| Nombre | Sí | Nombre para mostrar de esta conexión. |
| URL de EPM Cloud | Sí | La URL del pod o servicio de EPM Cloud, por ejemplo `https://planning-test-yourdomain.epm.us2.oraclecloud.com`. |
| Dominio de identidad | No | El dominio de identidad de EPM Cloud. Si se establece, PlaidCloud lo antepone al nombre de usuario como `identitydomain.username` al iniciar sesión. |
| Nombre de usuario | Sí | El nombre de usuario de la cuenta de servicio de integración. |
| Contraseña | Sí | La contraseña de la cuenta de servicio. Se almacena cifrada. |
| Aplicación predeterminada | No | Una aplicación de FCCS predeterminada con la que se rellena de antemano el selector de punto de vista del paso. Cada paso puede reemplazarla. |

## Qué puede hacer con la conexión

- **Obtener un segmento ad hoc por cuenta propia.** Cree un punto de vista (POV), es decir, la aplicación más las dimensiones de FCCS, en el formulario del paso, haga clic en Ejecutar y se crea automáticamente una tabla de resultados. Consulte [HFM/FCCS: leer datos (ad hoc)](/es/reference/workflow-steps/oracle-epm/hfm-fccs-read/).
- **Evitar la solicitud al equipo.** El segmento se ejecuta con la cuenta de servicio de la conexión, de modo que un usuario de finanzas obtiene los datos por sí mismo en lugar de esperar a un administrador de HFM.
- **Almacenar en caché las extracciones repetidas.** Si se vuelve a solicitar el mismo POV y la misma fecha de corte, se devuelve al instante la copia ya cargada en lugar de volver a consultar FCCS.
- **Controlar quién ve qué entidades.** La tabla cargada está **preparada para la seguridad a nivel de fila**: un administrador puede declarar Acceso a filas en la columna `Entity` para que los usuarios de autoservicio solo vean las entidades a las que tienen derecho. Esto se gestiona bajo el control del administrador y no es automático; consulte la referencia del paso.
- **Programar una carga recurrente.** Habilite **Destino vinculado** para promover un segmento ad hoc a una tabla persistente que crece de forma aditiva y combina en lugar de sobrescribir, de modo que el mismo paso colocado en un flujo de trabajo programado se convierte en una carga recurrente nocturna.

## Descubrimiento de metadatos

En los pods de FCCS compatibles, el formulario del paso descubre en vivo la lista de miembros de cada dimensión a partir de los metadatos de la aplicación en cuanto elige una conexión y una aplicación, de modo que el selector de POV ofrece miembros reales entre los que elegir (vuelve a descubrirlos cada vez que cambia alguno de los dos). En los pods más antiguos que no exponen el punto de conexión de metadatos, el descubrimiento no devuelve nada y el selector pasa a la entrada manual: usted escribe los nombres de los miembros a mano, y un punto de vista guardado siempre se conserva al reabrirlo. La extracción funciona igual en ambos casos.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| Solo lectura | El conector extrae datos de FCCS. No escribe datos de consolidación, no ejecuta consolidaciones ni contabiliza de vuelta. |
| Delimite la dimensión de entidad | Una extracción sin delimitar (sin selección de `Entity`) puede bloquear la aplicación de FCCS durante mucho tiempo mientras se ejecuta el trabajo de exportación. Mantenga acotada la selección de entidades. |
| Miembros manuales en pods más antiguos | Cuando un pod no expone el punto de conexión de metadatos, las listas de miembros no se rellenan automáticamente; escriba los nombres de los miembros a mano. |
| La seguridad a nivel de fila la gestiona el administrador y no es automática | La tabla cargada se puede controlar con Acceso a filas, pero un administrador debe publicar, declarar la columna `Entity`, aprobar la primera escritura controlada y conciliar. Hasta que lo haga, la tabla no se filtra. |

## Temas relacionados

- [Extraer de HFM / FCCS (guía)](/es/guides/connections/hfm-fccs/) — crear la conexión, crear un POV, ejecutarlo, almacenarlo en caché, controlarlo y programarlo.
- [HFM/FCCS: leer datos (ad hoc)](/es/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — la referencia de campos del paso.
- [Administrar grupos de seguridad y asignaciones](/es/administration/access/managing-security-groups-and-assignments/) — cómo Acceso a filas controla la tabla cargada.
- [Crear y administrar una conexión](/es/guides/connections/create-connection/)
