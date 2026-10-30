---
title: Deactivate Workspace Members
description: Desactive miembros del espacio de trabajo incluidos en una tabla de proyecto, identificados por dirección de correo electrónico o nombre de usuario.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## Descripción

Desactiva los miembros del espacio de trabajo indicados en una tabla de origen. Úselo para automatizar la baja de personas a partir de una lista de referencia (una extracción de RR. HH. o una revisión de accesos) en lugar de desactivar a cada persona a mano.

Combínelo con el paso [Get Workspace Members](/es/reference/workflow-steps/general/get-workspace-members/) para crear la lista de quienes ya no deberían tener acceso.

<Aside type="caution" title="Esto revoca el acceso">
  Todos los miembros coincidentes pierden el acceso cuando se ejecuta el paso.
  Compruebe que la tabla de origen contenga solo a quienes desea antes de programar este paso.
</Aside>

## Administradores del espacio de trabajo en la lista

[Solo un administrador del espacio de trabajo puede desactivar a otro administrador del espacio de trabajo](/es/administration/access/member-management/#cambio-de-un-administrador-del-espacio-de-trabajo). Cuando el paso se ejecuta sin derechos de administrador del espacio de trabajo y su lista incluye administradores, deja activos a esos administradores, desactiva a todos los demás y finaliza con un error cuyo mensaje indica cuántos miembros desactivó y nombra a cada administrador que dejó activo. Los miembros que desactivó permanecen desactivados. Para desactivar a un administrador, pida a un administrador del espacio de trabajo que lo haga en Identity.

## Configuración

### Parámetro de búsqueda de miembros

Cómo se hacen coincidir las filas de la tabla de origen con los miembros. Elija una opción:

- **Correo electrónico** (predeterminado)
- **Nombre de usuario**

## Relacionado

- [Pasos generales](/es/reference/workflow-steps/general/)
- [Get Workspace Members](/es/reference/workflow-steps/general/get-workspace-members/)
- [Administración de miembros](/es/administration/access/)
