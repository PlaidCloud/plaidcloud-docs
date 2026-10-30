---
title: "HFM/FCCS: leer datos (ad hoc)"
description: "Obtenga por su cuenta un segmento de datos de Oracle FCCS creando un punto de vista en el formulario del paso: la cuadrícula devuelta se carga automáticamente como una tabla, las extracciones repetidas se almacenan en caché, la columna Entity está lista para la seguridad a nivel de fila y un destino vinculado opcional lo convierte en una carga periódica programada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## Descripción

Lee un segmento de datos ad hoc de Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) a través de su [conexión de HFM/FCCS](/es/guides/connections/hfm-fccs/), mediante un **punto de vista (POV)** en lugar de escribir una consulta. Un usuario de finanzas elige una aplicación, crea un POV a partir de las dimensiones de FCCS y ejecuta el paso; la cuadrícula devuelta se carga automáticamente como una tabla del proyecto (esquema en la lectura: la tabla se crea a partir de las columnas de la cuadrícula). Parece una consulta en vivo, pero internamente el paso envía un trabajo de exportación a FCCS, lo **sondea** hasta que termina y luego obtiene y carga el resultado, de modo que un segmento de larga duración no bloquea y no se necesita ningún ticket al equipo de HFM.

Este paso aparece en el menú de pasos bajo **Oracle EPM (HFM/FCCS)**.

:::note[Acote la dimensión de entidad]
Mantenga acotada la selección de **Entidad**: una extracción sin acotar puede bloquear la aplicación de FCCS durante mucho tiempo mientras se ejecuta el trabajo de exportación.
:::

## Configuración

### Origen y destino

| Campo | Obligatorio | Notas |
|---|---|---|
| Conexión de HFM/FCCS | Sí | La [conexión de HFM/FCCS](/es/guides/connections/hfm-fccs/) por la que se lee. |
| Entorno | Sí | El entorno de la conexión. |
| Aplicación | Sí | La aplicación de FCCS de la que se lee. De forma predeterminada es la Aplicación predeterminada de la conexión, si se ha definido una. Al elegir la aplicación se activa el descubrimiento de miembros en vivo para el POV. |
| Tabla de destino | Sí | La tabla del proyecto en la que se carga la cuadrícula devuelta. |

### Punto de vista

Cree el segmento a partir de las dimensiones de FCCS. En los pods compatibles, las listas de miembros se rellenan automáticamente mediante el descubrimiento de metadatos en vivo una vez elegidas una conexión y una aplicación; en los pods más antiguos, usted escribe los nombres de los miembros manualmente.

| Dimensión | Obligatoria | Notas |
|---|---|---|
| Escenario | Sí | |
| Año | Sí | |
| Período | Sí | |
| Entidad | Acotada | Debe indicar un segmento acotado: el formulario rechaza una selección vacía, “all” o una selección de más de 500 miembros. Manténgala acotada para que la exportación no bloquee la aplicación. |
| Cuenta | No | |
| Custom1–Custom4 | No | Las dimensiones personalizadas de la aplicación. |
| ICP | No | Intercompañía. |
| Vista | No | |
| Valor | No | |

Una dimensión opcional sin definir no aplica ningún filtro en ese eje (se usa el miembro predeterminado de FCCS).

### Destino vinculado

Desactivado de forma predeterminada: cada ejecución carga un segmento ad hoc que sobrescribe la tabla de destino.

| Campo | Notas |
|---|---|
| Destino vinculado (carga periódica programada) | Cuando está marcado, el destino pasa a ser una tabla **persistente**: el paso se combina con ella mediante un upsert por conjunto de claves en lugar de sobrescribirla, y el esquema crece de forma aditiva cuando una cuadrícula posterior trae columnas nuevas (una columna nueva genera una advertencia, nunca un fallo). Colocar el paso en un flujo de trabajo programado da entonces una carga periódica que acumula en lugar de borrar. |
| Columnas clave | Se habilita solo con Destino vinculado activado. Columnas separadas por comas que forman la clave de combinación (por ejemplo `Entity, Account`). **Déjelo vacío** para usar como clave de combinación las columnas de dimensión del POV presentes en la cuadrícula cargada. |

