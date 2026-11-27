---
title: Wo sich die Workflows befinden
description: Navigieren Sie zu PlaidCloud-Workflows in Ihren Projekten und verwalten Sie sie mit der Workflow-Oberfläche und den Projektnavigationswerkzeugen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/where-are-workflows.md
---

Workflows befinden sich in Projekten. So finden Sie sie:

1. Öffnen Sie im oberen Menü **Projekte**.
2. Klicken Sie auf das Projekt, das die gesuchten Workflows enthält.
3. Wechseln Sie zur Registerkarte **Workflows**.

Sie sehen jeden Workflow im Projekt, geordnet in einer ordnerartigen Hierarchie.

## Was Sie für jeden Workflow sehen

- **Status** – läuft, normal abgeschlossen oder mit einer Warnung bzw. einem Fehler beendet
- Zeitstempel für **Erstellt** und **Zuletzt aktualisiert** sowie die Namen der verantwortlichen Personen
- **Ordnerorganisation** – Workflows können in verschachtelten Ordnern gruppiert werden, um große Projekte leichter zu verwalten

Doppelklicken Sie auf einen Workflow, um den **Workflow Explorer** zu öffnen. Dort können Sie Schritte ansehen, den gesamten Workflow ausführen, einen einzelnen Schritt ausführen oder einen Bereich wählen.

## Warum ein Workflow möglicherweise nicht sichtbar ist

Welche Workflows Sie sehen, hängt von zwei Dingen ab:

- **Projektzugriff** – Ihr Workspace-Administrator gewährt Ihnen Zugriff auf bestimmte Projekte. Wenn Sie ein Projekt erwarten, es aber nicht sehen, bitten Sie einen Projektinhaber, Sie hinzuzufügen.
- **Anzeigerolle** – innerhalb eines Projekts ist Ihnen eine von drei Rollen zugewiesen:
  - **Architect** – kann alles sehen und bearbeiten
  - **Manager** – kann Workflows sehen und ausführen, aber nicht ändern
  - **Explorer** – eingeschränkte Sichtbarkeit; manche Workflows können ausgeblendet sein

Wenn Sie bestimmte Workflows erwarten und sie nicht sehen, filtert Ihre Rolle sie möglicherweise heraus. Ein Architect des Projekts kann bestätigen, was Sie sehen sollten.

Ihre Rolle entscheidet auch, ob Sie einen Schritt ändern können. Wenn Sie einen Workflow öffnen, aber nicht ändern können, öffnet sich das Schrittformular schreibgeschützt – seine Felder sind deaktiviert und die Schaltfläche **Speichern** ist ausgeblendet –, sodass Sie die Konfiguration eines Schritts lesen, aber nicht verändern können. Das gilt überall, wo sich das Formular öffnet: über das Zahnradsymbol und das Kontextmenü der Workflow-Tabelle, die visuelle Arbeitsfläche, das Projektraster **Schritte** und das Menü **Neuer Schritt**.

## Nicht gespeicherte Änderungen in einem Schrittfenster

Ein Schrittfenster kennzeichnet nicht gespeicherte Änderungen mit einem **•** in seinem Titel. Beim Schließen des Fensters mit **Esc**, dem **X**, **Abbrechen** oder der Schaltfläche seiner Registerkarte erscheint die Frage **Nicht gespeicherte Änderungen verwerfen?**, damit eine Bearbeitung nicht versehentlich verloren geht. Wählen Sie **Verwerfen**, um ohne Speichern zu schließen, oder gehen Sie zurück, um weiter zu bearbeiten.

## Ein Schritt hat sich geändert, seit Sie ihn geöffnet haben

**Speichern** in einem Schrittformular überschreibt nie eine Änderung, die nach dem Öffnen des Formulars gespeichert wurde, gleichgültig, ob Weave sie vorgenommen hat oder jemand anderes. Es wird nichts gespeichert: Das Formular bleibt mit Ihren Änderungen geöffnet, und eine Warnung mit dem Titel **Aktualisierung fehlgeschlagen** sagt *Dieser Schritt wurde geändert, seit Sie ihn geöffnet haben. Laden Sie ihn neu, um die neueste Version zu sehen; Ihre nicht gespeicherten Änderungen gehen dabei verloren.* Wählen Sie **Neu laden**, um den Schritt so anzuzeigen, wie er jetzt ist, und nehmen Sie Ihre Änderungen dann erneut vor. Das Hinzufügen oder Entfernen einer der Beschriftungen des Schritts zählt nicht als Änderung. Wenn andere Speichervorgänge den Schritt weiter ändern, während Ihrer geschrieben wird, sagt eine Meldung **Aktualisierung fehlgeschlagen** *Dieser Schritt hat sich beim Speichern ständig geändert. Versuchen Sie es erneut.* und nichts wird gespeichert; speichern Sie erneut, sobald sie aufhören.

Über die REST API gibt `GET /rest/v1/analyze/projects/{project_id}/transform/{step_id}` den Schritt mit seinem `_etag` zurück. Senden Sie ihn als `if_match` mit `PUT` an denselben Pfad zurück, und ein Speichern über eine neuere Änderung hinweg wird mit `412` abgelehnt, ohne dass etwas geschrieben wird. Ohne ihn gilt das zuletzt Gespeicherte. Ein `PUT`, das andere Speichervorgänge immer wieder überholen, wird mit `503` und demselben *Dieser Schritt hat sich beim Speichern ständig geändert. Versuchen Sie es erneut.* abgelehnt, und nichts wird geschrieben. Wenn ein `PUT` `labels` enthält und nur diese nicht geschrieben werden konnten, antwortet es mit `503` und *Der Schritt wurde gespeichert, seine Bezeichnungen jedoch nicht: Sie haben sich beim Schreiben ständig geändert. Legen Sie die Bezeichnungen erneut fest.* KI-Assistenten, die über MCP verbunden sind, erhalten dieselbe Prüfung, indem sie den `_etag` aus `step_describe` als `if_match` an `step_upsert` übergeben.

## Nächste Schritte

- [Workflow Explorer](/de/guides/workflows/workflow-explorer/) – was Sie in einem geöffneten Workflow tun können
- [Einen Workflow erstellen](/de/guides/workflows/create-workflow/) – einen neuen starten
- [Einen Workflow ausführen](/de/guides/workflows/run-a-workflow/) – durchgängig ausführen
