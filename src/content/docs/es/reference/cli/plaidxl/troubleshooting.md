---
title: Solución de problemas de PlaidXL
description: "Soluciones para los problemas habituales de PlaidXL: el complemento no aparece en la cinta de opciones, una ventana emergente de inicio de sesión que no se abre, espacios de trabajo o proyectos que faltan, tablas mostradas en rojo, recuperaciones lentas, errores en fórmulas y métricas de PlaidXL, valores escritos que no se guardan y guardados que se detienen."
sidebar:
  label: Solución de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## La pestaña PlaidCloud no está en la cinta de opciones

- Cierre todas las ventanas de Excel y vuelva a abrir Excel. Un complemento recién instalado suele aparecer solo después de reiniciar.
- Abra **Insert → My Add-ins** y seleccione **PlaidCloud**.
- Compruebe que usa Excel de escritorio para Microsoft 365, o Excel 2021 o posterior. Consulte [Instalar PlaidXL](/es/reference/cli/plaidxl/install/).
- Si su organización administra los complementos, pregunte a su administrador de Microsoft 365 si el complemento **PlaidCloud** se ha implementado para usted.

## La ventana emergente de inicio de sesión no se abre

Cuando hace clic en **Sign In**, Excel le pregunta si desea mostrar una ventana emergente. Permítala. Si descartó el aviso, haga clic en **Sign In** de nuevo.

Si la ventana emergente se abre pero no puede terminar de iniciar sesión, intente iniciar sesión en PlaidCloud en su navegador con el mismo correo electrónico. Un problema allí (una contraseña caducada o un dispositivo de dos factores que ya no tiene) debe resolverse primero en PlaidCloud. Consulte [Autenticación de miembros](/es/administration/access/member-authentication/).

## Un espacio de trabajo no aparece en la lista

**Select a workspace** enumera los espacios de trabajo a los que pertenece su dirección de correo electrónico. Si falta alguno, compruebe que escribió el mismo correo electrónico que usa para ese espacio de trabajo y después pida a un administrador del espacio de trabajo que confirme que usted es miembro. Consulte [Administrar los miembros del espacio de trabajo](/es/administration/access/overview/managing-workspace-members/).

Para pasar a otro espacio de trabajo al que pertenece, abra el menú de la cuenta y elija **Switch workspace**.

## Falta un proyecto, una tabla o una dimensión

PlaidXL muestra lo que su cuenta puede ver en PlaidCloud. Si falta un proyecto, pida a su propietario que le dé acceso. Si falta una tabla, compruebe que existe en el proyecto seleccionado y que se ha cargado con datos: una tabla en la que nunca se ha escrito muestra **Unable to get table metadata** cuando la selecciona.

Las carpetas de las listas de proyectos, tablas y dimensiones empiezan contraídas. Escriba parte del nombre en el cuadro de filtro de la parte superior de la lista para encontrar un elemento dentro de una carpeta.

## Una tabla se muestra en rojo

