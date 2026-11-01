---
title: Iniciar sesión en PlaidXL
description: Conecte PlaidXL a su espacio de trabajo de PlaidCloud con su correo electrónico y su inicio de sesión habitual, incluidos el inicio de sesión único y la autenticación de dos factores, y luego cierre sesión o cambie de espacio de trabajo.
sidebar:
  label: Iniciar sesión
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL inicia sesión con su propia identidad, mediante el mismo inicio de sesión que utiliza para PlaidCloud en un navegador. No hay que escribir ninguna dirección de servidor ni se almacena ninguna contraseña en el libro.

## Iniciar sesión

1. Abra el panel de tareas: **PlaidCloud → Open PlaidXL**.
2. En **Enter your email**, escriba la dirección de correo electrónico que utiliza para PlaidCloud y haga clic en **Sign In**. PlaidXL recuerda la dirección para la próxima vez.
3. Si su correo electrónico pertenece a más de un espacio de trabajo, elija uno en **Select a workspace** y haga clic en **Sign In**. PlaidXL recuerda su elección. Si pertenece a un solo espacio de trabajo, PlaidXL lo elige por usted. Si ningún espacio de trabajo está vinculado al correo electrónico, el panel lo indica; compruebe la dirección e inténtelo de nuevo.
4. Excel le pregunta si desea permitir una ventana emergente. Permítala.
5. En la ventana emergente, inicie sesión como lo hace habitualmente:
   - **PlaidCloud sign-in**: su correo electrónico, su contraseña y el código de dos factores que haya configurado.
   - **Single sign-on**: si ya ha iniciado sesión en su organización, este paso se completa sin intervención. De lo contrario, primero se abre la página de inicio de sesión de su organización.
6. Cuando la ventana emergente muestre **Authenticated successfully**, ciérrela si no se ha cerrado sola.

El encabezado del panel de tareas muestra ahora su espacio de trabajo y el proyecto vinculado al libro, con el menú de su cuenta al lado. Continúe con [Trabajar con tablas y dimensiones](/es/reference/cli/plaidxl/retrieve/).

Para configurar la autenticación de dos factores o el inicio de sesión único para su cuenta, consulte [Autenticación de miembros](/es/administration/access/member-authentication/).

## Mantener la sesión iniciada

PlaidXL mantiene su sesión iniciada en este equipo y renueva su inicio de sesión en segundo plano mientras usted trabaja. Cuando abre el panel de tareas en una sesión posterior, va directamente a sus proyectos. Si su inicio de sesión ha caducado por completo, PlaidXL le pide de nuevo su correo electrónico. Un problema de red breve durante la renovación de su inicio de sesión no cierra su sesión; PlaidXL lo intenta de nuevo.

## Qué puede ver

PlaidXL lee con sus permisos. Usted ve los proyectos que puede abrir en PlaidCloud, y las tablas y dimensiones que contienen, y nada más. Si falta un proyecto o una tabla, solicite acceso a un propietario del proyecto. Consulte [Organizaciones y espacios de trabajo explicados](/es/administration/access/overview/organizations-and-workspaces-explained/) para saber cómo funciona la pertenencia a un espacio de trabajo.

## Cerrar sesión o cambiar de espacio de trabajo

Haga clic en el menú de la cuenta (los tres puntos) en la parte superior derecha del panel de tareas. Muestra su nombre y su espacio de trabajo, con dos comandos:

- **Log out** borra su inicio de sesión y vuelve a la pantalla del correo electrónico.
- **Switch workspace** cierra su sesión y vuelve a la pantalla del correo electrónico, para que pueda elegir otro espacio de trabajo en **Select a workspace**.

Su inicio de sesión lo comparten todos los libros que tenga abiertos, pero cada libro conserva su propio proyecto. El proyecto de un libro pertenece a un espacio de trabajo, así que después de cambiar, un libro vinculado a un proyecto del espacio de trabajo anterior no tiene proyecto hasta que elija uno. Consulte [El proyecto pertenece al libro](/es/reference/cli/plaidxl/retrieve/#el-proyecto-pertenece-al-libro).

## Tema claro y oscuro

El panel de tareas sigue su tema de Office y cambia cuando usted lo cambia.

## Teclado y lectores de pantalla

Las filas de las listas de proyectos, tablas y dimensiones reciben el foco del teclado y responden a **Enter** y **Space**. Un lector de pantalla anuncia la fila seleccionada, y los estados seleccionado y de advertencia llevan un icono además de un color.

## Relacionado

- [Instalar PlaidXL](/es/reference/cli/plaidxl/install/): agregue el complemento y abra el panel de tareas
- [Solución de problemas](/es/reference/cli/plaidxl/troubleshooting/): cuando la ventana emergente de inicio de sesión no se abre o falta un espacio de trabajo
- [Ver y administrar espacios de trabajo](/es/administration/access/overview/viewing-and-managing-workspaces/): los espacios de trabajo a los que pertenece
