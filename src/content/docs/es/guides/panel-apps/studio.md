---
title: Panel Studio
description: Cree, edite, obtenga una vista previa y publique aplicaciones de Panel sin salir de PlaidCloud, y después restaure una versión anterior, consulte el uso y la velocidad de la aplicación, configure alertas y resúmenes, publíquela en la galería y ancle a Inicio.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio es el editor de aplicaciones de Panel dentro de PlaidCloud. Muestra los archivos de la aplicación junto a un editor, crea una vista previa privada que puede abrir y publica la aplicación cuando esté lista. No necesita un repositorio git para empezar.

## Abrir Panel Studio

- En el tablero **Inicio** de un proyecto, elija **Abrir en Studio** en una aplicación de Panel.
- En **Mis aplicaciones Panel**, elija **Studio** en la fila de una aplicación.

Para empezar una aplicación nueva, elija **Nueva aplicación Studio**. Es el primer botón de la barra de herramientas de **Mis aplicaciones Panel**, y está en el cuadro **Aplicaciones Panel** de la pestaña **Inicio** de un proyecto. Para crear sobre una tabla, selecciónela en la pestaña **Tablas** del proyecto y elija **Crear aplicación Panel**.

## Crear una aplicación

El cuadro de diálogo **Nueva aplicación Studio** le permite comenzar desde uno de cinco lugares:

| Comenzar desde | Obtiene |
|---|---|
| **Aplicación en blanco** | Una aplicación mínima con un `app.py` y un `requirements.txt`. |
| **Desde una tabla** | Una aplicación creada sobre la tabla que seleccione. |
| **Desde una vista** | Lo mismo, creada sobre una vista del proyecto. |
| **Desde otra aplicación Studio** | Una copia de una de sus aplicaciones Studio. |
| **Desde la galería** | Una copia de una aplicación que su espacio de trabajo ha publicado en la [galería de aplicaciones](/es/guides/panel-apps/gallery/). |

Asigne un nombre a la aplicación, seleccione su **Proyecto** y elija **Crear**. Studio abre la aplicación nueva con sus archivos enumerados a la izquierda. Para una tabla o una vista, la indicación de Weave para crear la primera página de la aplicación queda lista para enviar. Consulte [Crear una aplicación de Panel](/es/guides/panel-apps/creating/).

## Editar

Seleccione un archivo de la lista para editarlo en el editor. Enumere sus dependencias de Python en `requirements.txt`, un paquete por línea. Se instalan cuando se compila la aplicación.

Elija **Preguntar a Weave** para que Weave escriba o modifique la aplicación por usted. Consulte [Crear aplicaciones de Panel con Weave](/es/guides/panel-apps/build-with-weave/).

## Guardar, obtener una vista previa y publicar

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Guardar conserva un borrador que solo usted puede ver. La vista previa crea una copia privada del borrador para el editor. Publicar reemplaza la aplicación activa después de que usted lo confirma." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Guardar</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">solo borrador</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Vista previa</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">solo editor</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publicar</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">la aplicación activa</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Sus ediciones solo llegan a quienes ven la aplicación cuando la publica.</figcaption>
</figure>

### Guardar

**Guardar** almacena sus cambios como borrador. La aplicación activa no cambia y nadie más ve el borrador.

### Vista previa

**Vista previa** compila su borrador guardado como una copia privada y la abre. Solo quienes editan la aplicación pueden abrir una vista previa.

- Una vista previa se elimina después de 24 horas sin guardar.
- Un espacio de trabajo puede tener hasta 10 vistas previas a la vez.
- Guarde de nuevo y elija **Vista previa** para ver sus últimas ediciones.

### Publicar

**Publicar** reemplaza la aplicación activa con su borrador guardado. Requiere permiso de edición en el proyecto de la aplicación, y Studio le pide que lo confirme primero.

Si otra persona publicó un cambio después de que usted abrió la aplicación, Studio informa de un conflicto en lugar de sobrescribir su trabajo. Vuelva a cargar la aplicación, incorpore sus ediciones y publique de nuevo.

## Estado de la compilación y errores

