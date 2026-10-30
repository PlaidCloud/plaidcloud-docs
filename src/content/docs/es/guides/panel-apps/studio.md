---
title: Panel Studio
description: Cree, edite, obtenga una vista previa y publique aplicaciones Panel sin salir de PlaidCloud; luego restaure una versión anterior, consulte el uso y la velocidad de la aplicación, configure alertas y resúmenes, publíquela en la galería y fíjela en Inicio.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio es el editor de aplicaciones Panel dentro de PlaidCloud. Muestra los archivos de la aplicación junto a un editor, compila una vista previa privada que usted puede abrir y publica la aplicación cuando está listo. No necesita un repositorio git para empezar.

## Abrir Panel Studio

- En el tablero **Inicio** de un proyecto, elija **Open in Studio** en una aplicación Panel.
- En **Mis aplicaciones Panel**, elija **Open in Studio** en la fila de una aplicación.

Para iniciar una aplicación nueva, elija **Create app** en cualquiera de los dos lugares.

## Crear una aplicación

El cuadro de diálogo **Create app** le permite comenzar desde uno de cinco lugares:

| Comenzar desde | Qué obtiene |
|---|---|
| **En blanco** | Una aplicación mínima con un `app.py` y un `requirements.txt`. |
| **Tabla** | Una aplicación creada sobre la tabla que elija. |
| **Vista** | Lo mismo, creada sobre una vista del proyecto. |
| **Plantilla** | Una aplicación ya hecha del [kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/#empezar-desde-una-plantilla). |
| **Desde la galería** | Una copia de una aplicación que su espacio de trabajo ha publicado en la [galería de aplicaciones](/es/guides/panel-apps/gallery/). |

Dé un nombre a la aplicación, elija su **Proyecto** y elija **Crear**. Studio abre la nueva aplicación con sus archivos enumerados a la izquierda.

## Editar

Elija un archivo de la lista para editarlo en el editor. Enumere sus dependencias de Python en `requirements.txt`, un paquete por línea. Se instalan cuando la aplicación se compila.

Elija **Ask Weave** para que Weave escriba o modifique la aplicación por usted. Consulte [Cree aplicaciones Panel con Weave](/es/guides/panel-apps/build-with-weave/).

## Guardar, obtener una vista previa y publicar

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Guardar conserva un borrador que solo usted puede ver. La vista previa compila una copia privada del borrador para el editor. Publicar reemplaza la aplicación en vivo después de que usted confirma." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Guardar</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">solo borrador</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Vista previa</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">solo para el editor</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publicar</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">la aplicación en vivo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Sus ediciones llegan a los visualizadores solo cuando usted publica.</figcaption>
</figure>

### Guardar

**Guardar** almacena sus cambios como un borrador. La aplicación en vivo no cambia, y nadie más ve el borrador.

### Vista previa

**Vista previa** compila su borrador guardado como una copia privada y la abre. Solo los editores de la aplicación pueden abrir una vista previa.

- Una vista previa se elimina después de 24 horas sin que se guarde.
- Un espacio de trabajo puede tener hasta 10 vistas previas a la vez.
- Guarde de nuevo y elija **Vista previa** para ver sus últimas ediciones.

### Publicar

**Publicar** reemplaza la aplicación en vivo con su borrador guardado. Requiere permiso de edición sobre el proyecto de la aplicación, y Studio le pide que confirme primero.

Si otra persona publicó un cambio después de que usted abrió la aplicación, Studio informa de un conflicto en lugar de sobrescribir su trabajo. Vuelva a cargar la aplicación, traslade sus ediciones y publique de nuevo.

## Estado y errores de compilación

La pestaña **Crear** muestra el estado de la última compilación y se actualiza mientras se ejecuta. Cuando una compilación falla, la pestaña enumera cada error con su archivo y número de línea, para que pueda ir directamente a la línea. Los problemas de dependencias en `requirements.txt` incluyen una sugerencia de corrección.

Los errores y las advertencias también se marcan en sus líneas en el editor, de modo que ve el problema donde está.

Para saber qué significa cada estado una vez publicada la aplicación, consulte [Uso de una aplicación Panel](/es/guides/panel-apps/using/#estado-de-compilación-aplicaciones-de-servidor).

## Historial y restauración

La pestaña **Historial** enumera cada versión publicada de la aplicación, de la más reciente a la más antigua, con su estado de compilación. Elija **Cargar más** para ver las anteriores.

Para volver a una versión anterior, elija **Restaurar** en ella y confirme. La versión restaurada pasa a ser la aplicación en vivo y se vuelve a compilar. Su borrador sin guardar no se pierde: permanece en el borrador y entra en vivo sobre la versión restaurada la próxima vez que publique. Si la aplicación ya coincide con esa versión, Studio lo indica y no cambia nada. Si alguien publicó mientras usted restauraba, Studio no restaura nada y le pide que lo intente de nuevo.

## Análisis

La pestaña **Análisis** muestra cómo usa la gente la aplicación y con qué rapidez responde. Elija los últimos 7, 14 o 30 días.

| Sección | Qué muestra |
|---|---|
| **Vistas por día** | Cuántas veces se abrió la aplicación cada día. |
| **Carga de página** | El tiempo de carga mediano y el tiempo que el 95 por ciento de las cargas mejora, a partir de las cargas de página del período. |
| **Consultas más lentas** | Las consultas que más tardaron, con la frecuencia con que se ejecutaron y sus tiempos mediano, del extremo lento y más lento. |
| **Errores** | Qué salió mal en el período, por tipo de error y por dónde de la aplicación ocurrió. |

Cuando un período contiene más actividad de la que Análisis puede leer, indica que las cifras son parciales. Cuando las cargas de página superan el [presupuesto de rendimiento](/es/guides/panel-apps/app-kit/#presupuestos-de-rendimiento) de la aplicación, Análisis le avisa cuántas lo hicieron y qué consultas fueron lentas. Análisis nunca muestra los datos que devolvió una consulta ni los nombres de las personas que abrieron la aplicación.

Ambas pestañas requieren que la aplicación esté asignada a un proyecto; una aplicación sin asignar muestra un aviso para asignarla.

## Alertas y resúmenes

Elija **Alerts & Digests** para configurar notificaciones que vigilan un número de los datos de la aplicación y le avisan cuando supera un límite, o que envían un resumen según una programación. Consulte [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/).

## Publicar una aplicación en la galería

Elija **Gallery…** para publicar la aplicación como una plantilla a partir de la cual cualquier persona que pueda ver su proyecto puede crear su propia aplicación, o para quitarla de la galería. Consulte [La galería de aplicaciones](/es/guides/panel-apps/gallery/).

## Fijar en Inicio

Elija **Pin to Home** para agregar la aplicación al tablero **Inicio** del proyecto, y **Unpin from Home** para quitarla.

## Eliminar una aplicación

Eliminar una aplicación Panel le pide que confirme primero. En **Mis aplicaciones Panel**, use el icono de **menos** en la fila de la aplicación. Anular la publicación también le pide que confirme.

## Siguientes pasos

- [Cree aplicaciones Panel con Weave](/es/guides/panel-apps/build-with-weave/): describa la aplicación y apruebe el cambio exacto.
- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): los componentes que usan los inicios de Studio con tabla, vista y plantilla.
- [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/): notifique a las personas cuando un número supere un límite, o según una programación.
- [La galería de aplicaciones](/es/guides/panel-apps/gallery/): comparta una aplicación como punto de partida para otros.
- [Uso de una aplicación Panel](/es/guides/panel-apps/using/): registros, uso y recompilaciones después de publicar.
