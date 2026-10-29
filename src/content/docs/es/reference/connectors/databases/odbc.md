---
title: ODBC
description: Configure una conexión ODBC en PlaidCloud mediante un DSN de sistema o un controlador ODBC en el equipo de un agente de PlaidLink, en Windows o Linux.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/odbc.md
---

**ODBC (Open Database Connectivity)** accede a una base de datos mediante la configuración de ODBC del equipo en el que se ejecuta un [agente de PlaidLink](/es/reference/cli/plaidlink/). Úselo para una base de datos que no tenga un conector dedicado de PlaidCloud, desde pasos de agente como [Agent Remote Export of SQL Result](/es/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). Para crear una, elija **ODBC** como tipo de conexión.

:::note
Una conexión ODBC requiere PlaidLink 1.2.31 o posterior en el agente. Consulte [Actualizar](/es/reference/cli/plaidlink/upgrade/).
:::

Una conexión ODBC funciona de una de dos maneras:

- **Mediante un DSN.** Deje **Controlador ODBC** en blanco e indique un origen de datos (DSN) configurado en el equipo del agente. El DSN contiene el controlador, el servidor, la base de datos y cualquier otro ajuste del controlador, y los **Atributos de conexión** pueden reemplazarlos. Funciona con cualquier controlador ODBC.
- **Mediante un controlador.** Elija o escriba un **Controlador ODBC** instalado en el equipo del agente y, a continuación, indique el servidor y la base de datos. PlaidCloud pasa al controlador un ajuste `Server` y un ajuste `Database`, seguidos de los **Atributos de conexión**. Funciona con los controladores de SQL Server de Microsoft. Para cualquier otro controlador, incluidos los demás que sugiere la lista, use un DSN.

## Documentación del proveedor
El controlador ODBC de cada base de datos tiene sus propios ajustes. Consulte la documentación del proveedor del controlador para conocer las palabras clave que acepta, tanto al crear un DSN como al escribir atributos de conexión.

## Crear el DSN en el equipo del agente

Configure el DSN en el equipo en el que se ejecuta el agente, como DSN de sistema, para que el agente lo encuentre con independencia de la cuenta con la que se ejecute.

### En Windows

1. Abra **Orígenes de datos ODBC (64 bits)**.
2. En la pestaña **DSN de sistema**, agregue un origen de datos que use el controlador ODBC de la base de datos e introduzca el servidor, la base de datos y cualquier otro ajuste que solicite el controlador.
3. Anote el **Nombre del origen de datos**. Lo introducirá en la conexión.

:::caution
El DSN debe ser un **DSN de sistema** de 64 bits. En Windows, el agente se ejecuta como un servicio, que no puede ver un DSN de usuario ni un DSN creado en el administrador de ODBC de 32 bits. En ese caso, el paso falla con `ODBC data source '<name>' is not defined on the agent machine`.
:::

### En Linux

En Linux, el agente accede a ODBC mediante unixODBC.

1. Instale unixODBC y el controlador ODBC de la base de datos.
2. Compruebe que el controlador esté registrado en `odbcinst.ini`, con su nombre entre corchetes. La mayoría de los paquetes de controladores se registran solos al instalarse, y `odbcinst -q -d` muestra los controladores registrados.
3. Agregue el origen de datos al archivo `odbc.ini` del sistema, como una sección con el nombre del DSN. Establezca `Driver` con el nombre del controlador registrado y agregue el servidor, la base de datos y cualquier otro ajuste que solicite el controlador:

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. Anote el nombre de la sección, aquí `Sales`. Lo introducirá en la conexión.

`odbcinst -j` muestra dónde están los archivos `odbcinst.ini` y `odbc.ini` del sistema, normalmente en `/etc`. Un DSN en el archivo `~/.odbc.ini` de un usuario solo se encuentra cuando el agente se ejecuta como ese usuario.

### En un contenedor

La imagen de contenedor de PlaidLink incluye unixODBC, pero ningún controlador ODBC. Para usar ODBC desde un agente que se ejecuta en Docker o Kubernetes, cree una imagen a partir de ella que instale el controlador y agregue a la imagen el archivo `odbc.ini` del sistema con el DSN, o móntelo en el contenedor. La imagen se ejecuta como el usuario `plaid`, así que cambie a `root` para instalar el controlador y vuelva a `plaid` después.

## Configuración

### Conexión de base de datos