La tabla tiene más filas o columnas de las que cabe en una hoja de cálculo de Excel, o PlaidCloud no puede informar de su tamaño. Puede recuperarla, y las filas que no caben continúan en otras hojas, pero una tabla dividida entre hojas no se puede guardar. Seleccione **Avanzado** para filtrar las filas y desactive las columnas que no necesite hasta que quepa. Consulte [Tablas mostradas en rojo](/es/reference/cli/plaidxl/retrieve/#tablas-mostradas-en-rojo).

## Una recuperación es lenta

Excel es más lento con las tablas anchas. Desactive las casillas de las columnas que no necesite y filtre las filas con **Avanzado**. Recuperar solo los datos con los que trabaja es más rápido y genera un libro más pequeño.

## Una fórmula muestra un error

| Lo que ve | Qué comprobar |
|---|---|
| `#SPILL!` | Hay algo en las celdas que necesita el resultado. Borre las celdas de debajo o de al lado de la fórmula. |
| `#NAME?` | Excel no reconoce la función. Compruebe que PlaidXL está instalado (la pestaña **PlaidCloud** está en la cinta de opciones) y compruebe la ortografía con [la lista de funciones](/es/reference/cli/plaidxl/functions/). |
| Un error de una función `PLAIDXL` | Compruebe que ha iniciado sesión y que está seleccionado el proyecto correcto, y después compruebe con PlaidCloud todos los nombres de tablas, columnas, dimensiones y nodos: los nombres deben coincidir exactamente. |
| `CELL` indica que no se encuentra una columna de filtro | El primer argumento de `DIMENSION_REPR` es una columna de la tabla, no una dimensión. Use exactamente el nombre de la columna de la tabla. Consulte [Valores](/es/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `METRIC` o `METRIC_BREAKDOWN` | Pase el puntero sobre la celda para leer el motivo. Consulte [Errores de métricas](/es/reference/cli/plaidxl/functions/#errores-de-métricas). |
| `#VALUE!` de `CELL` o `CELLS` | Pase el puntero sobre la celda para leer el motivo que dio PlaidCloud, como una columna desconocida, un nodo que no existe o no tiene miembros, o un problema al calcular el valor. Compruebe los nombres con PlaidCloud. |
| `CELL` devuelve un total inesperado | Un nodo se acumula solo en una columna vinculada a su dimensión; en cualquier otra columna debe coincidir exactamente con un valor. Compruebe la columna y el nodo de cada filtro. |
| Los valores no cambian después de que cambien los datos o el proyecto | Haga clic en **Recalculate PlaidXL formulas** en el menú **Actualizar** de la cinta de opciones. |
| `MEASURE_TYPE` devuelve un error | Use uno de `sum`, `mean`, `median`, `min`, `max`, `std` o `var`, en minúsculas. |

## Las fórmulas devuelven datos de otro proyecto

Las funciones de PlaidXL leen del proyecto vinculado al libro. Abra el panel de tareas en ese libro, elija el proyecto para el que se creó el informe y después haga clic en **Recalculate PlaidXL formulas** en el menú **Actualizar** de la cinta de opciones. Cada libro tiene su propio proyecto, por lo que elegir uno en otro libro no cambia este. Consulte [El proyecto pertenece al libro](/es/reference/cli/plaidxl/retrieve/#el-proyecto-pertenece-al-libro).

## Se omiten las tablas de otro espacio de trabajo

Después de cambiar de espacio de trabajo, **Refresh All Tables** indica que no se actualizaron las tablas o dimensiones de otro espacio de trabajo de este libro, y no aparecen en **On this sheet**. Vuelva a recuperar cada tabla en el espacio de trabajo actual para vincularla.

## Un valor escrito no se guarda

Cuando escribe sobre una fórmula `CELL`, el panel de tareas indica lo que escribió y enumera lo que no escribió, con el motivo. Consulte [Escribir valores en PlaidCloud](/es/reference/cli/plaidxl/write-values/).

| Lo que ve | Qué hacer |
|---|---|
| Solo una celda que contiene una única fórmula `PLAIDXL.CELL` acepta un valor escrito | Escriba sobre una celda cuya fórmula sea un único `CELL`, opcionalmente multiplicado, dividido o negado. |
| Un argumento no se puede leer aquí | Los argumentos de `CELL` deben ser celdas o texto, no otros cálculos. |
| Un método de reparto, una forma o una retención se aplica solo a sumas | Códigos como `E1200`, `1200 like FY2025` y `H` funcionan solo en celdas **Suma**. En las demás, escriba un número simple. |
| Todos los miembros retenidos | Libere una retención con `H` y después vuelva a escribir el valor. |
| El espacio de trabajo aún no acepta valores escritos en Excel | Pida a su administrador que actualice el espacio de trabajo. |

## Un guardado se rechaza o se detiene

Un guardado escribe de inmediato y rara vez se detiene. Se detiene cuando:

| Lo que ve | Qué hacer |
|---|---|
| La fila de encabezado ya no coincide con las columnas recuperadas | Devuelva el encabezado a como se recuperó, o vuelva a recuperar la tabla. |
| Un valor no se puede convertir | No se escribe nada y se enumeran las filas. Corrija los valores para que coincidan con el tipo de datos de la columna. |
| La tabla continúa en otras hojas | Una tabla dividida entre hojas no se puede guardar. Recupérela con un filtro para que quepa en una sola hoja. |
| La tabla se recuperó con un filtro que Save no puede respetar | Vuelva a recuperarla con un filtro de reglas **igual a** e **in** unidas por **AND**, o sin filtro. |
| Hay filas fuera de su acceso a filas | No se guarda nada. Quite esas filas y después guarde de nuevo. |
| La hoja no está vinculada a una tabla | Primero recupere la tabla en la hoja. Solo las tablas recuperadas en la hoja activa aparecen en **On this sheet**. |

Para deshacer un guardado, haga clic en **Deshacer** en el mensaje o en **Undo last write** en la cinta de opciones. El punto de restauración se conserva durante 7 días. Consulte [Guardar una tabla en PlaidCloud](/es/reference/cli/plaidxl/retrieve/#guardar-una-tabla-en-plaidcloud).

## Contenido relacionado

- [Instalar PlaidXL](/es/reference/cli/plaidxl/install/)
- [Iniciar sesión en PlaidXL](/es/reference/cli/plaidxl/connect/)
- [Obtener ayuda](/es/guides/support/getting-help/): abra un ticket de soporte
