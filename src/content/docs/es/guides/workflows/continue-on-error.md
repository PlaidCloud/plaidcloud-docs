---
title: Continuar en caso de error
description: Configure los pasos de un flujo de trabajo de PlaidCloud para que continúen la ejecución cuando se produce un error, de modo que los pasos siguientes se ejecuten a pesar de fallos anteriores.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/continue-on-error.md
---

Los pasos de un flujo de trabajo pueden configurarse para que sigan procesando aunque se produzca un error. Esto puede ser útil en condiciones de inicio del flujo de trabajo o cuando los datos pueden estar disponibles de forma intermitente. Si el paso produce un error, se registra como error, pero el flujo de trabajo continúa procesando.



Para establecer esta opción, abra el formulario del paso desde la tabla del flujo de trabajo (haga clic en su icono de engranaje o haga clic con el botón derecho y elija **Editar detalles del paso**) y vaya a la pestaña **General**. Establezca **Acción que se realizará en caso de error** en **Continuar**. Después de guardar el paso actualizado, ningún error del paso hará que el flujo de trabajo se detenga.



Los pasos que se han configurado para continuar en caso de error tendrán un indicador especial en la tabla de jerarquía de pasos del flujo de trabajo.
