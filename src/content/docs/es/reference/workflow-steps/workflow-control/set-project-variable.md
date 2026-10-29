---
title: Set Project Variable (paso)
description: Establezca variables a nivel de proyecto desde un paso de flujo de trabajo de PlaidCloud para almacenar valores accesibles desde todos los flujos de trabajo del proyecto.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable.md
---

## Descripción


“Set Project Variable” establece variables del proyecto para usarlas durante el flujo de trabajo. El nombre y el valor de una variable pueden contener cualquier combinación de caracteres válidos, incluidos espacios. Las variables se referencian dentro del flujo de trabajo colocándolas entre llaves. Por ejemplo, *a_variable* se referencia dentro de una transformación como *\{a_variable}*, por lo que puede usarse en algo como una fórmula o un valor de campo (p. ej., \{a_variable} * 2).



## Lista de variables


La tabla enumera todas las variables registradas en el proyecto, cada una con su **Valor actual** y su **Nota**, que se leen de nuevo cada vez que abre el paso, de modo que puede ver qué contiene una variable ahora antes de decidir qué valor asignarle.

Para establecer una, marque **Establecer** en su fila e introduzca el nuevo valor en **Establecer valor**. Solo se escriben las filas marcadas cuando se ejecuta el paso, por lo que un valor introducido sin marcar **Establecer** se ignora. También es posible establecer una variable que aún no se ha registrado: agregue una fila y establézcala del mismo modo; al ejecutar el paso se crea.







## Ejemplos


Aún no hay ejemplos...
