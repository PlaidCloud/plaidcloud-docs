---
title: Panel Studio
description: Cree, edite, previsualice y publique aplicaciones Panel sin salir de PlaidCloud; después restaure una versión anterior, consulte el uso y la velocidad de la aplicación, configure alertas y resúmenes, inclúyala en la galería y fíjela en Inicio.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio es el editor de aplicaciones Panel dentro de PlaidCloud. Muestra los archivos de la aplicación junto a un editor, crea una vista previa privada que usted puede abrir y publica la aplicación cuando esté lista. No necesita un repositorio de git para empezar.

## Abrir Panel Studio

- En el tablero **Inicio** de un proyecto, elija **Abrir en Studio** en una aplicación Panel.
- En **Mis aplicaciones Panel**, elija **Abrir en Studio** en la fila de una aplicación.

Para iniciar una aplicación nueva, elija **Nueva aplicación Studio**. Es el primer botón de la barra de herramientas de **Mis aplicaciones Panel** y se encuentra en el cuadro **Aplicaciones de Panel** de la pestaña **Inicio** de un proyecto. Para crear sobre una tabla, selecciónela en la pestaña **Tablas** del proyecto y elija **Crear aplicación Panel**.

## Crear una aplicación

El cuadro de diálogo **Nueva aplicación Studio** le permite empezar desde uno de cinco lugares:

| Comenzar desde | Qué obtiene |
|---|---|
| **Aplicación en blanco** | Una aplicación mínima con un `app.py` y un `requirements.txt`. |
| **Desde una tabla** | Una aplicación creada sobre la tabla que elija. |
| **Desde una vista** | Lo mismo, creada sobre una vista del proyecto. |
| **Desde otra aplicación Studio** | Una copia de una de sus aplicaciones de Studio. |
| **Desde la galería** | Una copia de una aplicación que su espacio de trabajo ha incluido en la [galería de aplicaciones](/es/guides/panel-apps/gallery/). |

Dé un nombre a la aplicación, elija su **Proyecto** y elija **Crear**. Studio abre la nueva aplicación con sus archivos enumerados a la izquierda. Si parte de una tabla o una vista, el prompt de Weave para crear la primera página de la aplicación está listo para enviarse. Consulte [Crear una aplicación Panel](/es/guides/panel-apps/creating/).

## Editar

Elija un archivo de la lista para editarlo en el editor. Enumere sus dependencias de Python en `requirements.txt`, un paquete por línea. Se instalan cuando se compila la aplicación.

Elija **Preguntar a Weave** para que Weave escriba o modifique la aplicación por usted. Consulte [Crear aplicaciones Panel con Weave](/es/guides/panel-apps/build-with-weave/).

## Guardar, previsualizar y publicar

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Guardar conserva un borrador que solo usted puede ver. Vista previa crea una copia privada del borrador para el editor. Publicar reemplaza la aplicación en vivo después de que usted lo confirme." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Guardar</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">solo borrador</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Vista previa</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">solo el editor</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publicar</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">la aplicación en vivo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Sus ediciones solo llegan a los usuarios cuando usted publica.</figcaption>
</figure>

### Guardar

**Guardar** almacena sus cambios como borrador. La aplicación en vivo no cambia y nadie más ve el borrador.

### Vista previa

**Vista previa** compila su borrador guardado como una copia privada y la abre. Solo los editores de la aplicación pueden abrir una vista previa.

- Una vista previa se elimina después de 24 horas sin guardar.
- Un espacio de trabajo puede tener hasta 10 vistas previas a la vez.
- Guarde de nuevo y elija **Vista previa** para ver sus últimas ediciones.

### Publicar

**Publicar** reemplaza la aplicación en vivo por su borrador guardado. Requiere permiso de edición en el proyecto de la aplicación, y Studio le pide confirmación antes.

Si otra persona publicó un cambio después de que usted abriera la aplicación, Studio informa de un conflicto en lugar de sobrescribir su trabajo. Vuelva a cargar la aplicación, incorpore sus ediciones y publique de nuevo.

## Estado de la compilación y errores

