---
title: Actualizar
description: Actualice su agente de PlaidLink a la última versión para acceder a nuevas funciones, parches de seguridad y una mejor compatibilidad con el sistema.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

Puede ser necesaria una actualización manual de PlaidLink si el agente no tiene privilegios suficientes para actualizarse a sí mismo cuando se publican nuevas versiones, o si prefiere un proceso de actualización manual.

## Descargar el agente

Consulte las versiones publicadas en [PlaidCloud.com](https://plaidcloud.com/) para **PlaidLink**

## Detener el agente actual

Escriba **`Services`** en la barra de búsqueda de Windows y abra el administrador de servicios. En la lista de servicios, busque **`PlaidCloud Agent`**.

Haga clic con el botón derecho en el servicio **`PlaidCloud Agent`** y seleccione *Stop*. Cuando el servicio se detenga correctamente, continúe.

## Extraer el agente

Vaya a la ubicación actual del agente instalado.

```bash
C:\Users\<Username here>\src\
```

Cambie el nombre de la carpeta de la instalación actual para que ya no se utilice como referencia. Por ejemplo, `Plaidlink_Old_12122022`

Extraiga el archivo zip descargado en esta misma ubicación para instalarlo. Por lo general, esta ubicación será:

```bash
C:\Users\<Username here>\src\plaidlink
```

## Iniciar el agente

Vuelva a la ventana *Services*. Haga clic con el botón derecho en el servicio **`PlaidCloud Agent`** y seleccione *Start*.

Escriba **`Services`** en la barra de búsqueda de Windows y abra el administrador de servicios. En la lista de servicios, busque **`PlaidCloud Agent`**.

Haga clic con el botón derecho en el servicio y seleccione **`Start`** para iniciar el agente. Cuando el agente aparezca en el estado **`Running`**, volverá a estar operativo con la nueva versión.
