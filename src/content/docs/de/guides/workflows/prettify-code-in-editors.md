---
title: Code in Editoren formatieren (Prettify)
description: Formatieren Sie SQL-, JSON- und Ausdruckscode in den Schritteditoren von PlaidCloud-Workflows mit der Schaltfläche Formatieren oder Umschalt+Alt+F automatisch.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/prettify-code-in-editors.md
---

## Code in Editoren formatieren

Mehrere Schritteditoren in Workflows verwenden einen Code-Editor – die SQL-Schritte (Frame Extract SQL, Remote Execute SQL, Remote Direct SQL, Remote Export SQL und Import SQL), das **Result schema** (JSON) des LLM-Schritts und der Ausdruckseditor, der in den Flow-Bereichen durchgängig verwendet wird.

Jeder dieser Editoren hat eine Schaltfläche **Formatieren**, die den Code an Ort und Stelle neu formatiert – sie rückt ihn ein und gestaltet ihn einheitlich, damit er leichter zu lesen und zu prüfen ist. Sie können auch **Umschalt+Alt+F** (**Umschalt+Option+F** unter macOS) drücken, während sich der Cursor im Editor befindet.

## Was formatiert wird

- **SQL** – in ein lesbares mehrzeiliges Layout umgewandelt: eine Klausel pro Zeile, ausgerichtetes `CASE` / `WHEN` und aufgelöste verschachtelte Funktionen. Projektvariablen und Vorlagen-Token wie `{variable}`, `{{ ... }}` und `{% ... %}` bleiben exakt erhalten.
- **JSON** – mit zwei Leerzeichen neu eingerückt (zum Beispiel das Result schema des LLM-Schritts).
- **Ausdrücke** – PlaidCloud-Ausdrücke werden nach der Python-Standardformatierung formatiert: einheitliche Abstände um Operatoren und Kommas sowie Zeilenumbrüche bei langen Ausdrücken.

## Wissenswertes

- Die Formatierung ändert nie, was Ihr Code tut – nur wie er angeordnet ist. SQL-Schlüsselwörter und Bezeichner behalten ihre ursprüngliche Groß- und Kleinschreibung.
- Kann der Code nicht geparst werden (Syntaxfehler), lässt die Formatierung ihn unverändert und zeigt eine kurze Meldung an, sodass Sie nie Ihre Arbeit verlieren.
- Die Formatierung wird als einzelner Schritt angewendet – drücken Sie **Strg+Z** (**Cmd+Z** unter macOS), um sie rückgängig zu machen.
