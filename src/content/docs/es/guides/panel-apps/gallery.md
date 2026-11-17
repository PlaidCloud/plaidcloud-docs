---
title: La galería de aplicaciones
description: Agregue una aplicación Studio a la galería o quítela, y cree una aplicación nueva a partir de una publicada.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

La galería de aplicaciones es el estante donde su espacio de trabajo guarda aplicaciones de Panel ya preparadas. Cualquier persona que pueda ver el proyecto de una aplicación publicada puede crear su propia copia en un proyecto que pueda editar y modificarla, de modo que una buena aplicación se convierte en un punto de partida en lugar de algo que la gente reconstruye.

## Crear una aplicación desde la galería

1. En **Aplicaciones**, elija **Nueva aplicación** > **Studio**.
2. En **Comenzar desde**, elija **Desde la galería**.
3. Elija una aplicación en **Aplicación de la galería**. Su descripción aparece debajo del selector.
4. Asigne un nombre a su aplicación, elija su **Proyecto** y elija **Crear**.

También puede elegir **Nueva aplicación** > **Desde la galería…** para explorar la galería por sí sola. Muestra cada aplicación con su nombre, proyecto y descripción, y **Crear aplicación a partir de esto…**. La galería solo muestra las aplicaciones de proyectos que usted puede ver.

La aplicación nueva es una copia de los archivos de la aplicación publicada. Su copia y el original son independientes: cambiar uno nunca cambia el otro.

## Publicar su aplicación

Necesita acceso de edición al proyecto de la aplicación. Solo se pueden publicar las aplicaciones creadas en [Panel Studio](/es/guides/panel-apps/studio/) que pertenecen a un proyecto; las aplicaciones de servidor, WASM y Dash no.

1. Abra la aplicación en Studio y elija **Galería…**. El botón solo está disponible para una aplicación que pertenece a un proyecto.
2. Introduzca una **Descripción** para mostrar en la tarjeta de la galería.
3. Elija **Publicar en la galería** y confirme.

Para cambiar la descripción, elija **Actualizar publicación**. Para quitar la aplicación de la galería, abra **Galería…** y elija **Quitar de la galería**. Mover la aplicación a otro proyecto también la quita de la galería.

## Quién puede ver qué

Todas las personas que pueden ver el proyecto pueden leer el código fuente de la aplicación publicada, incluidos los cambios que publique más adelante. No ponga contraseñas ni notas privadas en los archivos de una aplicación publicada. Al elegir publicar una aplicación, primero se le pide que lo confirme, y la publicación queda registrada en el registro de auditoría.

Las personas que crean desde la galería obtienen una copia de los archivos solo en la propia carpeta de la aplicación. Nunca ven los detalles del repositorio de la aplicación, las conexiones ni la configuración de webhooks.

## Pasos siguientes

- [Panel Studio](/es/guides/panel-apps/studio/): edite y publique la copia que cree.
- [El kit de aplicaciones de Panel](/es/guides/panel-apps/app-kit/): los componentes con los que se crean la mayoría de las aplicaciones de la galería.
