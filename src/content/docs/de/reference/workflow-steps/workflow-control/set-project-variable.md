---
title: Set Project Variable-Schritt
description: Legt Variablen auf Projektebene über einen PlaidCloud-Workflow-Schritt fest, um Werte zu speichern, auf die alle Workflows im Projekt zugreifen können.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable.md
---

## Beschreibung


Der Set Project Variable-Schritt legt Projektvariablen fest, die während des Workflows verwendet werden. Ein Variablenname und ein Wert dürfen eine beliebige Kombination gültiger Zeichen enthalten, einschließlich Leerzeichen. Variablen werden im Workflow referenziert, indem sie in geschweifte Klammern gesetzt werden. Beispielsweise wird *a_variable* in einer Transformation als *\{a_variable}* referenziert und kann so in etwas wie einer Formel oder einem Feldwert verwendet werden (z. B. \{a_variable} * 2).



## Variablenliste


Die Tabelle listet jede im Projekt registrierte Variable mit ihrem **Aktueller Wert** und ihrer **Notiz** auf, die bei jedem Öffnen des Schritts neu gelesen werden – so sehen Sie, was eine Variable aktuell enthält, bevor Sie entscheiden, worauf sie gesetzt werden soll.

Um eine Variable zu setzen, aktivieren Sie in ihrer Zeile **Festlegen** und geben Sie den neuen Wert unter **Wert festlegen** ein. Nur aktivierte Zeilen werden beim Ausführen des Schritts geschrieben. Ein Wert, den Sie eingeben, ohne **Festlegen** zu aktivieren, wird daher ignoriert. Sie können auch eine Variable setzen, die noch nicht registriert ist: Fügen Sie eine Zeile hinzu und setzen Sie sie auf dieselbe Weise – beim Ausführen des Schritts wird sie angelegt.







## Beispiele


Noch keine Beispiele ...
