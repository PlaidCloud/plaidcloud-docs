---
title: La galería de aplicaciones
description: Agregue una aplicación de Studio a la galería o retírela, y cree una aplicación nueva a partir de una aplicación incluida.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

La galería de aplicaciones es el estante donde su espacio de trabajo guarda aplicaciones Panel ya hechas. Cualquier persona que pueda ver el proyecto de una aplicación incluida puede crear su propia copia y modificarla, de modo que una buena aplicación se convierte en un punto de partida en lugar de algo que todos reconstruyen.

## Crear una aplicación desde la galería

1. En **Mis aplicaciones Panel**, elija **Nueva aplicación Studio**.
2. En **Comenzar desde**, elija **Desde la galería**.
3. Elija una aplicación en **Aplicación de la galería**. Su descripción aparece debajo del selector.
4. Dé un nombre a su aplicación, elija su **Proyecto** y elija **Crear**.

También puede elegir **Galería** en la barra de herramientas de **Mis aplicaciones Panel** para explorar la galería por separado. Cada tarjeta muestra el nombre, la descripción y el proyecto de la aplicación, con **Crear aplicación a partir de esto…**. La galería solo muestra las aplicaciones de proyectos que usted puede ver.

La nueva aplicación es una copia de los archivos de la aplicación incluida. Su copia y el original son independientes: modificar uno nunca modifica el otro.

## Incluir su aplicación

Necesita acceso de edición al proyecto de la aplicación. Solo se pueden incluir las aplicaciones creadas en [Panel Studio](/es/guides/panel-apps/studio/) que pertenecen a un proyecto; las aplicaciones de servidor, WASM y Dash no.

1. Abra la aplicación en Studio y elija **Galería…**. El botón solo está disponible para una aplicación que pertenece a un proyecto.
2. Escriba una **Descripción** que se mostrará en la tarjeta de la galería.
3. Elija **Publicar en la galería** y confirme.

Para cambiar la descripción, elija **Actualizar publicación**. Para quitar la aplicación de la galería, abra **Galería…** y elija **Quitar de la galería**. Mover la aplicación a otro proyecto también la quita de la galería.

## Quién puede ver qué

Todas las personas que pueden ver el proyecto pueden leer el código fuente de la aplicación incluida, incluidos los cambios que publique más adelante. No incluya contraseñas ni notas privadas en los archivos de una aplicación incluida. Al elegir incluir una aplicación, primero se le pide que lo confirme, y la inclusión queda registrada en el registro de auditoría.

Quienes crean una aplicación desde la galería obtienen una copia de los archivos de la carpeta propia de la aplicación únicamente. Nunca ven los detalles del repositorio de la aplicación, sus conexiones ni la configuración de sus webhooks.

## Siguientes pasos

- [Panel Studio](/es/guides/panel-apps/studio/): edite y publique la copia que cree.
- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): los componentes con los que se crean la mayoría de las aplicaciones de la galería.
