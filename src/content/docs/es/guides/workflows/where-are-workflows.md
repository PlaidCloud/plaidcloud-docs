---
title: Dónde están los flujos de trabajo
description: Navegue hasta los flujos de trabajo de PlaidCloud dentro de sus proyectos y adminístrelos con la interfaz de flujos de trabajo y las herramientas de navegación del proyecto.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/where-are-workflows.md
---

Los flujos de trabajo viven dentro de los proyectos. Para encontrarlos:

1. En el menú superior, abra **Proyectos**.
2. Haga clic en el proyecto que contiene los flujos de trabajo que busca.
3. Cambie a la pestaña **Flujos de trabajo**.

Verá todos los flujos de trabajo del proyecto, organizados en una jerarquía con aspecto de carpetas.

## Qué verá de cada flujo de trabajo

- **Estado**: en ejecución, completado con normalidad o terminado con una advertencia o un error
- Marcas de tiempo de **Creado** y de **última actualización**, además de los nombres de las personas responsables
- **Organización en carpetas**: los flujos de trabajo se pueden agrupar en carpetas anidadas para administrarlos más fácilmente en proyectos grandes

Haga doble clic en un flujo de trabajo para abrir el **Explorador de flujos de trabajo**, donde puede ver los pasos, ejecutar todo el flujo de trabajo, ejecutar un solo paso o elegir un rango.

## Por qué puede que un flujo de trabajo no sea visible

Los flujos de trabajo que puede ver dependen de dos cosas:

- **Acceso al proyecto**: el administrador de su espacio de trabajo le concede acceso a proyectos concretos. Si espera ver un proyecto y no lo ve, pida a un propietario del proyecto que le añada.
- **Rol de visualización**: dentro de un proyecto se le asigna uno de tres roles:
  - **Arquitecto**: puede ver y editar todo
  - **Gerente**: puede ver y ejecutar flujos de trabajo, pero no modificarlos
  - **Explorador**: visibilidad limitada; algunos flujos de trabajo pueden estar ocultos

Si espera ver flujos de trabajo concretos y no los ve, puede que su rol los esté filtrando. Un Arquitecto del proyecto puede confirmar lo que debería ver.

Su rol también decide si puede cambiar un paso. Si puede abrir un flujo de trabajo pero no modificarlo, el formulario del paso se abre en modo de solo lectura (sus campos están deshabilitados y su botón **Guardar** está oculto), de modo que puede leer la configuración de un paso sin poder alterarla. Esto se aplica dondequiera que se abra el formulario: el icono de engranaje y el menú contextual de la tabla del flujo de trabajo, el lienzo visual, la cuadrícula **Pasos** del proyecto y el menú **Nuevo paso**.

## Cambios sin guardar en una ventana de paso

Una ventana de paso marca los cambios sin guardar con un **•** en su título. Al cerrar la ventana con **Esc**, la **X**, **Cancelar** o el botón de su pestaña, se pregunta **¿Descartar los cambios sin guardar?** para que una edición no se pierda por accidente. Elija **Descartar** para cerrar sin guardar, o vuelva atrás para seguir editando.

## Un paso cambió desde que lo abrió

**Guardar** en un formulario de paso nunca sobrescribe un cambio guardado después de que usted abriera el formulario, ya lo haya hecho Weave u otra persona. No se guarda nada: el formulario sigue abierto con sus cambios, y una advertencia titulada **Error al actualizar** dice *Este paso cambió desde que lo abrió. Recargue para ver la última versión; sus cambios sin guardar se perderán.* Elija **Recargar** para mostrar el paso tal como está ahora y vuelva a hacer sus cambios. Agregar o quitar una de las etiquetas del paso no cuenta como un cambio. Si otros guardados siguen llegando al paso mientras se escribe el suyo, un mensaje **Error al actualizar** dice *Este paso siguió cambiando mientras se guardaba. Inténtelo de nuevo.* y no se guarda nada; vuelva a guardar cuando se detengan.

Mediante la REST API, `GET /rest/v1/analyze/projects/{project_id}/transform/{step_id}` devuelve el paso con su `_etag`. Envíelo de vuelta como `if_match` en un `PUT` a la misma ruta, y un guardado sobre un cambio más reciente se rechaza con `412` y no se escribe nada. Sin él, prevalece el último guardado. Un `PUT` que otros guardados siguen adelantando se rechaza con `503` y el mismo *Este paso siguió cambiando mientras se guardaba. Inténtelo de nuevo.*, y no se escribe nada. Cuando un `PUT` incluye `labels` y solo ellas no se pudieron escribir, responde `503` con *El paso se guardó, pero sus etiquetas no: siguieron cambiando mientras se escribían. Vuelva a establecer las etiquetas.* Los asistentes de IA conectados mediante MCP obtienen la misma comprobación al pasar el `_etag` de `step_describe` como `if_match` a `step_upsert`.

## Pasos siguientes

- [Explorador de flujos de trabajo](/es/guides/workflows/workflow-explorer/): qué hacer dentro de un flujo de trabajo abierto
- [Crear un flujo de trabajo](/es/guides/workflows/create-workflow/): empezar uno nuevo
- [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/): ejecutarlo de principio a fin
