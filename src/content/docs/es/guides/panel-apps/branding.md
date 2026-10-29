---
title: Marca del proyecto y proyectos de aplicaciones
description: Defina los colores de marca y un logotipo una sola vez para un proyecto, de modo que todas las aplicaciones Panel que contiene coincidan, y asigne aplicaciones Panel a un proyecto al publicarlas o después.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/branding.md
---

Una aplicación Panel pertenece a un proyecto. El proyecto hace dos cosas por la aplicación: es donde la aplicación lee sus tablas de forma predeterminada y contiene los colores y el logotipo que la aplicación luce. Defina la marca una vez y todas las aplicaciones del proyecto la adoptan.

## Aplicar la marca a un proyecto

1. Abra el proyecto y vaya a su pestaña **Inicio**.
2. En el grupo **Panel App Branding**, haga clic en **Edit Branding**.
3. Defina cualquiera de los colores. Haga clic en una muestra para elegir un color, o escriba un valor hexadecimal como `#0078d4`.
4. Opcionalmente, elija un logotipo.
5. Compruebe la **Vista previa** y luego haga clic en **Guardar**.

Solo los Gerentes y los Arquitectos pueden guardar la marca. Los demás miembros del proyecto ven el formulario en modo de solo lectura.

**Reset to default** borra todos los colores y el logotipo. Al guardar se reemplaza la marca completa, por lo que un color que deje en blanco vuelve al valor predeterminado de PlaidCloud.

### Colores

| Configuración | Qué colorea |
|---|---|
| **Brand** | Los botones, la pestaña activa, los controles deslizantes y otros controles principales. |
| **Brand accent** | Los acentos secundarios. |
| **Brand hover** | Un control principal mientras el puntero está sobre él. |
| **Brand pressed** | Un control principal mientras está presionado. |
| **Header background** | La barra del encabezado de la aplicación. |
| **Header text** | El título y el nombre de usuario en el encabezado. |
| **Link** | Los vínculos. |
| **Text on brand** | El texto que se encuentra sobre un control de color de marca. |

Estas ocho son las únicas opciones de configuración. Los colores deben ser valores hexadecimales de 3 o 6 dígitos. Las superficies, el texto del cuerpo y los bordes conservan el aspecto de PlaidCloud en modo claro y oscuro, por lo que una marca no puede hacer que una aplicación sea ilegible.

### Logotipo

El logotipo es una imagen de una [cuenta de documentos](/es/guides/documents/) del espacio de trabajo del proyecto.

1. Cargue la imagen en una carpeta llamada `branding` en el nivel superior de la cuenta de documentos.
2. En **Edit Branding**, elija la **Cuenta de documentos** y luego la imagen en **Image in the branding/ folder**.

El logotipo puede ser un archivo PNG, JPEG, GIF, WebP o SVG de hasta 512 KB. Aparece en el lado derecho del encabezado de la aplicación. La imagen debe estar directamente en `branding/` o en una carpeta dentro de ella, y cualquier persona que guarde la marca debe poder leer la cuenta.

### Cuándo aparecen los cambios

Una aplicación lee su marca cuando se inicia la sesión de un visualizador. Los cambios guardados se muestran la próxima vez que alguien abre la aplicación o la vuelve a cargar.

## Asignar una aplicación a un proyecto

### Al publicar

El cuadro de diálogo **Publicar aplicación Panel de servidor** tiene un selector **Proyecto** en **Configuración del directorio**. Elija el proyecto propietario de la aplicación. Necesita acceso al proyecto para publicar en él. El proyecto queda fijo una vez publicada la aplicación; para mover una aplicación, use **Asignar** como se describe a continuación.

Una aplicación publicada con un proyecto lee las tablas de ese proyecto de forma predeterminada, por lo que `table("sales")` no necesita un argumento de proyecto.

### Para aplicaciones existentes

1. Abra **Mis aplicaciones Panel**.
2. Haga clic en el icono **Asignar** en la fila de la aplicación que desea mover.
3. Elija el **Proyecto** y haga clic en **Revisar**.
4. Lea el resultado. Enumera los miembros del espacio de trabajo que hoy pueden abrir la aplicación pero no son miembros del proyecto.
5. Haga clic en **Asignar**.

Revisar no cambia nada. La columna **Proyecto** de **Mis aplicaciones Panel** muestra el proyecto de cada aplicación.

### Acceso

Quién puede abrir una aplicación no cambia hoy por su proyecto: los visualizadores que podían abrir la aplicación antes siguen pudiendo. Con el tiempo, el acceso a una aplicación seguirá la pertenencia a su proyecto, y por eso **Revisar** enumera los miembros que no están en el proyecto, para que pueda agregarlos primero.

## Siguientes pasos

- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): los componentes que usan su marca.
- [Creación de una aplicación Panel](/es/guides/panel-apps/creating/): publique una aplicación en un proyecto.
