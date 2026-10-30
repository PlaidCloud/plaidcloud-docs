---
title: Conector de SAP ECC y S/4HANA
description: Configure la conexión de SAP ECC / S/4HANA en PlaidCloud para integrar en sus flujos de trabajo datos financieros, logísticos y operativos de SAP mediante RFC.
sidebar:
  order: 1
  label: SAP ECC / S/4HANA
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-ecc.md
---

Un único tipo de conexión sirve tanto para SAP ECC como para SAP S/4HANA. A ambos se accede de la misma manera (llamadas a funciones remotas contra el servidor de aplicaciones), por lo que PlaidCloud no le pregunta con qué generación trabaja. En la pantalla **Conexiones**, elija **Nuevo → Instancia de SAP ECC / S/4HANA**.

Todos los [pasos de SAP](/es/reference/workflow-steps/sap/) se ejecutan contra una conexión de este tipo. Para buscar en SAP y extraer tablas, transacciones, informes y consultas de SAP guardadas, consulte [Extracciones ad hoc de SAP ECC / S/4HANA](/es/guides/connections/sap-adhoc-extract/).

## Documentación del proveedor

SAP ha eliminado toda la documentación de ECC y actualmente solo ofrece documentación de [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE). Las interfaces RFC que usa PlaidCloud son comunes a ambos.

## Configuración

Estos campos aparecen al crear o editar la conexión.

### Descripción de la cuenta

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre de la cuenta | Texto | Nombre para mostrar de esta conexión, visible dondequiera que un paso elija una conexión. Obligatorio. |
| Notas | Texto (varias líneas) | Notas opcionales sobre la conexión: a qué sistema apunta, quién es su propietario. |

### Entorno de SAP

| Campo | Tipo | Descripción |
|---|---|---|
| Cliente | Texto | Número de cliente de SAP, p. ej., `100`. Obligatorio. |
| Idioma | Selección | Idioma de inicio de sesión como código SAP de dos letras. De forma predeterminada es `EN`. Obligatorio. |
| Nivel de seguimiento | Selección | Nivel de detalle del seguimiento de RFC: Desactivado, Breve, Detallado o Completo. Déjelo en Desactivado a menos que esté diagnosticando un problema de conexión. Obligatorio. |
| Tipo de conexión | Opción | **Usar una única conexión directa** para acceder a un servidor de aplicaciones, o **Usar conexión de varios sistemas con equilibrio de carga** para pasar por un servidor de mensajes. Los campos siguientes se activan según esta elección. |

Al elegir **Usar una única conexión directa** se habilita:

| Campo | Tipo | Descripción |
|---|---|---|
| Host | Texto | Nombre de host o dirección IP del servidor de aplicaciones. |
| Número de sistema | Texto | Número de sistema SAP de dos dígitos, p. ej., `00`. |

Al elegir **Usar conexión de varios sistemas con equilibrio de carga** se habilita:

| Campo | Tipo | Descripción |
|---|---|---|
| Host de MS | Texto | Nombre de host o dirección IP del servidor de mensajes. |
| Servidor de MS | Texto | Puerto o nombre de servicio del servidor de mensajes. |
| ID del sistema | Texto | ID de sistema SAP de tres caracteres, p. ej., `PRD`. |
| Grupo | Texto | Grupo de inicio de sesión entre los que se equilibra la carga, p. ej., `PUBLIC`. |

### Credenciales de autenticación

| Campo | Tipo | Descripción |
|---|---|---|
| Usuario | Texto | Usuario de inicio de sesión de SAP para las llamadas RFC. Obligatorio. |
| Contraseña | Contraseña | Contraseña de ese usuario. Solo escritura: déjela en blanco al editar para conservar la contraseña almacenada. |

### Uso

| Campo | Tipo | Descripción |
|---|---|---|
| Activa (permitir acceso) | Interruptor | Indica si la conexión se puede usar. Desmárquela para pausar la conexión sin eliminarla. |
| Solo lectura | Interruptor | Restringe la conexión a operaciones de lectura. |

### Modelo de seguridad

| Campo | Tipo | Descripción |
|---|---|---|
| Modelo de seguridad | Selección | Quién puede usar esta conexión: Privado (solo propietarios), Solo miembros específicos, Solo grupos de seguridad específicos o Todos los miembros del espacio de trabajo. |

## Probar la conexión

**Probar conexión** en la ventana de la conexión inicia sesión con los datos anteriores e informa del resultado. Al editar una conexión existente y cambiar cualquier ajuste, vuelva a escribir la contraseña antes de probar: la almacenada no se envía junto con los valores editados.
