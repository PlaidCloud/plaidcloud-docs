---
title: Solución de problemas de PlaidXL
description: "Soluciones a los problemas habituales de PlaidXL: el complemento no aparece en la cinta, una ventana emergente de inicio de sesión que no se abre, espacios de trabajo o proyectos que faltan, tablas mostradas en rojo, recuperaciones lentas y errores en las fórmulas de PlaidXL."
sidebar:
  label: Solución de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## La pestaña PlaidCloud no aparece en la cinta

- Cierre todas las ventanas de Excel y vuelva a abrir Excel. Un complemento recién instalado suele aparecer solo después de reiniciar.
- Abra **Insertar → Mis complementos** y seleccione **PlaidCloud**.
- Compruebe que usa Excel de escritorio para Microsoft 365, o Excel 2021 o posterior. Consulte [Instalar PlaidXL](/es/reference/cli/plaidxl/install/).
- Si su organización administra los complementos, pregunte al administrador de Microsoft 365 si el complemento **PlaidCloud** está implementado para usted.

## La ventana emergente de inicio de sesión no se abre

Cuando hace clic en **Sign In**, Excel pregunta si se debe mostrar una ventana emergente. Permítala. Si descartó el aviso, haga clic en **Sign In** de nuevo.

Si la ventana emergente se abre pero no puede completar el inicio de sesión, intente iniciar sesión en PlaidCloud en su navegador con el mismo correo electrónico. Un problema allí (una contraseña vencida o un dispositivo de dos factores que ya no tiene) debe corregirse primero en PlaidCloud. Consulte [Autenticación de miembros](/es/administration/access/member-authentication/).

## Un espacio de trabajo no aparece en la lista

**Select a workspace** enumera los espacios de trabajo a los que pertenece su dirección de correo electrónico. Si falta uno, compruebe que escribió el mismo correo que usa para ese espacio de trabajo y luego pida a un administrador del espacio de trabajo que confirme que usted es miembro. Consulte [Administrar los miembros del espacio de trabajo](/es/administration/access/overview/managing-workspace-members/).

Para pasar a otro espacio de trabajo al que pertenece, abra el menú de la cuenta y elija **Switch workspace**.

## Falta un proyecto, una tabla o una dimensión

PlaidXL muestra lo que su cuenta puede ver en PlaidCloud. Si falta un proyecto, pida a su propietario que le dé acceso. Si falta una tabla, compruebe que existe en el proyecto seleccionado y que se ha cargado con datos: una tabla en la que nunca se ha escrito muestra **Unable to get table metadata** cuando la selecciona.

Las carpetas de las listas de proyectos, tablas y dimensiones aparecen contraídas. Escriba parte del nombre en el cuadro de filtro de la parte superior de la lista para encontrar un elemento dentro de una carpeta.

## Una tabla se muestra en rojo

La tabla tiene más filas o columnas de las que cabe en una hoja de cálculo de Excel. Seleccione **Advanced** para filtrar las filas y desmarque las columnas que no necesite, hasta que quepa. Consulte [Tablas mostradas en rojo](/es/reference/cli/plaidxl/retrieve/#tablas-mostradas-en-rojo).

## Una recuperación es lenta

Excel es más lento con las tablas anchas. Desmarque las casillas de las columnas que no necesite y filtre las filas con **Advanced**. Recuperar solo los datos con los que trabaja es más rápido y genera un libro más pequeño.

## Una fórmula muestra un error

| Lo que ve | Qué comprobar |
|---|---|
| `#SPILL!` | Hay algo en las celdas que necesita el resultado. Borre las celdas debajo o al lado de la fórmula. |
| `#NAME?` | Excel no reconoce la función. Compruebe que PlaidXL está instalado (la pestaña **PlaidCloud** está en la cinta) y compruebe la ortografía con [la lista de funciones](/es/reference/cli/plaidxl/functions/). |
| Un error de una función `PLAIDXL` | Compruebe que ha iniciado sesión y que el proyecto correcto está seleccionado, y luego compruebe cada nombre de tabla, columna, dimensión y nodo con PlaidCloud: los nombres deben coincidir exactamente. |
| `CELL` informa de que no se encuentra una columna de filtro | El primer argumento de `DIMENSION_REPR` es una columna de la tabla, no una dimensión. Use exactamente el nombre de la columna de la tabla. Consulte [Valores](/es/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `CELL` o `CELLS` | Pase el cursor sobre la celda para leer el motivo que dio PlaidCloud, como una columna desconocida, un nodo que no existe o no tiene miembros, o un problema al calcular el valor. Compruebe los nombres con PlaidCloud. |
| `CELL` devuelve un total inesperado | Un nodo se acumula solo en una columna vinculada a su dimensión; en cualquier otra columna debe coincidir exactamente con un valor. Compruebe la columna y el nodo de cada filtro. |
| Los valores no cambian después de que cambian los datos o el proyecto | Fuerce un recálculo completo; en Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` devuelve un error | Use uno de `sum`, `mean`, `median`, `min`, `max`, `std` o `var`, en minúsculas. |

## Las fórmulas devuelven datos de otro proyecto

Las funciones de PlaidXL leen del proyecto vinculado al libro. Abra el panel de tareas en ese libro, elija el proyecto para el que se creó el informe y luego fuerce un recálculo completo. Cada libro tiene su propio proyecto, por lo que elegir uno en otro libro no cambia este. Consulte [El proyecto pertenece al libro](/es/reference/cli/plaidxl/retrieve/#el-proyecto-pertenece-al-libro).

## Se omiten las tablas de otro espacio de trabajo

Después de cambiar de espacio de trabajo, el panel de tareas indica cuántas tablas con seguimiento pertenecen a otro espacio de trabajo y **Refresh All Tables** las omite. Recupere cada tabla de nuevo en el espacio de trabajo actual para vincularla.

## Un guardado se rechaza o se detiene

| Lo que ve | Qué hacer |
|---|---|
| Hay filas vacías dentro de la tabla | Una sola fila vacía se omite. Dos o más filas vacías seguidas, con datos debajo, detienen un guardado. Elimine las filas vacías o complételas y luego guarde de nuevo. |
| La tabla cambió desde que la recuperó | Alguien más guardó la tabla en PlaidCloud. Recupérela de nuevo y vuelva a aplicar sus ediciones. (PlaidCloud solo puede comprobarlo en algunos tipos de tabla; cuando no puede, la confirmación advierte de que se sobrescribirán los cambios de otras personas.) |
| No se puede convertir un valor | No se escribe nada y se enumeran las filas. Corrija los valores para que coincidan con el tipo de datos de la columna. |
| La hoja no está vinculada a una tabla | Primero recupere la tabla en la hoja. **Save to PlaidCloud…** aparece solo para las tablas recuperadas en la hoja activa. |

Para deshacer un guardado, haga clic en **Restore previous version** en el mensaje de confirmación, o abra la tabla en PlaidCloud y elija la versión anterior al guardado en el menú **As of**. El punto de restauración se conserva durante 7 días. Consulte [Guardar una tabla en PlaidCloud](/es/reference/cli/plaidxl/retrieve/#guardar-una-tabla-en-plaidcloud).

## Temas relacionados

- [Instalar PlaidXL](/es/reference/cli/plaidxl/install/)
- [Iniciar sesión en PlaidXL](/es/reference/cli/plaidxl/connect/)
- [Obtener ayuda](/es/guides/support/getting-help/): abra una incidencia de soporte
