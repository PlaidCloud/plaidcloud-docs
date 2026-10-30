---
title: Workflow Explorer
description: Verwenden Sie den PlaidCloud Workflow Explorer, um Workflow-Details, Schrittkonfigurationen, den Ausführungsverlauf und Abhängigkeitsinformationen anzuzeigen.
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

Um die Details eines Workflows anzuzeigen, suchen Sie ihn im Projekt und doppelklicken Sie darauf, um den Workflow im Explorer zu öffnen.

![Workflow Explorer](/images/workflow_explorer.png)

Von hier aus können Sie Workflow-Schritte verwalten, einschließlich des Erstellens oder Ändern vorhandener Workflow-Schritte, des Änderns der Reihenfolge, des Ausführens von Schritten und so weiter.

## Einen Schritt erstellen

Klicken Sie auf **Schritt erstellen** und wählen Sie einen Schritttyp. Ist in der Liste ein Schritt ausgewählt, beginnt ein neuer Schritt vom Typ Table Extract, Table Inner Join, Table Outer Join, Table Anti Join, Table Cross Join oder Table Lookup mit der Tabelle, die dieser Schritt schreibt: Sie wird zur Quelle des neuen Schritts (**Table 1** bei einem Join), und die Spalten werden so ausgefüllt, wie es **Quelle untersuchen** tun würde. Ein Hinweis am unteren Rand des Formulars weist darauf hin. Ändern Sie die Quelle, wenn der neue Schritt etwas anderes lesen soll. Nichts wird gespeichert, bis Sie den Schritt speichern.
