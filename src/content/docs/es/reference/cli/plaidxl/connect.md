---
title: Iniciar sesión en PlaidXL
description: Conecte PlaidXL a su espacio de trabajo de PlaidCloud con su correo electrónico y su inicio de sesión habitual, incluidos el inicio de sesión único y la autenticación de dos factores, y después cierre sesión o cambie de espacio de trabajo.
sidebar:
  label: Iniciar sesión
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL le hace iniciar sesión como usted mismo, con el mismo inicio de sesión que usa para PlaidCloud en un navegador. No hay que escribir ninguna dirección de servidor ni se guarda ninguna contraseña en el libro.

## Iniciar sesión

1. Abra el panel de tareas: **PlaidCloud → Open PlaidXL**, o **Cuenta** en el grupo **Conectar**.
2. En **Enter your email**, escriba la dirección de correo electrónico que usa para PlaidCloud y haga clic en **Sign In**. PlaidXL recuerda la dirección para la próxima vez.
3. Si su correo electrónico pertenece a más de un espacio de trabajo, elija uno en **Select a workspace** y haga clic en **Sign In**. PlaidXL recuerda su elección. Si pertenece a un solo espacio de trabajo, PlaidXL lo elige por usted. Si no hay ningún espacio de trabajo vinculado al correo electrónico, el panel se lo indica; compruebe la dirección e inténtelo de nuevo.
4. Excel pregunta si desea permitir una ventana emergente. Permítala.
5. En la ventana emergente, inicie sesión como lo hace normalmente:
   - **PlaidCloud sign-in**: su correo electrónico, su contraseña y el código de dos factores que haya configurado.
   - **Single sign-on**: si ya ha iniciado sesión en su organización, este paso se completa automáticamente. De lo contrario, primero se abre la página de inicio de sesión de su organización.
6. Cuando la ventana emergente muestre **Authenticated successfully**, ciérrela si no se ha cerrado sola.

El encabezado del panel de tareas muestra ahora su espacio de trabajo y el proyecto vinculado al libro, con el menú de su cuenta al lado. Continúe con [Trabajar con tablas y dimensiones](/es/reference/cli/plaidxl/retrieve/).

Para configurar la autenticación de dos factores o el inicio de sesión único para su cuenta, consulte [Autenticación de miembros](/es/administration/access/member-authentication/).

### Iniciar sesión con su cuenta de Office

Si ha iniciado sesión en Office con una cuenta profesional de Microsoft Entra ID y PlaidXL no tiene ningún inicio de sesión guardado, PlaidXL busca sus espacios de trabajo a partir de esa cuenta, de modo que no tiene que escribir su correo electrónico:

- **Un espacio de trabajo**: PlaidXL empieza a iniciar su sesión en él. Permita la ventana emergente si Excel se lo pide; con el inicio de sesión único, se completa automáticamente. En Excel para la Web, haga clic primero en **Continue as** su cuenta.
- **Varios espacios de trabajo**: si el libro se usó por última vez con uno de ellos, PlaidXL inicia sesión en ese. De lo contrario, elija uno en **Select a workspace**.
- **Ningún espacio de trabajo**: se abre la pantalla del correo electrónico con su dirección ya escrita.

Si inicia sesión con un correo electrónico distinto del de su cuenta de Office, PlaidXL le indica cuál es. Después de **Log out**, PlaidXL espera a que inicie sesión usted mismo.

### Comandos antes de iniciar sesión

Puede hacer clic en cualquier comando de PlaidXL de la cinta de opciones antes de haber iniciado sesión. PlaidXL abre el panel de tareas para que inicie sesión o elija un proyecto, y después ejecuta el comando en la celda desde la que empezó.

## Mantener la sesión iniciada

PlaidXL mantiene su sesión iniciada en este equipo y la renueva en segundo plano mientras trabaja. Cuando abre el panel de tareas en una sesión posterior, va directamente a sus proyectos. Si su inicio de sesión ha caducado por completo, PlaidXL le pide de nuevo su correo electrónico. Un problema de red breve durante la renovación no cierra su sesión; PlaidXL lo intenta de nuevo.

## Qué puede ver

PlaidXL lee con sus permisos. Usted ve los proyectos que puede abrir en PlaidCloud, y las tablas y dimensiones que contienen, y nada más. Si falta un proyecto o una tabla, solicite acceso a un propietario del proyecto. Consulte [Organizaciones y espacios de trabajo explicados](/es/administration/access/overview/organizations-and-workspaces-explained/) para saber cómo funciona la pertenencia a un espacio de trabajo.

## Cerrar sesión o cambiar de espacio de trabajo

Haga clic en el menú de la cuenta (los tres puntos) en la parte superior derecha del panel de tareas. Muestra su nombre y su espacio de trabajo, con tres comandos:

- **Keyboard shortcuts** enumera los métodos abreviados de PlaidXL para que pueda cambiarlos. Consulte [Métodos abreviados de teclado](/es/reference/cli/plaidxl/ribbon/#métodos-abreviados-de-teclado).
- **Switch workspace** cierra su sesión y vuelve a la pantalla del correo electrónico, para que pueda elegir otro espacio de trabajo en **Select a workspace**. Inicie sesión en el nuevo espacio de trabajo cuando se le pida. Volver a un espacio de trabajo en el que ya ha iniciado sesión no requiere un nuevo inicio de sesión, y cancelar el inicio de sesión mantiene el espacio de trabajo en el que estaba.
- **Log out** borra su inicio de sesión y vuelve a la pantalla del correo electrónico.

Cada inicio de sesión funciona solo para el espacio de trabajo en el que se realizó. Todos inician sesión una vez después de este cambio. Cuando ha cerrado sesión, **Guardar** dice **Sign in to PlaidCloud to save.** y recuperar una dimensión dice **Sign in to PlaidCloud to retrieve a dimension.**

Su inicio de sesión lo comparten todos los libros que tenga abiertos, pero cada libro conserva su propio proyecto. El proyecto de un libro pertenece a un espacio de trabajo, así que después de cambiar, un libro vinculado a un proyecto del espacio de trabajo anterior no tiene proyecto hasta que elija uno. Consulte [El proyecto pertenece al libro](/es/reference/cli/plaidxl/retrieve/#el-proyecto-pertenece-al-libro).

## Tema claro y oscuro

El panel de tareas sigue el tema de Office y cambia cuando usted lo cambia.

## Teclado y lectores de pantalla

Las filas de las listas de proyectos, tablas y dimensiones reciben el foco del teclado y responden a **Enter** y **Space**. Un lector de pantalla anuncia la fila seleccionada, y los estados de selección y advertencia llevan un icono además de un color.

## Temas relacionados

- [Instalar PlaidXL](/es/reference/cli/plaidxl/install/): agregue el complemento y abra el panel de tareas
- [Solución de problemas](/es/reference/cli/plaidxl/troubleshooting/): cuando la ventana emergente de inicio de sesión no se abre o falta un espacio de trabajo
- [Ver y administrar espacios de trabajo](/es/administration/access/overview/viewing-and-managing-workspaces/): los espacios de trabajo a los que pertenece
