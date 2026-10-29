---
title: La galería de aplicaciones
description: Publique una aplicación Panel como una plantilla desde la que su espacio de trabajo pueda comenzar, y cree una aplicación nueva a partir de una publicada.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

La galería de aplicaciones es el estante donde su espacio de trabajo conserva aplicaciones Panel ya hechas. Cualquier persona que pueda ver el proyecto de una aplicación publicada puede crear su propia copia y modificarla, de modo que una buena aplicación se convierte en un punto de partida en lugar de algo que la gente reconstruye.

## Crear una aplicación desde la galería

1. En **Mis aplicaciones Panel**, elija **Create app**.
2. En **Comenzar desde**, elija **Desde la galería**.
3. Elija una aplicación. Su descripción aparece debajo del selector.
4. Dé un nombre a su aplicación, elija su **Proyecto** y elija **Crear**.

También puede abrir la galería por separado, donde cada tarjeta muestra el nombre, la descripción y el proyecto de la aplicación, con **Create app from this…**. La galería solo enumera las aplicaciones de los proyectos que usted puede ver.

La nueva aplicación es una copia de los archivos de la aplicación publicada. Su copia y el original son independientes: cambiar uno nunca cambia el otro.

## Publicar su aplicación

Necesita permiso de edición sobre el proyecto de la aplicación, y la aplicación debe haberse creado en [Panel Studio](/es/guides/panel-apps/studio/) y estar asignada a un proyecto.

1. Abra la aplicación en Studio y elija **Gallery…**.
2. Escriba una **Descripción** para mostrar en la tarjeta de la galería.
3. Elija **List in gallery** y confirme.

Para cambiar la descripción, elija **Update listing**. Para quitar la aplicación, elija **Take out of gallery**. Mover la aplicación a otro proyecto también la quita de la galería.

## Quién puede ver qué

Todas las personas que pueden ver el proyecto pueden leer el código fuente de la aplicación publicada, incluidos los cambios que publique más adelante. No coloque contraseñas ni notas privadas en los archivos de una aplicación publicada. Al elegir publicar una aplicación, se le pide que confirme esto primero, y la publicación queda registrada en el registro de auditoría.

Las personas que crean desde la galería obtienen una copia de los archivos solo de la carpeta propia de la aplicación. Nunca ven los detalles del repositorio de la aplicación, las conexiones ni la configuración de webhooks.

## Siguientes pasos

- [Panel Studio](/es/guides/panel-apps/studio/): edite y publique la copia que crea.
- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): los componentes con los que se crean la mayoría de las aplicaciones de la galería.
