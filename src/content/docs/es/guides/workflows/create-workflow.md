---
title: Crear un flujo de trabajo (guía)
description: Cree un flujo de trabajo en PlaidCloud y elija su tipo (Estándar en serie, Estándar en paralelo o Avanzado (lienzo DAG)) para cargar, transformar y exportar datos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/create-workflow.md
---

Para crear un flujo de trabajo nuevo, necesita un proyecto existente. Si todavía no tiene uno, consulte [Administrar proyectos](/es/guides/projects/managing-projects/).

## Pasos

1. Abra el proyecto que debe contener el flujo de trabajo.
2. Cambie a la pestaña **Flujos de trabajo**.
3. Haga clic en **Flujo de trabajo nuevo** en la barra de herramientas.
4. Complete el formulario:
   - **Nombre**: breve y descriptivo (p. ej., “Cierre mensual — cargar valores reales”)
   - **Nota**: descripción más larga opcional para dar contexto
   - **Tipo de flujo de trabajo**: Estándar en serie (predeterminado), Estándar en paralelo o Avanzado (lienzo DAG). Consulte [Elegir un tipo de flujo de trabajo](#elegir-un-tipo-de-flujo-de-trabajo) más abajo.
   - **Activar flujo de trabajo de corrección en caso de error**: opcional; actívelo para elegir un flujo de trabajo de corrección (consulte [Acerca de los flujos de trabajo de corrección](#acerca-de-los-flujos-de-trabajo-de-corrección) más abajo).
5. Haga clic en **Crear**.

El flujo de trabajo aparece en la pestaña Flujos de trabajo y está listo para que le agregue pasos. Haga doble clic en él para abrir el [Explorador de flujos de trabajo](/es/guides/workflows/workflow-explorer/) y empezar a construir.

## Ver cuándo cambió por última vez una tabla de origen

En el formulario de un paso, un selector de tabla muestra debajo de la tabla seleccionada una línea atenuada **Última actualización** con la fecha y la hora, en su hora local, para que pueda saber de un vistazo si los datos están al día. Pase el cursor sobre la línea para ver el texto completo. La línea se oculta cuando la selección es dinámica o cuando la tabla nunca se ha actualizado.

## Elegir un tipo de flujo de trabajo

El **Tipo de flujo de trabajo** que elige al crear un flujo de trabajo determina cómo se organizan y se ejecutan sus pasos. De forma predeterminada es **Estándar en serie**, y lo establece desde el selector de tipo del formulario Flujo de trabajo nuevo.

| Tipo | Cómo se organizan y se ejecutan los pasos |
|------|--------------------------------|
| **Estándar en serie** | Los pasos se ejecutan desde la **lista de pasos**, uno a la vez y en orden. |
| **Estándar en paralelo** | Los pasos se ejecutan desde la **lista de pasos**, en paralelo cuando sus dependencias lo permiten. |
| **Avanzado (lienzo DAG)** | Los pasos se disponen en un **lienzo visual** y se ejecutan en orden de dependencia, con las ramas independientes ejecutándose en paralelo. El tipo avanzado también habilita puntos de interrupción, contenedores, ejecutar desde aquí, simulación y colaboración en tiempo real. |

Un cuarto tipo, **Macro** (un flujo de trabajo reutilizable y invocable con entradas y salidas declaradas), estará disponible próximamente y aparece en el selector como deshabilitado.

:::note
Un paso solo puede aparecer una vez en un flujo de trabajo. Se rechaza insertar, copiar, clonar o importar un paso en una posición que lo colocaría por segunda vez en un flujo de trabajo, y el mensaje indica el nombre del paso; así, no puede llegar a este estado en adelante. Si un flujo de trabajo anterior a esa corrección todavía tiene un paso en dos lugares, falla de inmediato en una ejecución **Estándar en serie** con un error que indica el nombre del paso duplicado, igual que en una ejecución **Estándar en paralelo** detenida en un paso final elegido (consulte [Ejecutar un rango de pasos en un flujo de trabajo](/es/guides/workflows/running-a-range-of-steps-in-a-workflow/)), ya que ejecutar hasta un punto final también se hace de forma secuencial. Una ejecución **Estándar en paralelo** hasta el final tolera el duplicado y lo ejecuta una sola vez. En cualquier caso, elimine el paso duplicado para reparar el flujo de trabajo: eliminar pasos nunca está restringido.
:::

Elija **Avanzado (lienzo DAG)** aquí si desea usar el [Diseñador visual de flujos de trabajo](/es/guides/workflows/advanced-workflows/) desde el principio. La elección no es permanente: más adelante puede promover un flujo de trabajo estándar con **Convertir a avanzado…** desde la lista de Flujos de trabajo.

## Acerca de los flujos de trabajo de corrección

Si el flujo de trabajo nuevo termina con un error, PlaidCloud puede ejecutar automáticamente un **flujo de trabajo de corrección** como respuesta. Esto resulta útil para:

- Enviar una notificación a un canal de Slack, una lista de distribución de correo electrónico o un webhook para que alguien investigue
- Activar un flujo de trabajo de reversión o limpieza que restaure un estado correcto conocido
- Registrar el fallo en una tabla de auditoría

Un flujo de trabajo de corrección es opcional. Puede dejarlo en blanco ahora y configurarlo después si lo necesita. El flujo de trabajo de corrección solo se activa ante fallos terminales, no ante advertencias de pasos individuales.

## Pasos siguientes

- [Explorador de flujos de trabajo](/es/guides/workflows/workflow-explorer/): agregue pasos a su flujo de trabajo nuevo
- [Flujos de trabajo avanzados](/es/guides/workflows/advanced-workflows/): elija un tipo de flujo de trabajo y construya en el lienzo visual
- [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/): ejecute el flujo de trabajo una vez que tenga pasos
- [Administrar errores de pasos](/es/guides/workflows/managing-step-errors/): depuración de fallos
