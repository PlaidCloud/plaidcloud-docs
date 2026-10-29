---
title: "Essbase: consultar cubo"
description: Ejecute una consulta MDX en vivo contra un cubo de Oracle Essbase y deposite la cuadrícula de resultados en una tabla del flujo de trabajo, con columnas derivadas de la cuadrícula y con acceso a filas aplicado al resultado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## Descripción

El paso **Essbase: consultar cubo** ejecuta un `SELECT` de MDX contra un cubo de Oracle Essbase y escribe la cuadrícula devuelta en una tabla de destino. Es una **auténtica consulta en vivo**: el paso envía el MDX y lee la cuadrícula resultante de forma síncrona, de modo que cada ejecución refleja las cifras actuales del cubo. No es una extracción ni un sondeo: no hay ningún trabajo de preparación que esperar ni ninguna instantánea que quede obsoleta entre ejecuciones.

Úselo para traer un segmento concreto de un cubo (un conjunto de cuentas por período, una comparación de escenarios, un conjunto de inductores para una asignación) a una tabla de PlaidCloud que luego pueda transformar, combinar o usar en informes junto con el resto de sus datos.

## Requisitos previos

- Una [conexión de Oracle Essbase](/es/reference/connectors/erp/oracle-essbase/) que apunte a Essbase 21c o posterior, o a Oracle Analytics Cloud (OAC), con una cuenta de servicio que pueda leer la aplicación y el cubo que desea consultar.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Flujo desde una conexión de Essbase, pasando por la aplicación y el cubo elegidos, una consulta MDX y la cuadrícula devuelta, hasta una tabla de destino." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Conexión</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Aplicación</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ Cubo</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Cuadrícula</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Tabla</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">El MDX se ejecuta en vivo contra el cubo; la cuadrícula devuelta se deposita en la tabla de destino con columnas derivadas de la propia cuadrícula.</figcaption>
</figure>

## Configuración

- **Conexión**: una conexión de Oracle Essbase. El acceso directo de edición junto al selector abre el editor de conexiones para verla o editarla.
- **Aplicación**: la aplicación de Essbase que se consulta. El selector enumera las aplicaciones que puede ver la cuenta de servicio de la conexión; si la conexión define una aplicación predeterminada, aparece preseleccionada.
- **Cubo (base de datos)**: el cubo de la aplicación elegida contra el que se consulta.
- **MDX**: la instrucción `SELECT` de MDX que se ejecuta. Créela con la selección guiada de miembros o escríbala directamente (véase más abajo).
- **Tabla de destino**: la tabla en la que se escribe la cuadrícula devuelta.

## Creación de la consulta

Puede generar el MDX de dos maneras:

- **Selección guiada de miembros.** Explore las dimensiones y los miembros del cubo y elija lo que va en columnas y en filas; el paso arma el MDX por usted. Los miembros se cargan un nivel cada vez a medida que los expande, de modo que un esquema grande sigue respondiendo con rapidez.
- **MDX sin procesar.** Escriba o pegue directamente un `SELECT` de MDX: es la vía alternativa para todo lo que el selector guiado no cubre, como miembros calculados, funciones u operadores de conjuntos.

Ambas vías producen el mismo valor de `MDX` que ejecuta el paso; el selector guiado es un punto de partida que siempre puede editar a mano.

## Opciones

| Campo | Valor predeterminado | Notas |
|---|---|---|
| Suprimir celdas #Missing | Desactivado | En el servidor: descarta las celdas `#Missing` y otras estructuralmente irrelevantes antes de que crucen la red. Es seguro: nunca descarta un cero contabilizado. |
| Suprimir también las celdas con cero (con pérdida) | Desactivado | Un filtro independiente y opcional que también descarta cualquier celda cuyo valor ya sea exactamente `0`, una vez obtenida. **Con pérdida**: un cero contabilizado es un hecho real en un cubo de planificación, no ausencia de datos; actívelo solo si desea específicamente excluir los ceros del resultado. |
| Límite de filas | 250,000 | Limita el número de filas devueltas. Déjelo en blanco para usar el límite predeterminado de 250,000; súbalo o bájelo de forma explícita. Una consulta que supera el límite se rechaza en lugar de truncarse en silencio: acote la consulta (agregue un segmentador, `NON EMPTY` o un conjunto de miembros más ajustado) o aumente el Límite de filas, y vuelva a intentarlo. |

## Vista previa

Antes de guardar, **Vista previa** ejecuta el MDX actual contra el cubo y muestra las columnas devueltas y las primeras filas: una comprobación rápida de que la consulta tiene la forma esperada, con independencia del Límite de filas con el que esté configurado el propio paso.

## Resultados y esquema en lectura

La cuadrícula que devuelve Essbase se escribe en la tabla de destino con sus **columnas derivadas de la cuadrícula devuelta** (esquema en lectura). No es necesario declarar de antemano una lista de columnas:

- Los nombres de columna proceden de las filas de encabezado de la cuadrícula. Una celda de encabezado que no abarca nada (la esquina situada sobre las etiquetas de fila) pasa a ser `column_1`, `column_2`, etc.; los nombres duplicados se vuelven únicos con un sufijo numérico.
- Una columna cuyas celdas de datos son todas numéricas se tipifica como numérica; todo lo demás se tipifica como texto. Las celdas vacías de Essbase se depositan como nulos.
- Las etiquetas de miembros y de alias de la cuadrícula proceden de la tabla de alias configurada en la conexión, aplicada de forma coherente en cada ejecución, y no del valor predeterminado por sesión de Essbase, que podría mostrar texto de etiqueta distinto según quién hubiera iniciado sesión cuando se ejecutó la consulta.

Como la forma sigue a la consulta, cambiar lo que el MDX coloca en las columnas cambia las columnas de la tabla en la siguiente ejecución; téngalo en cuenta en los pasos posteriores que hagan referencia a nombres de columna concretos.

## Acceso a filas

La [seguridad a nivel de fila](/es/administration/access/managing-security-groups-and-assignments/#administración-del-acceso-a-filas) se aplica a la tabla depositada exactamente igual que a cualquier otra tabla de PlaidCloud. La gobernanza se aplica sobre el resultado que escribe el paso, de modo que un lector con una restricción de filas solo ve las filas que permite su grupo de seguridad: la consulta se ejecuta con la cuenta de servicio de la conexión, pero la tabla que produce se rige como el resto de sus datos.

## Ejemplo

Este MDX coloca dos medidas en las columnas y dos productos en las filas:

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

Al ejecutarlo contra un cubo que devuelve esas cuatro cifras, se deposita una tabla como esta:

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

La columna de etiquetas de fila no tiene encabezado en la cuadrícula, así que pasa a ser `column_1` (texto); `Sales` y `COGS` son completamente numéricas y se depositan como columnas numéricas.

## Relacionado

- [Conexión con Oracle Essbase (guía)](/es/guides/connections/essbase/): cree la conexión y elabore una consulta.
- [Conector de Oracle Essbase](/es/reference/connectors/erp/oracle-essbase/): referencia de los campos de la conexión.
- [Essbase: leer dimensión](/es/reference/workflow-steps/essbase/essbase-dimension-read/): cargue el esquema de una dimensión de Essbase en una dimensión de PlaidCloud, en nube directa.
- [Pasos de Oracle Essbase](/es/reference/workflow-steps/essbase/)
- [Solicitud REST](/es/reference/workflow-steps/general/rest-request/): el paso de uso general para otras solicitudes HTTP en vivo.
