---
title: PlaidXL
description: Use el complemento PlaidXL de Excel para iniciar sesión en su espacio de trabajo de PlaidCloud, traer tablas de proyecto y jerarquías de dimensiones a las hojas de cálculo, actualizarlas a petición y crear informes dinámicos con las funciones personalizadas de PlaidXL.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL es el complemento de PlaidCloud para Microsoft Excel. Conecta un libro con su espacio de trabajo de PlaidCloud para que sus modelos e informes lean de tablas y dimensiones de proyecto confiables, y no de una copia que queda obsoleta la próxima vez que se ejecuta un flujo de trabajo.

Puede trabajar con PlaidXL de dos maneras, y la mayoría de los libros usan ambas:

- **El panel de tareas**: explore sus proyectos, elija una tabla o dimensión, seleccione columnas y filtros, y recupere los datos en una hoja de cálculo. **Refresh All Tables** obtiene los datos actuales de todas las tablas que ha recuperado.
- **Funciones personalizadas**: fórmulas como `=PLAIDXL.TABLE.GET_TABLE("Sales")` y `=PLAIDXL.CELL(...)` que leen datos de PlaidCloud directamente en las celdas. Úselas para listar tablas y dimensiones, distribuir una jerarquía y calcular valores acumulados para un informe.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel contiene el panel de tareas de PlaidXL y las funciones personalizadas de PlaidXL. Ambos envían solicitudes, con la sesión iniciada como usted, a un proyecto de su espacio de trabajo de PlaidCloud, que devuelve filas de tablas, jerarquías de dimensiones y valores acumulados a las celdas de la hoja de cálculo." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Libro de Excel</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Panel de tareas de PlaidXL</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">explorar, filtrar, recuperar, actualizar</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Funciones PLAIDXL.*</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tablas, jerarquías, valores en celdas</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Espacio de trabajo de PlaidCloud</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Proyecto</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tablas</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">dimensiones y jerarquías</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">sesión como usted</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">filas, nodos, valores</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">El panel de tareas y las funciones personalizadas leen del proyecto que usted selecciona, con sus propios permisos de PlaidCloud.</figcaption>
</figure>

PlaidXL lee datos. No escribe nada de vuelta en PlaidCloud, por lo que editar una hoja recuperada nunca modifica una tabla del proyecto.

## Requisitos

- Excel para Microsoft 365, o Excel 2021 o posterior, en Windows o Mac. La pestaña PlaidCloud de la cinta de opciones y el panel de tareas se ejecutan en Excel de escritorio.
- Una cuenta de PlaidCloud en al menos un espacio de trabajo y acceso a los proyectos que desea leer. PlaidXL muestra solo los proyectos, tablas y dimensiones que su cuenta ya puede ver en PlaidCloud.

## Temas

- [Instalar](/es/reference/cli/plaidxl/install/): agregue PlaidXL a Excel y abra el panel de tareas
- [Iniciar sesión](/es/reference/cli/plaidxl/connect/): conéctese a su espacio de trabajo, cierre sesión y cambie de espacio de trabajo
- [Trabajar con tablas y dimensiones](/es/reference/cli/plaidxl/retrieve/): elija un proyecto, filtre una tabla, recupérela en una hoja y actualícela
- [Funciones personalizadas](/es/reference/cli/plaidxl/functions/): todas las funciones `PLAIDXL`, sus argumentos y lo que devuelven
- [Crear un informe con funciones personalizadas](/es/reference/cli/plaidxl/build-a-report/): distribuya una jerarquía y rellénela con valores acumulados
- [La cinta de opciones de PlaidCloud](/es/reference/cli/plaidxl/ribbon/): comandos para actualizar, desplegar y sanear
- [Solución de problemas](/es/reference/cli/plaidxl/troubleshooting/): soluciones para los problemas más comunes

¿Es la primera vez que usa PlaidXL? El tutorial [Trabajar en Excel con PlaidXL](/es/get-started/tutorials/excel-with-plaidxl/) le guía desde la instalación del complemento hasta un primer informe en unos 20 minutos.

## Temas relacionados

- [Proyectos](/es/guides/projects/): qué contiene un proyecto y cómo encontrar uno
- [Tablas y vistas](/es/guides/data/tables-views/): las tablas que recupera PlaidXL
- [Uso de dimensiones](/es/guides/dimensions/dimensions/): las jerarquías que PlaidXL distribuye y acumula
