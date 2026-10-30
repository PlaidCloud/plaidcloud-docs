---
title: Get Workspace Members
description: Escriba los miembros del espacio de trabajo en una tabla de proyecto y elija qué campos de identidad y de actividad se incluyen.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Descripción

Escribe los miembros del espacio de trabajo en una tabla de proyecto. Úselo para informar sobre los accesos, conciliar una lista de miembros con una fuente de RR. HH. o impulsar un paso posterior a partir de quién tiene acceso en ese momento.

## Configuración

### Información que se incluirá

Activados de forma predeterminada: **Apellido**, **Nombre**, **Correo electrónico**, **Nombre de usuario**, **Fecha de creación del miembro** y **Marca de tiempo del último inicio de sesión**.

### Configuración adicional

Desactivados de forma predeterminada:

- **Incluir miembros desactivados**: amplía la salida más allá de los miembros activos.
- **Modo de historial de inicio de sesión**: devuelve el historial de inicios de sesión en lugar de solo el último inicio de sesión.

## Relacionado

- [Pasos generales](/es/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/es/reference/workflow-steps/general/deactivate-workspace-members/)
- [Administración de miembros](/es/administration/access/)
