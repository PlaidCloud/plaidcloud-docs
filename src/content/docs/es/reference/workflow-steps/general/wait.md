---
title: Esperar
description: Agregue un retardo temporizado en un paso de flujo de trabajo de PlaidCloud para pausar la ejecución durante un tiempo determinado antes de continuar con el siguiente paso.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## Descripción


La transformación Esperar se usa para pausar el procesamiento durante un tiempo determinado. Puede ser especialmente útil cuando se esperan operaciones de E/S de otros sistemas o para depurar flujos de trabajo durante el desarrollo.



## Parámetros de duración


Especifique un valor entero no negativo con el control numérico **Duración**.



A continuación, especifique la unidad de tiempo en el menú desplegable. Están disponibles las siguientes unidades:


* Segundos
* Minutos
* Horas

## Esperar una hora o un archivo

La sección **Otras esperas** tiene estos campos. El paso los espera en este orden, después de la duración:

* **Milisegundos** (`milliseconds`): milisegundos que se esperan además de la duración.
* **Hasta la hora del día** (`until_time`): después, espera hasta que el reloj marque por siguiente vez esta hora del día, en UTC, como `HH:MM:SS`.
* **Esperar un archivo** (`file`): después, espera a que cambie este archivo de Document, `{account, path}`. **Cambio del archivo** (`file_event`) es el cambio que se espera: `modified` (predeterminado), `created` o `deleted`. El paso revisa el archivo cada **Revisar el archivo cada (segundos)** (`poll_seconds`, predeterminado 5) durante como máximo **Espera máxima del archivo (segundos)** (`max_wait_seconds`, predeterminado 3600, como máximo un día), y luego finaliza con una advertencia y el flujo de trabajo continúa. Un archivo que ya existe cuando se espera `created` termina la espera de inmediato, y un archivo que falta cuando se espera `modified` o `deleted` finaliza con una advertencia que nombra la ruta, sin esperar.
