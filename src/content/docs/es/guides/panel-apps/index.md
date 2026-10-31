---
title: Aplicaciones Panel
description: Cree e implemente aplicaciones de datos interactivas de HoloViz Panel en PlaidCloud, ya sea como aplicaciones estáticas que se ejecutan en el navegador o como aplicaciones de servidor compiladas desde un repositorio de git.
sidebar:
  label: Aplicaciones Panel
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Las aplicaciones Panel le permiten publicar aplicaciones interactivas de [HoloViz Panel](https://panel.holoviz.org/) (entradas parametrizadas, gráficos en vivo y tablas de datos incrustadas) directamente desde PlaidCloud. Usted las administra desde la pantalla **Mis aplicaciones Panel**, que enumera cada aplicación junto con su tiempo de ejecución, estado de compilación y URL.

Comience en [Panel Studio](/es/guides/panel-apps/studio/): elija **Nueva aplicación Studio** para crear una aplicación en PlaidCloud a partir de una aplicación en blanco, una tabla, una vista o la galería, sin ningún repositorio que configurar. Para necesidades a medida, publique con uno de los tiempos de ejecución siguientes, que se muestran en la columna **Tiempo de ejecución**:

- **WASM**: una aplicación estática que se ejecuta íntegramente en el navegador (Pyodide). Usted publica un archivo HTML ya compilado desde una cuenta de documentos. No hay ningún proceso de servidor ni nada que escalar; se sirve de inmediato.
- **Servidor**: una aplicación compilada desde un repositorio de git y ejecutada en el servidor. Al publicar, PlaidCloud compila su repositorio en un contenedor que permanece inactivo con cero réplicas, se activa con la primera solicitud a su URL, sirve (incluidas las actualizaciones en vivo) y vuelve a escalar a cero cuando está inactivo. Es la opción adecuada para aplicaciones que necesitan un entorno de ejecución de Python, cómputo en el servidor o bibliotecas que no pueden ejecutarse en el navegador.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Los dos tiempos de ejecución de las aplicaciones Panel. Una aplicación WASM es un archivo HTML ya compilado que se sirve directamente al navegador sin servidor. Una aplicación de servidor se compila desde un repositorio de git en un contenedor que permanece inactivo con cero réplicas, se activa con la primera solicitud en unos quince segundos, sirve y vuelve a escalar a cero cuando está inactivo." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">archivo HTML compilado</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">navegador · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">se sirve de inmediato</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Servidor</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">repo de git</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">compilar contenedor</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">inactivo · 0 réplicas</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">nada en ejecución</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1.ª sol.</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">sirviendo</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">se activa en ~15 s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">vuelve a 0 cuando está inactivo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Dos tiempos de ejecución: una aplicación <strong>WASM</strong> es un archivo HTML ya compilado que se sirve directamente al navegador; una aplicación de <strong>servidor</strong> se compila desde git, permanece inactiva en cero, se activa con la primera solicitud (~15 s), sirve y vuelve a escalar a cero.</figcaption>
</figure>

## Elegir un tiempo de ejecución

| | WASM | Servidor |
|---|---|---|
| Origen | Un archivo HTML publicado | Un repositorio de git (conexión, rama, punto de entrada) |
| Se ejecuta | En el navegador | En el servidor, con escalado a cero |
| Ideal para | Paneles de control ligeros y autónomos | Aplicaciones que necesitan cómputo en el servidor o bibliotecas completas de Python |
| Inicio en frío | Ninguno | La primera solicitud activa la aplicación (~15 segundos) |

## Siguientes pasos

- [Panel Studio](/es/guides/panel-apps/studio/): cree, edite, previsualice y publique una aplicación en PlaidCloud, sin ningún repositorio que configurar.
- [Implementar una aplicación Panel desde PlaidCloud Git](/es/guides/panel-apps/deploy-from-git/): el recorrido completo desde el repositorio hasta una aplicación servida, mediante una conexión administrada sin credenciales.
- [Crear aplicaciones Panel con Weave](/es/guides/panel-apps/build-with-weave/): describa la aplicación y apruebe el cambio exacto que propone Weave.
- [Crear una aplicación Panel](/es/guides/panel-apps/creating/): inicie una aplicación de Studio a partir de una aplicación en blanco, una tabla o la galería, o publique una aplicación de servidor desde git o una aplicación WASM desde un archivo.
- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): cree aplicaciones con el aspecto de PlaidCloud, en modo claro y oscuro, con filtros, cifras destacadas, una cuadrícula de datos paginada en el servidor, gráficos, formularios, botones de ejecución, configuración guardada e impresión.
- [La API de datos para aplicaciones Panel](/es/guides/panel-apps/data-api/): filtre, pagine, cuente y agregue tablas en el servidor.
- [Alertas y resúmenes](/es/guides/panel-apps/alerts-and-digests/): reciba una notificación push, un correo electrónico o un mensaje de Slack o Teams cuando una cifra supere un límite, o un resumen programado.
- [La galería de aplicaciones](/es/guides/panel-apps/gallery/): incluya una aplicación como plantilla y cree aplicaciones nuevas a partir de las incluidas.
- [Marca del proyecto y proyectos de aplicaciones](/es/guides/panel-apps/branding/): defina los colores y un logotipo para las aplicaciones de un proyecto, y asigne aplicaciones a proyectos.
- [Usar una aplicación Panel](/es/guides/panel-apps/using/): estado de la compilación, apertura de la aplicación, edición y eliminación.
- [Crear un agente de IA dentro de una aplicación Panel](/es/get-started/tutorials/panel-ai-agent/): un tutorial: dé a un agente de IA la API REST como herramientas, limitadas a los permisos del propio usuario.
