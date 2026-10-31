---
title: Run SAP PCM Hyper Loader (paso)
description: Ejecute el Hyper Loader de SAP PCM desde un paso de flujo de trabajo de PlaidCloud para realizar cargas masivas de datos de alta velocidad en modelos de PCM.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## Descripción


Carga un modelo de SAP Profitability and Cost Management (PCM) mediante cargas directas de tablas. Este proceso es considerablemente más rápido que Databridge. El Hyper Loader admite prácticamente todas las tablas de datos, asignaciones y estructuras actuales de PCM.


Esta es la lista actual de destinos de carga disponibles:


* Alias de actividad
* Jerarquía dimensional de actividad
* Alias de inductor de actividad
* Jerarquía dimensional de inductor de actividad
* Valor de inductor de actividad
* Composición predeterminada de la lista de materiales
* Tarifa unitaria externa de la lista de materiales
* Composición de la lista de materiales
* Volumen de producción de la lista de materiales
* Unidades vendidas de la lista de materiales
* Alias de objeto de costo 1
* Jerarquía dimensional de objeto de costo 1
* Alias de objeto de costo 2
* Jerarquía dimensional de objeto de costo 2
* Alias de objeto de costo 3
* Jerarquía dimensional de objeto de costo 3
* Alias de objeto de costo 4
* Jerarquía dimensional de objeto de costo 4
* Alias de objeto de costo 5
* Jerarquía dimensional de objeto de costo 5
* Asignación de objeto de costo
* Inductor de objeto de costo
* Alias de partida
* Alias de detalle de partida
* Jerarquía dimensional de detalle de partida
* Valor de detalle de partida
* Jerarquía dimensional de partida
* Asignación directa de actividad de partida
* Asignación de inductor de recursos de partida
* Valor de partida
* Alias de período
* Jerarquía dimensional de período
* Alias de inductor de recursos
* Jerarquía dimensional de inductor de recursos
* División de inductor de recursos
* Valor de inductor de recursos
* Alias de centro de responsabilidad
* Jerarquía dimensional de centro de responsabilidad
* Ingresos
* Alias de ingresos
* Jerarquía dimensional de ingresos
* Alias de servicio
* Jerarquía dimensional de servicio
* Alias de distribución
* Jerarquía dimensional de distribución
* Valor de distribución
* Alias de versión
* Jerarquía dimensional de versión
* Alias de hoja de trabajo 1
* Jerarquía dimensional de hoja de trabajo 1
* Alias de hoja de trabajo 2
* Jerarquía dimensional de hoja de trabajo 2
* Valor de hoja de trabajo

## Nuestras credenciales


PlaidCloud es un socio oficial de SAP y un proveedor preferido de servicios relacionados con el diseño y la implementación de modelos de SAP PCM.


## Qué se comprueba al guardar

Cada origen de la pestaña **Pasos de carga** se almacena temporalmente en la tabla de carga elegida como su **Tabla de carga de destino**, y las columnas se emparejan por nombre. Al guardar, se rechaza el paso y se indica el origen cuando:

- Un origen no tiene tabla de carga de destino, o tiene una que no es una tabla de carga de PCM — *El origen 'activity_aliases' se carga en 'ACTIVITY', que no es una tabla de carga de PCM.*
- Las columnas de un origen no coinciden con las de su tabla de carga: falta una columna de la tabla de carga, tiene un tipo distinto del de la tabla de carga, o no tiene origen, expresión ni constante — *El origen 'activity_aliases' no coincide con la tabla de carga PPLOAD_ACTIVITY_AL: falta DEFAULTALIAS; no hay origen, expresión ni constante para ALIAS.* **Restablecer columnas de destino al esquema** vuelve a rellenar las columnas de destino de un origen a partir de su tabla de carga.
- Dos orígenes tienen el mismo nombre. Cada origen se exporta a un archivo con su nombre, de modo que uno sobrescribiría al otro — *El nombre de origen 'activity_aliases' se usa más de una vez; cada origen necesita el suyo, o uno sobrescribe al otro.*


## Ejemplos


Seleccione Agente que usar en la lista desplegable. Introduzca el nombre del modelo y seleccione la ubicación de la ruta de almacenamiento del paquete de carga; luego seleccione la carpeta secundaria deseada. Use la Selección de datos de la tabla que aparece a continuación para seleccionar la tabla de origen del modelo y la tabla de carga de destino. Al inspeccionar origen>>propagar, se mostrarán los datos de ambos lados de la tabla. Haga clic en “Guardar y ejecutar” cuando haya introducido los datos y agregado las expresiones que necesite.
