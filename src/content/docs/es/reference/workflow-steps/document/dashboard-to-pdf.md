---
title: Convert Dashboard to PDF
description: Renderice un panel de control de PlaidCloud a PDF en una cuenta de documentos, una vez por cada fila de un conjunto de datos de filtros, aplicando los valores de cada fila como filtros del panel de control.
sidebar:
  order: 22
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/dashboard-to-pdf.md
---

## Descripción

Renderiza un panel de control a PDF y escribe los archivos en una cuenta de documentos. Úselo para programar un panel de control: un paquete de cierre de mes, una distribución a personas que no inician sesión o una instantánea archivada de cómo se veían las cifras en un día determinado.

El paso renderiza una vez por cada fila de un conjunto de datos de filtros y aplica los valores de esa fila como filtros del panel de control, de modo que un solo paso puede generar un conjunto de PDF por región o por entidad en una única ejecución.

## Configuración

### Panel de control

El panel de control que se va a renderizar.

### Conjunto de datos de filtros

La tabla cuyas filas determinan los renderizados: un PDF por fila.

### Ruta de salida

La cuenta de documentos y la carpeta en las que se escriben los PDF.

### Opciones

- **Generación simultánea de PDF**: cuántos renderizados se ejecutan a la vez. El valor predeterminado es 8; redúzcalo si el panel de control es tan pesado que los renderizados en paralelo agotan el tiempo de espera.
- **Tiempo de espera de renderizado (segundos)**: aparece en la configuración del paso, pero el ejecutor de flujos de trabajo **no lo aplica actualmente**. Establecerlo no tiene ningún efecto por ahora.

### Filtros del panel de control

Los filtros propios del panel de control, cada uno con su **ID del filtro del panel de control**. Se leen del panel de control al rellenar la asignación.

### Asignación de columnas de origen

Las columnas del conjunto de datos de filtros y cómo se usa cada una. Utilice **Inspeccionar origen › Rellenar tabla de asignación** para leer las columnas y los filtros del panel de control; una columna con el mismo nombre que un filtro del panel de control se etiqueta como filtro de este. Si vuelve a rellenar, se conservan la **Clase** y la **Columna de filtro asignada** que ya haya establecido en una columna.

Establezca la **Clase** de cada columna:

- **Filtro de columna**: el valor de la columna establece el filtro del panel de control indicado en **Columna de filtro asignada**, que debe ser uno de los filtros del panel de control.
- **Nombre de archivo**: la columna proporciona el nombre de archivo de cada PDF. Solo una columna puede ser el Nombre de archivo. Si no hay ninguna, el paso muestra una advertencia y genera los nombres automáticamente.
- **Sin filtro**: la columna no se usa.

Al menos una columna debe ser un **Filtro de columna**.

## Qué se comprueba al guardar

Se rechaza guardar el paso, con indicación de la columna, cuando:

- Ninguna columna es un Filtro de columna con una Columna de filtro asignada — *Etiquete al menos una columna de origen como Filtro de columna, con la Columna de filtro asignada que establece.*
- Un Filtro de columna no tiene Columna de filtro asignada, o indica una que no figura entre los filtros del panel de control — *La Columna de filtro asignada 'Region' para la columna de origen 'region' no es uno de los filtros del panel de control.*
- Más de una columna es el Nombre de archivo — *Solo una columna de origen puede ser el Nombre de archivo; region y entity lo son.*
- Una columna de Filtro de columna o de Nombre de archivo no tiene tipo de datos — *La columna de origen 'region' no tiene tipo de datos; inspeccione el origen de nuevo para actualizarlo.* Algunos pasos guardados en el formulario del paso no tienen los tipos de sus columnas y fallan en cada ejecución hasta que se los restituye. Ejecute **Inspeccionar origen › Rellenar tabla de asignación** para restaurarlos; se conservan las etiquetas de Filtro de columna y Nombre de archivo.

## Relacionado

- [Pasos de documento](/es/reference/workflow-steps/document/)
- [Paneles de control (guía)](/es/guides/dashboards/)
- [Pasos de informe](/es/reference/workflow-steps/reports/)
