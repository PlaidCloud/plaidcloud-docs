---
title: Iniciar sesión en PlaidXL
description: Conecte PlaidXL a su espacio de trabajo de PlaidCloud con su correo electrónico y su método habitual de inicio de sesión, incluidos el inicio de sesión único y la autenticación de dos factores, y después cierre sesión o cambie de espacio de trabajo.
sidebar:
  label: Iniciar sesión
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL inicia sesión con su propia identidad, mediante el mismo inicio de sesión que usa para PlaidCloud en un navegador. No hay que escribir ninguna dirección de servidor ni se guarda ninguna contraseña en el libro.

## Iniciar sesión

1. Abra el panel de tareas: **PlaidCloud → Show Taskpane**.
2. En **Enter your email**, escriba la dirección de correo electrónico que usa para PlaidCloud y haga clic en **Sign In**.
3. Si su correo electrónico pertenece a más de un espacio de trabajo, elija uno en **Select a tenant** y haga clic en **Sign In**. (Un *tenant* en PlaidXL es su espacio de trabajo de PlaidCloud). Si pertenece a un solo espacio de trabajo, PlaidXL lo elige por usted.
4. Excel le pregunta si desea permitir una ventana emergente. Permítala.
5. En la ventana emergente, inicie sesión como lo hace habitualmente:
   - **Inicio de sesión de PlaidCloud**: su correo electrónico, su contraseña y el código de dos factores que haya configurado, si corresponde.
   - **Inicio de sesión único**: si ya inició sesión en su organización, este paso se completa automáticamente. De lo contrario, primero se abre la página de inicio de sesión de su organización.
6. Cuando la ventana emergente muestre **Authenticated successfully**, ciérrela si no se ha cerrado sola.

El panel de tareas ahora muestra **Connected to** con el ID de su espacio de trabajo **as** su nombre de usuario, con sus proyectos listados debajo. Continúe con [Trabajar con tablas y dimensiones](/es/reference/cli/plaidxl/retrieve/).

Para configurar la autenticación de dos factores o el inicio de sesión único en su cuenta, consulte [Autenticación de miembros](/es/administration/access/member-authentication/).

## Mantener la sesión iniciada

PlaidXL mantiene su sesión iniciada en este equipo y la renueva en segundo plano mientras trabaja. Cuando abra el panel de tareas en una sesión posterior, irá directamente a sus proyectos. Si su sesión ha caducado por completo, PlaidXL le solicita de nuevo su correo electrónico.

## Qué puede ver

PlaidXL lee con sus permisos. Usted ve los proyectos que puede abrir en PlaidCloud, y las tablas y dimensiones que contienen, y nada más. Si falta un proyecto o una tabla, solicite acceso a un propietario del proyecto. Consulte [Explicación de organizaciones y espacios de trabajo](/es/administration/access/overview/organizations-and-workspaces-explained/) para saber cómo funciona la pertenencia a un espacio de trabajo.

## Cerrar sesión o cambiar de espacio de trabajo

Haga clic en **Logout** en la parte superior del panel de tareas. PlaidXL borra su sesión y vuelve a la pantalla del correo electrónico.

Para trabajar en otro espacio de trabajo, cierre sesión, vuelva a iniciar sesión y elija el otro espacio de trabajo en **Select a tenant**. PlaidXL trabaja con un solo espacio de trabajo a la vez, para todos los libros que tenga abiertos.

## Tema claro y oscuro

El panel de tareas sigue el tema de Office. Para fijarlo en claro u oscuro, haga clic en el botón del sol o la luna en la parte superior izquierda del panel de tareas.

## Temas relacionados

- [Instalar PlaidXL](/es/reference/cli/plaidxl/install/): agregue el complemento y abra el panel de tareas
- [Solución de problemas](/es/reference/cli/plaidxl/troubleshooting/): qué hacer cuando la ventana emergente de inicio de sesión no se abre o falta un espacio de trabajo
- [Ver y administrar espacios de trabajo](/es/administration/access/overview/viewing-and-managing-workspaces/): los espacios de trabajo a los que pertenece
