---
title: Configurar una asignación
description: Configure una asignación de PlaidCloud, incluidos los datos de origen, los datos de inductores, la asignación de destinos, los métodos de asignación y las opciones de procesamiento.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/configure-an-allocation.md
---

## Finalidad

Las asignaciones permiten desglosar valores (normalmente costos) a un nivel más granular aplicando un inductor. Las asignaciones se usan para múltiples propósitos, entre ellos el **costeo basado en actividades**, el **contracargo de servicios compartidos y de TI**, el cálculo del costo totalmente cargado de producir y suministrar un bien o servicio a los clientes, etc. Son una herramienta fundamental para el análisis financiero y una piedra angular de las operaciones de informes de gestión, como la **rentabilidad de clientes y productos**. También son una construcción útil para establecer y administrar precios de transferencia intercompañía globales de bienes y servicios.

## Configurar la transformación de asignación

En la práctica, las asignaciones se configuran en PlaidCloud de forma similar a otras transformaciones de datos, como las combinaciones y las búsquedas. Deben definirse cuatro parámetros de configuración para que una transformación de asignación se ejecute correctamente.

1. **Especificar los datos previos a la asignación**: especifique la tabla de datos previos a la asignación en la sección **Tabla de valores que asignar** de la transformación de asignación.
2. **Especificar los datos de inductores**: los datos de inductores servirán de base para las proporciones que se usan en la asignación. Elija la tabla de datos de inductores en la sección **Tabla de datos de inductores** de la transformación de asignación.
3. **Especificar la tabla de resultados**: los datos posteriores a la asignación deben almacenarse en una tabla. Especifique la tabla en la sección **Tabla de resultados de la asignación** de la sección de resultados de la transformación.
4. **Especificar la dimensión de asignación**: las asignaciones requieren una dimensión de asignación, cuya finalidad es indicar cómo se asignará cada registro o conjunto de registros de los datos previos a la asignación. Especifique la dimensión de asignación en la sección **Jerarquía de la dimensión de asignación** de la transformación de asignación.

Además de esos cuatro, las dos pestañas de asignación de columnas necesitan **Roles** de columna definidos para que el paso se guarde: una columna **Valor que asignar** en el **Mapa de origen de la asignación**, y columnas **Valor de división**, **Relación de origen (denominador)** y **Destino de la asignación (numerador)** en el **Mapa de datos de inductores**. PlaidCloud lo comprueba al guardar e indica lo que falta; consulte [Solución de problemas de asignaciones](/es/guides/allocations/results/troubleshooting-allocations/#por-qué-no-se-puede-guardar-un-paso-de-asignación).

## Conceptos clave

La suma de los valores de un conjunto de datos asignado debe coincidir con la de los datos de origen previos a la asignación

Las asignaciones están disponibles en PlaidCloud como una opción de transformación. Para configurar una asignación, primero defina las asignaciones y luego configure una transformación de asignación que las use para asignar los registros entrantes con una tabla de inductores específica.

Las asignaciones son dimensiones especiales. Se accede a ellas en la sección Dimensiones de un proyecto de PlaidCloud.

Para configurar una dimensión de asignación, siga estos pasos:

1. Desde la pantalla del proyecto, vaya a la pestaña Dimensiones
2. Cree una dimensión nueva
