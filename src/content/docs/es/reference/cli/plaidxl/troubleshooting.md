---
title: Solución de problemas de PlaidXL
description: "Soluciones para problemas comunes de PlaidXL: el complemento no aparece en la cinta de opciones, la ventana emergente de inicio de sesión no se abre, faltan espacios de trabajo o proyectos, tablas que se muestran en rojo, recuperaciones lentas y errores en las fórmulas de PlaidXL."
sidebar:
  label: Solución de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## La pestaña PlaidCloud no aparece en la cinta de opciones

- Cierre todas las ventanas de Excel y vuelva a abrir Excel. Un complemento recién instalado suele aparecer solo después de reiniciar.
- Abra **Insert → My Add-ins** y seleccione **PlaidCloud**.
- Compruebe que usa Excel de escritorio para Microsoft 365, o Excel 2021 o posterior. Consulte [Instalar PlaidXL](/es/reference/cli/plaidxl/install/).
- Si su organización administra los complementos, pregunte al administrador de Microsoft 365 si el complemento **PlaidCloud** está implementado para usted.

## La ventana emergente de inicio de sesión no se abre

Cuando hace clic en **Sign In**, Excel le pregunta si desea mostrar una ventana emergente. Permítala. Si descartó el aviso, haga clic en **Sign In** de nuevo.

Si la ventana emergente se abre pero no puede terminar de iniciar sesión, intente iniciar sesión en PlaidCloud en su navegador con el mismo correo electrónico. Un problema allí, como una contraseña caducada o un dispositivo de dos factores que ya no tiene, debe resolverse primero en PlaidCloud. Consulte [Autenticación de miembros](/es/administration/access/member-authentication/).

## Un espacio de trabajo no aparece en la lista

**Select a tenant** lista los espacios de trabajo a los que pertenece su dirección de correo electrónico. Si falta uno, compruebe que escribió el mismo correo electrónico que usa para ese espacio de trabajo y luego pida a un administrador del espacio de trabajo que confirme que usted es miembro. Consulte [Administrar los miembros del espacio de trabajo](/es/administration/access/overview/managing-workspace-members/).

Para pasar a otro espacio de trabajo al que pertenece, haga clic en **Logout** e inicie sesión de nuevo.

## Falta un proyecto, una tabla o una dimensión

PlaidXL muestra lo que su cuenta puede ver en PlaidCloud. Si falta un proyecto, pida a su propietario que le dé acceso. Si falta una tabla, compruebe que existe en el proyecto seleccionado y que se ha cargado con datos: una tabla en la que nunca se ha escrito muestra **Unable to get table metadata** cuando la selecciona.

Las carpetas de las listas de proyectos, tablas y dimensiones aparecen contraídas. Escriba parte del nombre en el cuadro de filtro de la parte superior de la lista para encontrar un elemento dentro de una carpeta.

## Una tabla se muestra en rojo

La tabla tiene más filas o columnas de las que caben en una hoja de cálculo de Excel. Seleccione **Avanzado** para filtrar las filas y desactive las columnas que no necesite hasta que quepa. Consulte [Tablas que se muestran en rojo](/es/reference/cli/plaidxl/retrieve/#tablas-que-se-muestran-en-rojo).

## Una recuperación es lenta

Excel es más lento con las tablas anchas. Desactive las casillas de las columnas que no necesite y filtre las filas con **Avanzado**. Recuperar solo los datos con los que trabaja es más rápido y genera un libro más pequeño.

## Una fórmula muestra un error

| Qué ve | Qué comprobar |
|---|---|
| `#SPILL!` | Hay algo en las celdas que necesita el resultado. Borre las celdas situadas debajo o junto a la fórmula. |
| `#NAME?` | Excel no reconoce la función. Compruebe que PlaidXL está instalado (la pestaña **PlaidCloud** está en la cinta de opciones) y compruebe la ortografía con [la lista de funciones](/es/reference/cli/plaidxl/functions/). |
| Un error de una función `PLAIDXL` | Compruebe que ha iniciado sesión y que está seleccionado el proyecto correcto; después compruebe con PlaidCloud todos los nombres de tablas, columnas, dimensiones y nodos: los nombres deben coincidir exactamente. |
| `CELL` indica que no se encuentra una columna de filtro | El primer argumento de `DIMENSION_REPR` es una columna de la tabla, no una dimensión. Use exactamente el nombre de la columna de la tabla. Consulte [Valores](/es/reference/cli/plaidxl/functions/#valores). |
| `CELL` devuelve 0 o un total inesperado | Compruebe el nombre del nodo con la dimensión: un nodo que no existe no acumula nada y devuelve 0. Un nodo se acumula solo en una columna vinculada a su dimensión; en cualquier otra columna debe coincidir exactamente con un valor. |
| Los valores no cambian después de que cambian los datos o el proyecto | Fuerce un recálculo completo; en Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` devuelve un error | Use uno de `sum`, `mean`, `median`, `min`, `max`, `std` o `var`, en minúsculas. |

## Las fórmulas devuelven datos de otro proyecto

Las funciones de PlaidXL leen del proyecto seleccionado en el panel de tareas, y esa selección es compartida por todos los libros que tenga abiertos. Seleccione el proyecto para el que se creó el informe y luego fuerce un recálculo completo. **Establecer como predeterminado** guarda un proyecto en el libro, de modo que quede seleccionado al abrir allí el panel de tareas. Consulte [Establecer un proyecto predeterminado](/es/reference/cli/plaidxl/retrieve/#establecer-un-proyecto-predeterminado).

## Temas relacionados

- [Instalar PlaidXL](/es/reference/cli/plaidxl/install/)
- [Iniciar sesión en PlaidXL](/es/reference/cli/plaidxl/connect/)
- [Obtener ayuda](/es/guides/support/getting-help/): abra un ticket de soporte