| Campo | Obligatorio | Descripción |
|---|---|---|
| Controlador ODBC | No | Déjelo en blanco para conectarse mediante un DSN. De lo contrario, el nombre de un controlador ODBC instalado en el equipo del agente, exactamente como lo registra ese equipo: en Windows, tal como lo muestra **Orígenes de datos ODBC (64 bits)** en su pestaña **Controladores**, y en Linux, como el nombre de su sección en `odbcinst.ini`. La lista ofrece controladores comunes y puede escribir cualquier otro. Aquí solo funcionan los controladores de SQL Server de Microsoft. Para cualquier otro controlador, incluidos los demás que ofrece la lista, déjelo en blanco y use un DSN. El nombre de un controlador no puede contener llaves ni punto y coma. |
| Nombre del origen de datos (DSN) o servidor | Sí | Sin controlador, el nombre del DSN de sistema en el equipo del agente. Con un controlador, el nombre de host del servidor de base de datos, o `host,port` para SQL Server en un puerto no predeterminado. |
| Base de datos | Con un controlador | La base de datos que se abre. No está disponible sin un controlador, porque el DSN indica la suya, y al guardar se rechaza una base de datos sin controlador. |
| Atributos de conexión | No | Otros ajustes del controlador, como pares `KEY=value` separados por `;`. Consulte [Atributos de conexión](#atributos-de-conexión). |

La conexión no tiene campo de puerto. Para SQL Server en un puerto no predeterminado, agréguelo al servidor como `host,port`, porque los controladores de SQL Server de Microsoft no admiten una palabra clave de puerto. Con un DSN, establezca el puerto en el DSN o reemplácelo con un atributo como `PORT=5433` para un controlador que lo admita.

### Atributos de conexión

Los **Atributos de conexión** pasan ajustes de ODBC al controlador en cualquiera de los dos modos, escritos como los escribe ODBC:

- Con un controlador, se agregan después de los ajustes propios de la conexión. Úselos para cualquier otra cosa que el controlador necesite, como `ApplicationIntent=ReadOnly` para conectarse a una réplica de solo lectura.
- Con un DSN, reemplazan los ajustes propios del DSN, como `PORT=5433`, o `DBQ=MYLIB` para la biblioteca predeterminada de IBM i.

Separe los pares con `;`, como en `Encrypt=yes;ApplicationIntent=ReadOnly`. Encierre entre llaves un valor que contenga `;`, como en `KEY={first;second}`, y dentro de las llaves escriba `}` como `}}`. Las palabras clave llegan al controlador en mayúsculas; las palabras clave de ODBC no distinguen entre mayúsculas y minúsculas.

Al guardar se rechaza lo siguiente:

- texto que no sean pares `KEY=value`, incluida una llave que nunca se cierra y una palabra clave sin valor;
- una palabra clave indicada más de una vez, en cualquier combinación de mayúsculas y minúsculas;
- una palabra clave que la conexión establece desde sus propios campos: `DRIVER`, `DSN`, `SERVER`, `DATABASE`, `UID`, `PWD`, `USER`, `USERID`, `USERNAME` y `PASSWORD`;
- `FILEDSN` y `SAVEFILE`, que harían que el agente leyera los ajustes de la conexión desde un archivo de su equipo, o los escribiera en uno.

Las listas de conexiones ocultan los atributos, porque un controlador puede admitir allí su propia palabra clave de credenciales; el formulario de la propia conexión los muestra. Borre el campo para quitarlos. Introduzca el usuario y la contraseña en **Credenciales de autenticación**.

:::note
**ODBC Driver 18 for SQL Server** cifra la conexión y comprueba el certificado del servidor de forma predeterminada. Para un servidor con un certificado autofirmado, agregue `TrustServerCertificate=yes` a los atributos.
:::

### Credenciales de autenticación

| Campo | Descripción |
|---|---|
| Usuario | El usuario con el que se conecta. Mediante un DSN, déjelo en blanco para iniciar sesión según lo configurado en el DSN o, en SQL Server, agregue `TRUSTED_CONNECTION=Yes` a los atributos para iniciar sesión con la cuenta del propio agente. Con un controlador de SQL Server y sin usuario, la conexión inicia sesión con la cuenta del propio agente: su cuenta de Windows o, en Linux, su vale de Kerberos. |
| Usar autenticación de inicio de sesión único (sin contraseña, usuario opcional) | Se conecta sin una contraseña almacenada. |
| Contraseña | La contraseña del usuario (solo escritura). Déjela en blanco al editar para conservar la contraseña guardada. |

### Configuración de SSL y configuración de SSH

Estas pestañas no se aplican a una conexión ODBC. Establezca el cifrado y otras opciones del controlador en el DSN o en los atributos de conexión.

## Conexiones guardadas por una versión anterior

Las versiones anteriores de este formulario exigían una **Base de datos** y un controlador elegido de una lista fija, y rellenaban un **Puerto**, pero nunca pasaban el controlador, por lo que esas conexiones no podían conectarse. Abra la conexión y realice una de estas acciones:

- **Conéctese mediante un DSN:** borre **Controlador ODBC**, introduzca el DSN y guarde. Al guardar se borra la base de datos anterior.
- **Conéctese mediante un controlador de SQL Server:** compruebe que **Controlador ODBC** coincida con un controlador de SQL Server instalado en el equipo del agente. Muchos nombres de la lista anterior no eran los nombres con los que se registran los controladores.

Una conexión que conserva un controlador de la lista anterior se abre como una conexión de controlador. No se conecta hasta que el controlador sea un controlador de SQL Server instalado en el equipo del agente; para cualquier otra base de datos, conéctese mediante un DSN.

Al guardar también se borra el puerto anterior. Una conexión que solo tuvo un DSN, sin base de datos, se abre con **Controlador ODBC** en blanco.
