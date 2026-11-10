---
title: Administración de archivos
description: Administre cuentas de almacenamiento de archivos en PlaidCloud para importar y exportar datos mediante CSV, Excel, Parquet y otros formatos de archivo.
sidebar:
  label: Descripción general
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents: almacene, organice, busque y comparta archivos junto con sus datos y flujos de trabajo. Los documentos pueden provenir de cualquier cuenta de almacenamiento conectada y utilizarse como referencia en los flujos de trabajo.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Las cuentas de almacenamiento conectadas, como S3, Google Cloud Storage y OneDrive, alimentan PlaidCloud Documents, donde los archivos se almacenan, organizan, buscan y comparten. Luego, los pasos de los flujos de trabajo hacen referencia a esos archivos para importar y exportar datos." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">cuentas de almacenamiento</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Documentos</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">almacenar · organizar · buscar · compartir</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">pasos del flujo de trabajo</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">importar · exportar archivos</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Los archivos llegan a Documentos desde cualquier cuenta de almacenamiento conectada; allí los almacena, organiza, busca y comparte, y luego los usa como referencia desde los pasos de los flujos de trabajo para importar y exportar datos.</figcaption>
</figure>

## El espacio de Documentos

**Documento** se abre con una barra lateral a la izquierda y, junto a ella, la página que usted elija. Los miembros que no pueden abrir una página no ven su elemento.

| Elemento de la barra lateral | Qué muestra |
|---|---|
| **Resumen** | Mosaicos de sus cuentas (**Cuentas**, **Compartidas**, **Privadas para usted**, **Buckets administrados**, **Servicios externos** y **Deshabilitado** cuando una cuenta requiere atención), archivos **Anclados**, **Cuentas por servicio** y **Quién puede usarlas**. Seleccione un archivo anclado para abrir **Examinar** en su carpeta con el archivo seleccionado. |
| **Examinar** | El explorador de archivos. Elija la cuenta en la lista del encabezado de la página. Consulte [Uso de las cuentas de documentos](/es/guides/documents/using-document/). |
| **Compartidas** | Cuentas compartidas con usted. Haga doble clic en una fila para examinarla. |
| **Mis privadas** | Cuentas que solo usted puede usar. Haga doble clic en una fila para examinarla. |
| **Administrar** | Cuentas de las que es propietario, con **Nombre**, **Servicio**, **Tipo de seguridad**, **Estado** y **Descripción**. Un administrador del espacio de trabajo ve aquí todas las cuentas de documentos y puede administrar cualquiera de ellas. |

La barra lateral muestra un recuento junto a **Compartidas**, **Mis privadas** y **Administrar**. El Resumen tiene los botones **Examinar archivos** y **Nueva cuenta** para empezar rápidamente.

### Acciones de fila en Administrar

Abra el menú **⋯** de una fila, haga clic con el botón derecho en la fila o use el menú **Acciones** de la barra de herramientas para:

- **Abrir** y **Editar**, que abren la página de la cuenta.
- **Clonar…**, **Historial de versiones** y **Dónde se usa…**. Consulte [Dónde se usa y reasignación](/es/guides/documents/account-management/document-account-used-by/).
- **Quién puede usarla**, con **Miembros**, **Grupos**, **Agentes** y **Propietarios**. Consulte [Control del acceso a las cuentas de documentos](/es/guides/documents/account-management/control-document-account-access/).
- **Habilitar** o **Deshabilitar**, y **Eliminar**.

### La página de la cuenta

**Nueva cuenta**, **Abrir** y **Editar** muestran la cuenta como una página, con **Administrar cuentas** en la parte superior para volver. Tiene tarjetas para:

- **General**: el nombre, el servicio, el bucket y la ruta de inicio de la cuenta.
- **Acceso**: el modelo de seguridad y quién puede usar la cuenta. **Miembros**, **Grupos**, **Agentes** y **Propietarios** tienen cada uno un vínculo **Editar** que abre el mismo selector que el menú de fila.
- **Credenciales**: campos de solo escritura para el servicio que eligió. Una nota **Credenciales guardadas** indica que las credenciales están establecidas, y los valores guardados nunca se muestran. Deje un campo en blanco para conservar lo que está guardado. Las cuentas SFTP también tienen **Probar conexión**.
- **SSH**: la configuración de la clave, solo para cuentas SFTP.

El encabezado tiene **Examinar**, **Dónde se usa** y un menú **Acciones** con **Clonar**, **Historial de versiones**, **Habilitar** o **Deshabilitar** y **Eliminar**. Si sale de una página con cambios sin guardar, PlaidCloud le pregunta si desea descartarlos.

Los vínculos y marcadores antiguos a las pantallas de documentos siguen abriendo la página correspondiente.
