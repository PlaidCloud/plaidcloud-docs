---
title: Instalar PlaidXL
description: Agregue el complemento PlaidXL a Excel en Windows o Mac, encuentre la pestaña PlaidCloud de la cinta de opciones y abra el panel de tareas de PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

Usted instala PlaidXL una sola vez por equipo, no una vez por libro. A partir de ese momento, la pestaña **PlaidCloud** está en la cinta de opciones de Excel en todos los libros que abra.

## Antes de empezar

- Utilice Excel para Microsoft 365, o Excel 2021 o posterior, en Windows o Mac.
- Si su organización administra los complementos de Office de forma centralizada, es posible que el administrador de Microsoft 365 deba implementar PlaidXL por usted. Si no puede instalar complementos usted mismo, pídale que agregue el complemento **PlaidCloud**.

## Instalar en Windows

1. En Excel, abra **Insertar → Complementos** (en algunas versiones, **Inicio → Complementos**).
2. Escriba `PlaidCloud` en el cuadro de búsqueda de complementos.
3. Seleccione el complemento **PlaidCloud** y haga clic en **Agregar**.

## Instalar en Mac

1. En Excel para Mac, abra **Insertar → Complementos**. En versiones anteriores, el menú es **Insertar → Store**.
2. Escriba `PlaidCloud` en el cuadro de búsqueda de complementos.
3. Seleccione el complemento **PlaidCloud** y haga clic en **Agregar**.

## Abrir el panel de tareas

1. Haga clic en la pestaña **PlaidCloud** de la cinta de opciones.
2. En el grupo **Datos**, haga clic en **Open PlaidXL**.

El panel de tareas de PlaidXL se abre en el lado derecho de la ventana y le pide que inicie sesión. Continúe con [Iniciar sesión](/es/reference/cli/plaidxl/connect/).

El panel de tareas mantiene la sesión iniciada entre sesiones de trabajo, así que normalmente iniciará sesión una vez y después solo abrirá el panel de tareas cuando lo necesite.

## Si PlaidXL no aparece

- Cierre todas las ventanas de Excel y vuelva a abrir Excel. A menudo, un complemento no aparece en la cinta de opciones hasta que se reinicia Excel.
- Busque en **Insertar → Mis complementos** (Windows) o **Insertar → Complementos → Mis complementos** (Mac) y seleccione **PlaidCloud** desde allí.
- Si su organización bloquea los complementos de la tienda, pida a su administrador de Microsoft 365 que lo implemente.

Hay más soluciones en la página [Solución de problemas](/es/reference/cli/plaidxl/troubleshooting/).

## Relacionado

- [Iniciar sesión](/es/reference/cli/plaidxl/connect/): conecte el complemento a su espacio de trabajo
- [La cinta de opciones de PlaidCloud](/es/reference/cli/plaidxl/ribbon/): todos los comandos de la pestaña **PlaidCloud**
