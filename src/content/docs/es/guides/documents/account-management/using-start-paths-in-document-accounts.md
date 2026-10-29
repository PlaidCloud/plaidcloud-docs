---
title: Uso de rutas de inicio en las cuentas de documentos
description: Configure rutas de inicio en las cuentas de documentos de PlaidCloud para controlar la ubicación de directorio predeterminada al examinar el almacenamiento de archivos.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

El formulario de administración de cuentas permite configurar la información de conexión de almacenamiento y una ruta de inicio. Una ruta de inicio permite a quienes usan la cuenta comenzar a examinar la estructura de directorios más abajo en el árbol de directorios. Esta opción es útil cuando varios equipos necesitan almacenamiento de archivos segregado, pero solo desea una cuenta de servicio de almacenamiento subyacente.



La opción Ruta de inicio de las cuentas de documentos es útil por los siguientes motivos:


* Para controlar el acceso a subdirectorios de equipos y grupos específicos
* Para conceder acceso a un solo bucket

Por ejemplo, establecer una ruta de inicio de *teams/team_1/* para la cuenta de documentos `Team 1` y *teams/team_2* para la cuenta de documentos `Team 2` proporciona puntos de partida distintos en una cuenta compartida. Cuando un miembro abre la cuenta de documentos Team 1, comienza la navegación de archivos dentro de *team/team_1*. No podrá subir por el árbol ni ver nada por encima de *teams/team_1*.



Team 2 tendría una restricción similar: no podría navegar al área de Team 1.



Esto permite restringir a equipos específicos a los niveles inferiores del árbol, mientras que otros equipos tienen acceso de nivel superior al árbol, sin necesidad de complejidad adicional en el almacenamiento en la nube, como buckets adicionales o permisos especiales.



## Agregar y actualizar la ruta de inicio


1. Vaya a Document > Manage Accounts
2. Seleccione la cuenta que desea editar y entre en el modo de edición
3. Agregue una ruta de inicio en el campo de texto Ruta de inicio
4. Seleccione el botón Guardar

## Formato de la ruta de inicio


La ruta siempre comienza con el nombre del bucket seguido de los subdirectorios.



```text
<my-bucket>/folder1/folder2/
```
