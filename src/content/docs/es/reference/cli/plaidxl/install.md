---
title: Instalar PlaidXL
description: Agregue el complemento PlaidXL a Excel en Windows o Mac, localice la pestaña PlaidCloud de la cinta de opciones y abra el panel de tareas de PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

Usted instala PlaidXL una sola vez por equipo, no una vez por libro. A partir de entonces, la pestaña **PlaidCloud** aparece en la cinta de opciones de Excel en todos los libros que abra.

## Antes de empezar

- Use Excel para Microsoft 365, o Excel 2021 o posterior, en Windows o Mac.
- Su espacio de trabajo de PlaidCloud debe estar en una versión actual. En un espacio de trabajo más antiguo, las extracciones muestran **This PlaidCloud workspace needs an update for PlaidXL**; pida a su administrador que lo actualice.
- Si su organización administra los complementos de Office de forma centralizada, es posible que el administrador de Microsoft 365 deba implementar PlaidXL por usted. Si no puede instalar complementos por su cuenta, pídale que agregue el complemento **PlaidCloud**.

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
2. En el grupo **Conectar**, haga clic en **Open PlaidXL**.

El panel de tareas de PlaidXL se abre en el lado derecho de la ventana y le pide que inicie sesión. Continúe con [Iniciar sesión](/es/reference/cli/plaidxl/connect/).

El panel de tareas mantiene la sesión iniciada entre sesiones de trabajo, así que normalmente iniciará sesión una sola vez y después solo abrirá el panel de tareas cuando lo necesite.

## Si PlaidXL no aparece

- Cierre todas las ventanas de Excel y vuelva a abrir Excel. A menudo un complemento no aparece en la cinta de opciones hasta que Excel se reinicia.
- Busque en **Insertar → Mis complementos** (Windows) o **Insertar → Complementos → Mis complementos** (Mac) y seleccione **PlaidCloud** desde allí.
- Si su organización bloquea los complementos de la tienda, pida al administrador de Microsoft 365 que lo implemente.

Encontrará más soluciones en la página [Solución de problemas](/es/reference/cli/plaidxl/troubleshooting/).

## Relacionado

- [Iniciar sesión](/es/reference/cli/plaidxl/connect/): conecte el complemento a su espacio de trabajo
- [La cinta de opciones de PlaidCloud](/es/reference/cli/plaidxl/ribbon/): todos los comandos de la pestaña **PlaidCloud**