La pestaña **Crear** muestra el estado de la última compilación y se actualiza mientras se ejecuta. Cuando una compilación falla, la pestaña enumera cada error con su archivo y su número de línea, para que usted pueda ir directamente a la línea. Los problemas de dependencias en `requirements.txt` incluyen una sugerencia para corregirlos.

Los errores y las advertencias también se marcan en sus líneas en el editor, de modo que usted ve el problema donde está.

Para saber qué significa cada estado una vez publicada la aplicación, consulte [Usar una aplicación Panel](/es/guides/panel-apps/using/#estado-de-compilación-aplicaciones-de-servidor).

## Historial y restauración

La pestaña **Historial** enumera todas las versiones publicadas de la aplicación, de la más reciente a la más antigua, con su estado de compilación. Elija **Cargar más** para ver las más antiguas.

Para volver a una versión anterior, elija **Restaurar** en ella y confirme. La versión restaurada pasa a ser la aplicación en vivo y se vuelve a compilar. Su borrador sin guardar no se pierde: permanece en el borrador y se pone en vivo sobre la versión restaurada la próxima vez que publique. Si la aplicación ya coincide con esa versión, Studio lo indica y no cambia nada. Si alguien publicó mientras usted restauraba, Studio no restaura nada y le pide que lo intente de nuevo.

## Análisis

La pestaña **Análisis** muestra cómo usan la aplicación las personas y con qué rapidez responde. Elija los últimos 7, 14 o 30 días.

| Sección | Muestra |
|---|---|
| **Vistas por día** | Cuántas veces se abrió la aplicación cada día. |
| **Carga de página** | El tiempo de carga mediano y el tiempo que superan el 95 por ciento de las cargas, a partir de las cargas de página del período. |
| **Consultas más lentas** | Las consultas que más tardaron, con la frecuencia con que se ejecutaron y sus tiempos mediano, del extremo lento y más lento. |
| **Errores** | Qué salió mal en el período, por tipo de error y por el lugar de la aplicación donde ocurrió. |

Cuando un período contiene más actividad de la que Análisis puede leer, indica que las cifras son parciales. Cuando las cargas de página superan el [presupuesto de rendimiento](/es/guides/panel-apps/app-kit/#presupuestos-de-rendimiento) de la aplicación, Análisis le avisa de cuántas lo hicieron y qué consultas fueron lentas. Análisis nunca muestra los datos que devolvió una consulta ni los nombres de las personas que abrieron la aplicación.

Ambas pestañas requieren que la aplicación esté asignada a un proyecto; una aplicación sin asignar muestra un aviso para asignarla.

## Alertas y resúmenes

Elija **Alertas y resúmenes** para configurar notificaciones que vigilan una cifra de los datos de la aplicación y le avisan cuando supera un límite, o que envían un resumen según una programación. Consulte [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/).

## Incluir una aplicación en la galería

Elija **Galería…** en Studio. Elija **Publicar en la galería** para incluir la aplicación como una plantilla a partir de la cual cualquier persona que pueda ver su proyecto puede crear su propia aplicación, o **Quitar de la galería** para quitarla. El botón está disponible para las aplicaciones que pertenecen a un proyecto. Necesita acceso de edición al proyecto. Consulte [La galería de aplicaciones](/es/guides/panel-apps/gallery/).

## Fijar en Inicio

Elija **Anclar a Inicio** para agregar la aplicación al tablero **Inicio** del proyecto y **Desanclar de Inicio** para quitarla.

## Eliminar una aplicación

Eliminar una aplicación Panel pide confirmación primero. En **Mis aplicaciones Panel**, use el icono de **menos** en la fila de la aplicación. Cancelar la publicación también pide confirmación.

## Siguientes pasos

- [Crear aplicaciones Panel con Weave](/es/guides/panel-apps/build-with-weave/): describa la aplicación y apruebe el cambio exacto.
- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): los componentes que usan los inicios de Studio a partir de tablas y vistas.
- [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/): avise a las personas cuando una cifra supere un límite, o según una programación.
- [La galería de aplicaciones](/es/guides/panel-apps/gallery/): comparta una aplicación como punto de partida para otros.
- [Usar una aplicación Panel](/es/guides/panel-apps/using/): registros, uso y recompilaciones después de publicar.
