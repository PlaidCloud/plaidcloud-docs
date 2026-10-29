---
title: Embellecer (dar formato a) el código en los editores
description: Use el botón Embellecer o Shift+Alt+F para dar formato automáticamente al código SQL, JSON y de expresiones en los editores de pasos de los flujos de trabajo de PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## Embellecer el código en los editores

Varios editores de pasos de flujos de trabajo usan un editor de código: los pasos SQL (Frame Extract SQL, Remote Execute SQL, Remote Direct SQL, Remote Export SQL e Import SQL), el **Result schema** (JSON) del paso LLM y el Editor de expresiones que se usa en todas las áreas de flujo.

Cada uno de estos editores tiene un botón **Embellecer** que vuelve a dar formato al código en el mismo lugar, aplicando sangría y una disposición uniforme para que sea más fácil de leer y revisar. También puede pulsar **Shift+Alt+F** (**Shift+Option+F** en macOS) mientras el cursor está en el editor.

## Qué se formatea

- **SQL**: se reformatea con una disposición legible de varias líneas: una cláusula por línea, `CASE` / `WHEN` alineados y funciones anidadas desglosadas. Las variables del proyecto y los tokens de plantilla como `{variable}`, `{{ ... }}` y `{% ... %}` se conservan exactamente.
- **JSON**: se vuelve a aplicar sangría con dos espacios (por ejemplo, el Result schema del paso LLM).
- **Expresiones**: las expresiones de PlaidCloud se formatean con el formato estándar de Python: espaciado uniforme alrededor de operadores y comas, y saltos de línea en las expresiones largas.

## Qué debe saber

- Embellecer nunca cambia lo que hace el código, solo cómo está dispuesto. Las palabras clave y los identificadores de SQL conservan su uso original de mayúsculas y minúsculas.
- Si el código no se puede analizar (un error de sintaxis), Embellecer lo deja intacto y muestra un breve mensaje, de modo que nunca pierde su trabajo.
- El formato se aplica como un único paso: pulse **Ctrl+Z** (**Cmd+Z** en macOS) para deshacerlo.