La pestaña **Crear** muestra el estado de la compilación más reciente y se actualiza mientras se ejecuta. Cuando una compilación falla, la pestaña enumera cada error con su archivo y número de línea, para que pueda ir directamente a la línea. Los problemas de dependencias en `requirements.txt` incluyen una sugerencia sobre cómo corregirlos.

Los errores y las advertencias también se marcan en sus líneas en el editor, de modo que vea el problema donde está.

Para saber qué significa cada estado una vez publicada la aplicación, consulte [Usar una aplicación de Panel](/es/guides/panel-apps/using/#estado-de-compilación-aplicaciones-de-servidor).

## Historial y restauración

La pestaña **Historial** enumera todas las versiones publicadas de la aplicación, de la más reciente a la más antigua, con su estado de compilación. Elija **Cargar más** para ver las anteriores.

Para volver a una versión anterior, elija **Restaurar** en ella y confirme. La versión restaurada se convierte en la aplicación activa y se vuelve a compilar. Su borrador sin guardar no se pierde: permanece en el borrador y pasa a estar activo sobre la versión restaurada la próxima vez que publique. Si la aplicación ya coincide con esa versión, Studio lo indica y no cambia nada. Si otra persona publicó mientras usted restauraba, Studio no restaura nada y le pide que lo intente de nuevo.

## Análisis

La pestaña **Análisis** muestra cómo usan la aplicación las personas y con qué rapidez responde. Elija los últimos 7, 14 o 30 días.

| Sección | Muestra |
|---|---|
| **Vistas por día** | Cuántas veces se abrió la aplicación cada día. |
| **Carga de página** | El tiempo de carga mediano y el tiempo que el 95 por ciento de las cargas mejoran, a partir de las cargas de página del período. |
| **Consultas más lentas** | Las consultas que más tardaron, con la frecuencia con que se ejecutaron y sus tiempos mediano, del extremo lento y más lento. |
| **Errores** | Lo que salió mal en el período, por tipo de error y por el lugar de la aplicación donde ocurrió. |

Cuando un período contiene más actividad de la que Análisis puede leer, indica que las cifras son parciales. Cuando las cargas de página superan el [presupuesto de rendimiento](/es/guides/panel-apps/app-kit/#presupuestos-de-rendimiento) de la aplicación, Análisis le advierte cuántas lo hicieron y qué consultas fueron lentas. Análisis nunca muestra los datos que devolvió una consulta ni los nombres de las personas que abrieron la aplicación.

Las pestañas **Historial** y **Análisis** requieren que la aplicación esté asignada a un proyecto; una aplicación sin asignar muestra una indicación para asignarla.

## Alertas y resúmenes

Elija **Alertas y resúmenes** para configurar notificaciones que vigilan un número en los datos de la aplicación y le avisan cuando cruza un límite, o que envían un resumen según una programación. Consulte [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/).

## Publicar una aplicación en la galería

Elija **Galería…** en Studio. Elija **Publicar en la galería** para publicar la aplicación como una plantilla a partir de la cual cualquier persona que pueda ver su proyecto puede crear su propia aplicación, o **Quitar de la galería** para quitarla. El botón está disponible para las aplicaciones que pertenecen a un proyecto. Necesita acceso de edición al proyecto. Consulte [La galería de aplicaciones](/es/guides/panel-apps/gallery/).

## Anclar a Inicio

Elija **Anclar a Inicio** para agregar la aplicación al tablero **Inicio** del proyecto, y **Desanclar de Inicio** para quitarla.

## Eliminar una aplicación

Eliminar una aplicación de Panel le pide que lo confirme primero. En **Mis aplicaciones Panel**, use el icono de **menos** en la fila de la aplicación. Anular la publicación también le pide que lo confirme.

## Siguientes pasos

- [Crear aplicaciones de Panel con Weave](/es/guides/panel-apps/build-with-weave/): describa la aplicación y apruebe el cambio exacto.
- [El kit de aplicaciones de Panel](/es/guides/panel-apps/app-kit/): los componentes que usan los inicios de Studio desde tabla y desde vista.
- [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/): notifique a las personas cuando un número cruza un límite, o según una programación.
- [La galería de aplicaciones](/es/guides/panel-apps/gallery/): comparta una aplicación como punto de partida para otras personas.
- [Usar una aplicación de Panel](/es/guides/panel-apps/using/): registros, uso y recompilaciones después de publicar.