## Cómo funciona

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="El paso envía un trabajo de exportación a FCCS, lo sondea hasta que termina, obtiene la cuadrícula y la carga como una tabla; un punto de vista repetido se sirve desde la tabla en caché." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Enviar trabajo</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Sondear</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Obtener cuadrícula</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cargar tabla</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">mientras se ejecuta…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">POV repetido</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">servido desde la caché</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Una ejecución envía un trabajo de exportación, lo sondea, obtiene la cuadrícula y carga una tabla. El mismo punto de vista solicitado de nuevo se sirve desde la copia ya cargada.</figcaption>
</figure>

Mientras se ejecuta el trabajo, el paso muestra un estado de sondeo. Cuando termina la carga, la tabla se crea a partir de las columnas de la cuadrícula: no hay que definir ningún esquema de antemano.

## Almacenamiento en caché

El mismo POV solicitado de nuevo se **sirve desde la tabla ya cargada**, al instante, en lugar de volver a enviar la exportación a FCCS. Una ejecución se identifica por la aplicación, la tabla de destino, el punto de vista y una etiqueta **as-of** (valor predeterminado `latest`); una repetición que se resuelve en un segmento ya cargado informa de que la tabla se dejó en su lugar en vez de reescribirla. Cambie la etiqueta as-of cuando quiera forzar una extracción nueva del mismo POV.

## Seguridad a nivel de fila

El eje de entidad de la cuadrícula cargada se normaliza a una columna llamada exactamente **`Entity`**, de modo que la tabla está **lista para la seguridad a nivel de fila**: un administrador puede gobernarla con [Acceso a filas](/es/administration/access/managing-security-groups-and-assignments/) para que los usuarios de autoservicio solo vean las entidades a las que tienen derecho.

Esto está **gobernado bajo control del administrador, no es automático**. Como la extracción se ejecuta con la cuenta de servicio de la conexión, PlaidCloud no permite que el paso declare su propia seguridad. Un administrador sigue el flujo estándar de Acceso a filas:

1. **Publicar** la tabla cargada para informes.
2. **Declarar** la columna `Entity` como atributo de gobierno (denegación predeterminada).
3. **Aprobar** la primera escritura gobernada.
4. **Conciliar** para que los permisos surtan efecto.

Hasta que un administrador lo haga, la tabla no se filtra. Consulte [Administrar grupos de seguridad y asignaciones](/es/administration/access/managing-security-groups-and-assignments/).

## Límites de capacidad

| Limitación | Qué significa |
|---|---|
| Solo lectura | Extrae un segmento de FCCS. No escribe datos de consolidación, no ejecuta consolidaciones ni contabiliza de vuelta. |
| Entidad acotada obligatoria | El formulario rechaza una selección de entidad vacía, “all” o de más de 500 miembros, y un único miembro agregado aún puede expandirse en el servidor: mantenga acotado el segmento. |
| Miembros manuales en pods antiguos | Donde un pod no expone el punto de conexión de metadatos, las listas de miembros no se rellenan automáticamente; escriba los nombres de los miembros a mano. |
| La seguridad a nivel de fila la gobierna el administrador | La columna `Entity` está lista para la seguridad a nivel de fila, pero un administrador debe publicar, declarar, aprobar la primera escritura y conciliar antes de que la tabla se filtre. |

## Relacionado

- [Extraer de HFM / FCCS (guía)](/es/guides/connections/hfm-fccs/): el tutorial completo.
- [Conector de HFM / FCCS](/es/reference/connectors/rest/hfm-fccs/): referencia de los campos de la conexión.
- [Pasos de Oracle EPM (HFM / FCCS)](/es/reference/workflow-steps/oracle-epm/)
- [Administrar grupos de seguridad y asignaciones](/es/administration/access/managing-security-groups-and-assignments/)
